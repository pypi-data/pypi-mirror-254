import json
import signal
from datetime import datetime
from typing import Any, Callable, Optional

from numerous.grpc import spm_pb2, spm_pb2_grpc

from numerous.client_common.grpc_retry import grpc_retry_unary
from numerous.sdk.connect.job_state import JobState
from numerous.sdk.connect.job_utils import JobIdentifier


class HibernationHandler:
    def __init__(
        self,
        spm_client: spm_pb2_grpc.SPMStub,
        identity: JobIdentifier,
        execution_id: str,
        job_time_getter: Callable[[], Optional[datetime]],
        state_getter: Callable[[], JobState],
    ) -> None:
        self._spm_client = spm_client
        self._job_time_getter = job_time_getter
        self._identity = identity
        self._execution_id = execution_id
        self._state_getter = state_getter
        self.last_hibernate_time = self._load_last_hibernate_time()
        self.hibernating = False
        self.callback: Optional[Callable[[], Any]] = None

    def hibernate(self) -> None:
        self.hibernating = True
        if self.callback is not None:
            self.callback()
        self._state_getter().commit()
        self._store_last_hibernate_time()
        signal.raise_signal(signal.SIGTERM)

    @grpc_retry_unary()
    def _store_last_hibernate_time(self) -> None:
        job_time = self._job_time_getter()

        if job_time is None:
            return

        self._spm_client.SetScenarioCustomMetaData(
            request=spm_pb2.ScenarioCustomMetaData(
                project=self._identity.project_id,
                scenario=self._identity.scenario_id,
                execution=self._execution_id,
                key=f"{self._identity.job_id}.last_hibernate_job_time",
                meta=json.dumps(job_time.isoformat()),
            )
        )

    @grpc_retry_unary()
    def _load_last_hibernate_time(self) -> Optional[datetime]:
        last_hibernate_time = self._spm_client.GetScenarioCustomMetaData(
            request=spm_pb2.ScenarioCustomMetaData(
                project=self._identity.project_id,
                scenario=self._identity.scenario_id,
                execution=self._execution_id,
                key=f"{self._identity.job_id}.last_hibernate_job_time",
            )
        ).meta

        if not last_hibernate_time:
            return None

        try:
            return datetime.fromisoformat(json.loads(last_hibernate_time))
        except (ValueError, TypeError, json.decoder.JSONDecodeError):
            return None
