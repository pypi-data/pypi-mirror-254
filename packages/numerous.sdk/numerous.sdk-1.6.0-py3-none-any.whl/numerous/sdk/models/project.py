from dataclasses import dataclass
from typing import Any

from numerous.grpc.spm_pb2_grpc import FileManagerStub

from .parameter import Parameter, get_parameters_dict


@dataclass
class Project:
    id: str
    name: str
    parameters: dict[str, Parameter]

    @staticmethod
    def from_document(
        data: dict[str, Any], file_manager_client: FileManagerStub
    ) -> "Project":
        return Project(
            id=data["id"],
            name=data["projectName"],
            parameters=get_parameters_dict(
                data.get("parameters", []), file_manager_client
            ),
        )
