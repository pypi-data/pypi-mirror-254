import threading
from enum import Enum
from time import sleep

from numerous.grpc import spm_pb2
from numerous.grpc.spm_pb2_grpc import SPMStub

from numerous.client_common.grpc_retry import grpc_retry_unary
from numerous.sdk.connect.config import Config
from numerous.sdk.connect.job_utils import JobIdentifier


class JobStatus(str, Enum):
    INITIALIZING = "initializing"
    RUNNING = "running"
    STOPPED = "stopped"
    FINISHED = "finished"
    ERROR = "error"
    FAILED = "failed"
    HIBERNATING = "hibernating"


class StatusHandler:
    """Handles job status updates, so they are not done too frequently."""

    def __init__(
        self,
        spm_client: SPMStub,
        identity: JobIdentifier,
        config: Config,
    ) -> None:
        self._spm_client = spm_client
        self._identity = identity
        self._running = True
        self._minimum_update_interval = config.min_status_update_interval_seconds
        self._max_status_message_length = config.max_status_message_length
        self._status: JobStatus = JobStatus.INITIALIZING
        self._progress: float = 0.0
        self._message: str = ""
        self._status_updater_continue = threading.Event()
        self._status_updater_thread = threading.Thread(
            name="StatusUpdater", target=self._status_updater, daemon=True
        )
        self._status_updater_thread.start()

    def close(self):
        self._running = False
        self._status_updater_continue.set()
        self._status_updater_thread.join()

    def _status_updater(self) -> None:
        self._set_scenario_progress()
        while self._running:
            sleep(self._minimum_update_interval)
            self._status_updater_continue.wait()
            self._status_updater_continue.clear()
            self._set_scenario_progress()

    @property
    def status(self) -> JobStatus:
        return self._status

    @status.setter
    def status(self, value: JobStatus) -> None:
        if self._status == value:
            return
        self._status = value
        self._status_updater_continue.set()

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, value: str) -> None:
        truncated = value[: self._max_status_message_length]
        if truncated == self._message:
            return
        self._message = truncated
        self._status_updater_continue.set()

    @property
    def progress(self) -> float:
        return self._progress

    @progress.setter
    def progress(self, value: float) -> None:
        clamped = _clamp(value, 0.0, 100.0)
        if clamped == self._progress:
            return
        self._progress = clamped
        self._status_updater_continue.set()

    @grpc_retry_unary()
    def _set_scenario_progress(self):
        self._spm_client.SetScenarioProgress(
            spm_pb2.ScenarioProgress(
                project=self._identity.project_id,
                scenario=self._identity.scenario_id,
                job_id=self._identity.job_id,
                status=self._status.value,
                progress=self._progress,
                message=self._message,
            )
        )


def _clamp(value: float, minimum: float, maximum: float):
    """Clamps the given value, between the given minimum and maximum values.

    :param minimum: The result will never be lower than the minimum.
    :param maximum: The result will never be higher than the maximum.
    """
    return min(max(minimum, value), maximum)
