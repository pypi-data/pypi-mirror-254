"""Contains the implementation of the job client."""

import json
import logging
import logging.handlers
import os
import signal
import sys
import threading
import time
from types import FrameType, TracebackType
from typing import Any, Callable, Optional
from urllib.parse import urlparse

import grpc
from numerous.grpc import spm_pb2
from numerous.grpc.spm_pb2_grpc import FileManagerStub, SPMStub, TokenManagerStub

from numerous.cli.local import create_local_execution_from_repository
from numerous.client_common.grpc_retry import grpc_retry_unary
from numerous.sdk.connect.access_token import RefreshingAccessToken
from numerous.sdk.connect.auth import AccessTokenAuthMetadataPlugin
from numerous.sdk.connect.command_handler import CommandHandler
from numerous.sdk.connect.config import Config
from numerous.sdk.connect.file_manager import FileManager, FileUploadContext
from numerous.sdk.connect.hibernation import HibernationHandler
from numerous.sdk.connect.inputs import (
    HIBERNATE_SELF,
    HibernatingSourceAction,
    InputReader,
)
from numerous.sdk.connect.job_state import JobState
from numerous.sdk.connect.job_utils import JobIdentifier
from numerous.sdk.connect.reader import Reader
from numerous.sdk.connect.status_handler import JobStatus, StatusHandler
from numerous.sdk.connect.subscription import Subscription
from numerous.sdk.connect.writer import Writer
from numerous.sdk.models.group import Group
from numerous.sdk.models.job import Job
from numerous.sdk.models.job_time import JobTime
from numerous.sdk.models.optimization import OptimizationConfiguration
from numerous.sdk.models.parameter import Parameter
from numerous.sdk.models.project import Project
from numerous.sdk.models.scenario import Scenario


class JobLogHandler(logging.handlers.BufferingHandler):
    FLUSH_AFTER_SECONDS = 10.0

    def __init__(
        self,
        spm: SPMStub,
        identity: JobIdentifier,
        execution_id: str,
        current_root_log_level: int = 0,
    ) -> None:
        super().__init__(100)
        self._spm_client = spm
        self._project_id = identity.project_id
        self._scenario_id = identity.scenario_id
        self._execution_id = execution_id
        self._previous_root_log_level = current_root_log_level
        self._next_flush_time = time.monotonic() + JobLogHandler.FLUSH_AFTER_SECONDS

    def emit(self, record: logging.LogRecord) -> None:
        if logging.Logger.root.level > record.levelno:
            return

        super().emit(record)

    def shouldFlush(self, record: logging.LogRecord) -> bool:
        return super().shouldFlush(record) or time.monotonic() >= self._next_flush_time

    def flush(self) -> None:
        """Pushes log entries to the back-end, and clears the buffer."""

        self.acquire()
        try:
            self._push_log_entries()
            self.buffer.clear()
        finally:
            self._next_flush_time = time.monotonic() + JobLogHandler.FLUSH_AFTER_SECONDS
            self.release()

    @grpc_retry_unary()
    def _push_log_entries(self):
        if not self.buffer:
            return

        log_entries = []
        timestamps = []
        for record in self.buffer:
            log_entries.append(self.format(record))
            timestamps.append(record.created)

        self._spm_client.PushExecutionLogEntries(
            spm_pb2.LogEntries(
                execution_id=self._execution_id,
                log_entries=log_entries,
                timestamps=timestamps,
                scenario=self._scenario_id,
                project_id=self._project_id,
            )
        )

    def get_previous_root_level(self) -> int:
        return self._previous_root_log_level


class JobClient:
    """The JobClient is the recommended way to connect to the numerous platform."""

    def __init__(
        self,
        channel: grpc.Channel,
        identity: JobIdentifier,
        execution_id: str,
        config: Optional[Config] = None,
    ) -> None:
        """Initialize the job client with a gRPC channel. The channel must be
        configured with credentials.

        :param channel: A gRPC channel configured with required authorization.
        :param identity: Contains identity information for the job object and related objects.
        """

        self._config = Config() if config is None else config
        self._channel = channel
        self._spm_client = SPMStub(self._channel)
        self._file_manager_client = FileManagerStub(self._channel)
        self._identity = identity
        self._execution_id = execution_id
        self._logger: logging.Logger = self._create_logger()
        self._log_handler = self._add_job_log_handler_to_root()
        self._file_manager = FileManager(
            self._spm_client, self._identity.project_id, self._identity.scenario_id
        )
        self._job_state: Optional[JobState] = None
        self._job = None
        self._scenario_document: Optional[dict[str, Any]] = None
        self._project_document: Optional[dict[str, Any]] = None
        self._scenario: Optional[Scenario] = None
        self._project: Optional[Project] = None
        self._group: Optional[Group] = None
        self._reader: Optional[Reader] = None
        self._input_reader: Optional[InputReader] = None
        self._writer: Optional[Writer] = None
        self._terminate_callback: Optional[Callable] = None
        self._status_handler = StatusHandler(
            self._spm_client, self._identity, self._config
        )
        self._setup_sigterm_handling()

        self._hibernation_handler = HibernationHandler(
            self._spm_client,
            self._identity,
            self._execution_id,
            lambda: self.job_time.current_time,
            lambda: self.state,
        )
        self._command_handler = self._create_command_handler(self._hibernation_handler)

    def _setup_sigterm_handling(self) -> None:
        def _sigterm_handler(signalnum: int, frame: Optional[FrameType]):  # noqa: F841
            if self._hibernation_handler.hibernating:
                sys.exit(0)

            if self._terminate_callback:
                thread = threading.Thread(target=self._terminate_callback, daemon=True)
                thread.start()
                thread.join(timeout=self._config.terminate_handler_timeout)
            sys.exit(1)

        signal.signal(signal.SIGTERM, _sigterm_handler)

    def _create_command_handler(
        self, hibernating_handler: HibernationHandler
    ) -> CommandHandler:
        subscription = Subscription(
            self._identity.project_id,
            self._identity.scenario_id,
            self._spm_client,
            [
                ".".join(
                    (
                        "COMMAND",
                        self._identity.project_id,
                        self._identity.scenario_id,
                        self._identity.job_id,
                    )
                )
            ],
        )
        return CommandHandler(subscription, hibernating_handler)

    def _create_logger(self) -> logging.Logger:
        """Job Client Log Initialization"""
        job_client_logger = logging.getLogger("job_client")
        job_client_logger.setLevel(logging.INFO)
        return job_client_logger

    def _add_job_log_handler_to_root(self) -> JobLogHandler:
        root_level = logging.root.level
        if not logging.root.hasHandlers():
            logging.root.setLevel(logging.INFO)

        job_log_handler = JobLogHandler(
            self._spm_client, self._identity, self._execution_id, root_level
        )
        job_log_handler.setFormatter(logging.Formatter(fmt=logging.BASIC_FORMAT))
        logging.root.addHandler(job_log_handler)

        return job_log_handler

    def _remove_job_log_handler_from_root(self):
        job_log_handler = next(
            (item for item in logging.root.handlers if isinstance(item, JobLogHandler)),
            None,
        )
        if job_log_handler is not None:
            logging.root.handlers.remove(job_log_handler)
            logging.root.setLevel(job_log_handler.get_previous_root_level())

    def __enter__(self) -> "JobClient":
        """Return itself upon entering the context manager."""
        self.status = JobStatus.RUNNING
        return self

    def __exit__(
        self,
        exc_type: Optional[type[BaseException]],  # noqa: F841
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],  # noqa: F841
    ) -> Optional[bool]:
        """Closes the gRPC channel upon exiting the context manager."""
        self.close(exc_value)
        return None

    @staticmethod
    def connect(
        status: JobStatus = JobStatus.RUNNING, message: Optional[str] = None
    ) -> "JobClient":
        """Create a JobClient from environment variables.

        Uses the following environment variables:
         - `NUMEROUS_API_SERVER`
         - `NUMEROUS_API_PORT`
         - `NUMEROUS_API_REFRESH_TOKEN`
         - `NUMEROUS_PROJECT`
         - `NUMEROUS_SCENARIO`
         - `JOB_ID`
         - `NUMEROUS_EXECUTION_ID`
        """
        try:
            job_client = JobClient._from_environment()
        except KeyError:
            job_client = JobClient._from_numerous_repository()
        job_client.status = status
        job_client.message = message or "Running"
        return job_client

    @staticmethod
    def from_connection_params(
        hostname: str,
        port: str,
        refresh_token: str,
        identity: JobIdentifier,
        execution_id: str,
        config: Config,
    ) -> "JobClient":
        """Create a JobClient from connection parameters.

        :param hostname: Hostname of the numerous server
        :param port: gRPC port of the numerous server
        :param refresh_token: Refresh token for the execution.
        :param identity: Contains identity information for the job object and related objects.
        """
        token_manager = TokenManagerStub(
            grpc.secure_channel(
                f"{hostname}:{port}",
                grpc.ssl_channel_credentials(),
                JobClient.channel_options(config),
            )
        )

        authorized_channel = grpc.secure_channel(
            f"{hostname}:{port}",
            grpc.composite_channel_credentials(
                grpc.ssl_channel_credentials(),
                grpc.metadata_call_credentials(
                    AccessTokenAuthMetadataPlugin(
                        RefreshingAccessToken(token_manager, refresh_token)
                    )
                ),
            ),
            JobClient.channel_options(config),
        )

        return JobClient(authorized_channel, identity, execution_id, config)

    @staticmethod
    def channel_options(config: Config) -> list[tuple[str, Any]]:
        """Returns the default gRPC channel options."""
        return [
            ("grpc.max_message_length", config.grpc_max_message_size),
            ("grpc.max_send_message_length", config.grpc_max_message_size),
            ("grpc.max_receive_message_length", config.grpc_max_message_size),
        ]

    @staticmethod
    def _from_environment() -> "JobClient":
        """Create a JobClient from environment variables.

        Uses the following environment variables:
         - `NUMEROUS_API_SERVER`
         - `NUMEROUS_API_PORT`
         - `NUMEROUS_API_REFRESH_TOKEN`
         - `NUMEROUS_PROJECT`
         - `NUMEROUS_SCENARIO`
         - `JOB_ID`
         - `NUMEROUS_EXECUTION_ID`
        """
        return JobClient.from_connection_params(
            os.environ["NUMEROUS_API_SERVER"],
            os.environ["NUMEROUS_API_PORT"],
            os.environ["NUMEROUS_API_REFRESH_TOKEN"],
            JobIdentifier(
                os.environ["NUMEROUS_PROJECT"],
                os.environ["NUMEROUS_SCENARIO"],
                os.environ["JOB_ID"],
            ),
            os.environ["NUMEROUS_EXECUTION_ID"],
            config=Config.from_environment(),
        )

    @staticmethod
    def _from_legacy_client(client: Any) -> "JobClient":
        """Create a JobClient from a legacy :class:`~numerous.client.numerous_client.NumerousClient`.

        Connects to the same job as the legacy client is connected to.
        """
        from numerous.client import NumerousClient
        from numerous.client.common import initialize_grpc_channel

        if not isinstance(client, NumerousClient):
            raise TypeError(
                f"'client' argument must be of type NumerousClient, was {type(client).__name__}"
            )
        else:
            if client._refresh_token is None:
                raise RuntimeError("Legacy client does not have a refresh token")

            channel, _ = initialize_grpc_channel(
                refresh_token=client._refresh_token,
                token_callback=client._get_current_token,
                server=client._channel_server,
                port=client._channel_port,
                secure=client._channel_secure,
                instance_id=client._instance_id,
            )

            return JobClient(
                channel,
                JobIdentifier(client._project, client._scenario, client._job_id),
                client._execution_id,
                Config.from_environment(),
            )

    @staticmethod
    def _from_numerous_repository() -> "JobClient":
        repo, execution_id, refresh_token = create_local_execution_from_repository()
        if repo.remote is None:
            raise RuntimeError(
                f"Repository at {repo.path} does not have a remote configured."
            )
        if repo.scenario is None:
            raise RuntimeError(
                f"Repository at {repo.path} does not have a scenario checked out."
            )

        parsed_url = urlparse(repo.remote.api_url)
        port = parsed_url.port or (443 if parsed_url.scheme == "https" else 80)
        if parsed_url.hostname is None:
            raise RuntimeError(
                f"Repository at {repo.path} does not have a valid remote configured."
            )

        return JobClient.from_connection_params(
            parsed_url.hostname,
            str(port),
            refresh_token,
            JobIdentifier(
                repo.scenario.project_id,
                repo.scenario.id,
                repo.remote.job_id,
            ),
            execution_id,
            config=Config.from_environment(),
        )

    def open_output_file(self, file_name: str) -> FileUploadContext:
        """
        :param file_name: Output file name.
        :return: An object to be used under with statement.

        Example:
            >>> with JobClient.connect() as client:
            ...     with client.open_output_file("output_data") as output_file:
            ...         output_file.write("First file content")
            ...         output_file.write_from_file("first_file.csv")
            ...         output_file.write("Second file content")
            ...         output_file.write_from_file("second_file.csv")
        """
        return FileUploadContext(self._file_manager, file_name)

    def close(self, error: Optional[BaseException] = None) -> None:
        """Close the JobClient.

        Closes the JobClient's connection to the numerous platform, immediately
        terminating any active communication.

        :param error_occured: If `True`, sets the job status with `JobStatus.ERROR`.

        This method is idempotent.
        """
        if isinstance(error, SystemExit) and error.code == 0:
            error = None

        if error:
            self.log.error(
                "An error occured in the job. This may be due to an error in the job "
                "code. Please reach out to the developer with the error information "
                "below:",
                exc_info=error,
            )

        if self._writer is not None:
            self._writer.close(self._hibernation_handler.hibernating)

        self._log_handler.flush()
        self._set_completed_job_status(error is not None)
        self._remove_job_log_handler_from_root()
        self._complete_execution()
        self._status_handler.close()
        self._channel.close()
        self._command_handler.close()

    def _set_completed_job_status(self, error_occured: bool):
        if error_occured:
            self.status = JobStatus.FAILED
            self.message = "Error occured"
        elif self._hibernation_handler.hibernating:
            self.message = "Hibernating"
            self.status = JobStatus.HIBERNATING
        elif self.status not in (
            JobStatus.ERROR,
            JobStatus.FINISHED,
            JobStatus.STOPPED,
        ):
            self.message = "Finished"
            self.status = JobStatus.FINISHED

    def _complete_execution(self) -> None:
        """Signal to the back-end that the execution has ended."""
        self._spm_client.CompleteExecution(
            request=spm_pb2.CompleteExecutionMessage(
                execution=spm_pb2.ExecutionMessage(
                    project_id=self._identity.project_id,
                    scenario_id=self._identity.scenario_id,
                    job_id=self._identity.job_id,
                    execution_id=self._execution_id,
                ),
                hibernate=self._hibernation_handler.hibernating,
            )
        )

    @property
    def log(self) -> logging.Logger:
        """Return the Job Client logger for the job."""
        return self._logger

    def flush_logs(self) -> None:
        """Flush all buffered log messages, so that they are sent to the server."""
        self._log_handler.flush()

    @property
    def file_manager(self) -> FileManager:
        """Access the file manager of the job."""
        return self._file_manager

    @property
    def state(self) -> JobState:
        """The job state, which can be persisted across hibernations.

        It is a lazy property, that will load any remote state on access.
        """
        if self._job_state is None:
            self._job_state = JobState(
                self._spm_client, self._identity, self._execution_id
            )
        return self._job_state

    @property
    def parameters(self) -> dict[str, Parameter]:
        return self.job.parameters

    @property
    def project(self) -> Project:
        """The associated :class:`Project` configuration, with parameters.
        It is a lazy property, that will load the scenario data on access.
        """
        if self._project_document is None:
            self._project_document = self._get_project_document()

        if self._project is None:
            self._project = Project.from_document(
                self._project_document, self._file_manager_client
            )
        return self._project

    @property
    def scenario(self) -> Scenario:
        """The associated :class:`Scenario` configuration, with jobs, components,
        parameters and input variables.

        It is a lazy property, that will load the scenario data on access.
        """
        if self._scenario_document is None:
            self._scenario_document = self._get_scenario_document()

        if self._scenario is None:
            scenario_has_optimization_target = self._scenario_document.get(
                "optimizationTargetScenarioID", False
            )
            optimization = (
                OptimizationConfiguration(
                    self._spm_client,
                    self._identity.project_id,
                    self._identity.scenario_id,
                    self._scenario_document,
                )
                if scenario_has_optimization_target
                else None
            )

            self._scenario = Scenario.from_document(
                self._scenario_document,
                self._file_manager_client,
                self._status_handler,
                optimization,
                last_hibernate_time=self._hibernation_handler.last_hibernate_time,
            )
        return self._scenario

    @property
    def job_time(self) -> JobTime:
        """The associated time setup of the job, which contains start and end times
        of the simulation, and the duration.
        """

        return self.job.time

    def _get_scenario_document(self) -> dict[str, Any]:
        if self._scenario_document is None:
            response = self._spm_client.GetScenario(
                spm_pb2.Scenario(
                    project=self._identity.project_id,
                    scenario=self._identity.scenario_id,
                )
            )
            self._scenario_document = json.loads(response.scenario_document)
        return self._scenario_document

    def _get_project_document(self) -> dict[str, Any]:
        proj_data = self._spm_client.GetProject(
            spm_pb2.Project(project=self._identity.project_id)
        )
        return json.loads(proj_data.project_document)

    @property
    def group(self) -> Optional[Group]:
        if self._group is not None and self._group.id == self.scenario.group_id:
            return self._group
        response = self._spm_client.GetGroup(
            spm_pb2.Group(
                project=self._identity.project_id,
                group=self.scenario.group_id,
            )
        )
        self._group = Group.from_document(
            json.loads(response.group_document),
            self._file_manager_client,
            self.scenario.group_id,
        )
        return self._group

    @property
    def status(self) -> JobStatus:
        """Status of the job, reported to the platform.

        Getting the status returns a locally cached value.
        """
        return self._status_handler.status

    @status.setter
    def status(self, value: JobStatus) -> None:
        self._status_handler.status = value

    @property
    def message(self) -> str:
        """Status message of the job, reported to the platform. Is truncated to at most 32 characters upon setting.

        Getting the status message returns a locally cached value.
        """
        return self._status_handler.message

    @message.setter
    def message(self, value: str):
        self._status_handler.message = value

    @property
    def progress(self) -> float:
        """Progress of the job, reported to the platform. Is clamped between 0.0 and 100.0 upon setting.

        Getting the progress returns a locally cached value.
        """
        return self._status_handler.progress

    @progress.setter
    def progress(self, value: float):
        self._status_handler.progress = value

    @property
    def reader(self) -> Reader:
        """Data reader for the job."""
        if self._reader is None:
            self._reader = Reader(
                self._spm_client,
                self._identity,
                self._execution_id,
            )
        return self._reader

    @property
    def writer(self) -> Writer:
        """Data writer for the job."""
        if self._writer is None:
            self._writer = Writer(
                self._spm_client,
                self._identity,
                self.job_time.start,
                self._execution_id,
                self._config.grpc_max_message_size,
                flush_margin_bytes=self._config.grpc_max_message_size // 8,
            )

        return self._writer

    def hibernate(self) -> None:
        """Hibernate the current job execution

        Terminates the Python process, committing the job state to the
        back-end. The job can be resumed again, and the state can be reloaded
        to continue.

        If the job is scheduled, it will then follow its schedule, and be
        resumed at the next scheduled resume.
        """
        self._hibernation_handler.hibernate()

    def set_terminate_callback(self, callback: Callable[[], Any]) -> None:
        """Set a custom function to be called if the job is terminated."""
        self._terminate_callback = callback

    def set_hibernate_callback(self, callback: Callable[[], Any]) -> None:
        """Set a custom function to be called if the job is hibernated."""
        self._hibernation_handler.callback = callback

    @property
    def job(self) -> Job:
        """The model of the current job."""
        return self.scenario.jobs[self._identity.job_id]

    def read_inputs(
        self,
        step: float,
        repeat_spacing: Optional[float] = None,
        hibernating_source_action: HibernatingSourceAction = HIBERNATE_SELF,
        update_progress: bool = False,
    ) -> InputReader:
        """Get an iterator over all input variables in the scenario.

        This method can only be called once in the job runtime.

        :param step: The distance (in time) between each read. Zero-order hold is used
            for values at steps that are not in the original data set.
        :param repeat_spacing: The distance (in time) between the last data point of the
            source data set, and the repeated first data point when repeating.

        Returns an :class:`~numerous.sdk.connect.inputs.InputReader`, that can be
        iterated over.

        Example:
            >>> result = 0
            >>> with JobClient.connect() as job_client:
            ...     for t, data in job_client.read_inputs(step=3600.0):
            ...          result += data["component_name.input_variable_id"]
        """

        if self._input_reader:
            raise RuntimeError("You can only read inputs once during a job runtime.")

        self._input_reader = InputReader(
            self._spm_client,
            hibernation_handler=self._hibernation_handler,
            identity=self._identity,
            execution_id=self._execution_id,
            job=self.job,
            input_sources=self.scenario.input_sources,
            input_variables=self.scenario.input_variables,
            step=step,
            repeat_spacing=repeat_spacing,
            hibernating_source_action=hibernating_source_action,
            update_progress=update_progress,
        )

        return self._input_reader
