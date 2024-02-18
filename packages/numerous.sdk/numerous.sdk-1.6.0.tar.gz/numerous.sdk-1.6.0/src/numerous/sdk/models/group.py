from dataclasses import dataclass
from typing import Any

from numerous.grpc.spm_pb2_grpc import FileManagerStub

from .parameter import Parameter, get_parameters_dict


@dataclass
class Group:
    id: str
    name: str
    parameters: dict[str, Parameter]

    @staticmethod
    def from_document(
        data: dict[str, Any], file_manager_client: FileManagerStub, group_id
    ) -> "Group":
        return Group(
            id=group_id,
            name=data.get("groupName", ""),
            parameters=get_parameters_dict(
                data.get("parameters", []), file_manager_client=file_manager_client
            ),
        )
