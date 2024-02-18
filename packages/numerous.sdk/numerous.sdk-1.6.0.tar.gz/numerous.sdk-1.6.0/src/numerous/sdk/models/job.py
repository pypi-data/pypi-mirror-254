"""Jobs represent the things that run on the numerous platform,
including the context in which code using the SDK is running.

This module contains the definition of :class:`Job` and the implementation
of its instances' creation.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Optional

from numerous.grpc.spm_pb2_grpc import FileManagerStub

from numerous.sdk.connect.status_handler import StatusHandler
from numerous.sdk.models.job_time import JobTime
from numerous.sdk.models.parameter import Parameter, get_parameters_dict


@dataclass
class Job:
    """A job in a :class:`numerous.sdk.models.scenario.Scenario`"""

    id: str
    name: str
    is_main: bool
    parameters: dict[str, Parameter]
    time: JobTime

    @staticmethod
    def from_document(
        job_id: str,
        data: dict[str, Any],
        file_manager_client: FileManagerStub,
        status_handler: StatusHandler,
        last_hibernate_time: Optional[datetime] = None,
    ) -> "Job":
        return Job(
            id=job_id,
            name=data.get("name", ""),
            is_main=data.get("isMain", False),
            parameters=get_parameters_dict(
                data.get("image", {}).get("parameters", []), file_manager_client
            ),
            time=JobTime.from_document(data, last_hibernate_time, status_handler),
        )
