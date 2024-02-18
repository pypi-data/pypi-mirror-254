import enum
import json
import logging
import urllib.request
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import timedelta
from typing import IO, Any, Generator, Optional, Union

from numerous.grpc.spm_pb2 import FilePath, FilePaths
from numerous.grpc.spm_pb2_grpc import FileManagerStub

logger = logging.getLogger(__name__)


@dataclass
class Parameter:  # will be used as a base-class later for implementing specific functionality
    id: str
    uuid: str
    display_name: str
    type: str
    value: Any

    @staticmethod
    def from_document(
        data: dict[str, Any], file_manager_client: FileManagerStub
    ) -> "Parameter":
        return Parameter(
            id=data["id"],
            uuid=data["uuid"],
            display_name=data["displayName"],
            type=data["type"],
            value=parse_value(data, file_manager_client=file_manager_client),
        )


@dataclass
class FileReference:
    """Represents the reference to a selected file, uploaded to the platform. Can be
    used to access that files content."""

    id: str
    path: str
    name: str
    file_manager_client: FileManagerStub
    _downloaded_filepath: Optional[str] = field(default=None, init=False)

    @staticmethod
    def from_document(
        data: dict[str, Any], file_manager_client: FileManagerStub
    ) -> "FileReference":
        return FileReference(
            data["id"],
            data["path"],
            data["name"],
            file_manager_client=file_manager_client,
        )

    def _get_file_url(self) -> str:
        return (
            self.file_manager_client.GetDownloadUrls(
                request=FilePaths(
                    file_paths=[FilePath(path=self.path, content_type="text/plain")]
                )
            )
            .urls[0]
            .url
        )

    @property
    def file_path(self) -> str:
        """The local path to the referenced file. The file will be downloaded on access."""
        return (
            self._downloaded_filepath if self._downloaded_filepath else self.download()
        )

    def download(self) -> str:
        """Download the referenced file, and get the resulting path.

        If the file has already been downloaded, the previously downloaded file is
        overridden."""
        try:
            url = self._get_file_url()
            filepath, _ = urllib.request.urlretrieve(url)  # nosec
            self._downloaded_filepath = filepath
            return filepath
        except Exception as e:
            logger.exception(f"Error while downloading file: {e}")
            raise

    @contextmanager
    def open_text(self) -> Generator[IO[str], None, None]:
        """Open the referenced file for reading text content."""
        with open(self.file_path, "r") as f:
            yield f

    def read_json(self) -> Union[dict, list]:
        """Read the JSON content of the referenced file."""
        with self.open_text() as f:
            return json.load(f)

    def read_text(self) -> str:
        """Read the text content of the referenced file."""
        with self.open_text() as f:
            return f.read()

    @contextmanager
    def open_bytes(self) -> Generator[IO[bytes], None, None]:
        """Open the referenced file for reading binary content."""
        with open(self.file_path, "rb") as f:
            yield f

    def read_bytes(self) -> bytes:
        """Read the bytes of the referenced file."""
        with self.open_bytes() as f:
            return f.read()


class SimTimeUnit(enum.Enum):
    years = "years"
    months = "months"
    days = "days"
    hours = "hours"
    minutes = "minutes"
    seconds = "seconds"

    @classmethod
    def from_string(cls, value_str) -> "SimTimeUnit":
        for member in cls:
            if member.value == value_str:
                return member
        raise ValueError(f"No matching enum member for value: {value_str}")


@dataclass
class Currency:
    name: str
    code: str

    @staticmethod
    def from_document(data: dict[str, Any]) -> "Currency":
        return Currency(data["name"], data["code"])


@dataclass
class Month:
    value: int

    @staticmethod
    def from_document(data: dict[str, Any]) -> "Month":
        return Month(data["value"])


@dataclass
class MapLocation:
    id: str
    name: str
    center: tuple[float, float]

    @staticmethod
    def from_document(data: dict[str, Any]) -> "MapLocation":
        return MapLocation(data["id"], data["name"], data["center"])


@dataclass
class TimeValue:
    total_seconds: float
    unit: SimTimeUnit
    delta: timedelta

    @staticmethod
    def from_document(data: dict[str, Any]) -> "TimeValue":
        return TimeValue(
            float(data["value"]),
            SimTimeUnit.from_string(data["unit"]),
            timedelta(seconds=float(data["value"])),
        )


@dataclass
class Config:
    value: str

    @staticmethod
    def from_document(data: dict[str, Any]) -> "Config":
        return Config(data["value"])


@dataclass
class Selection:
    id: str
    value: Union[str, float, int]

    @staticmethod
    def from_document(data: dict[str, Any]) -> "Selection":
        return Selection(data["tag"], data["value"])


def parse_value(data: dict[str, Any], file_manager_client: FileManagerStub) -> Any:
    value = data["value"]
    type_ = data["type"]
    if type_ == "string":
        return value
    elif type_ == "number":
        return float(value)
    elif type_ == "boolean":
        return value
    elif type_ == "file":
        return FileReference.from_document(value, file_manager_client)
    elif type_ == "json":
        return json.loads(value)
    elif type_ == "time_value":
        return TimeValue.from_document(value)
    elif type_ == "currency":
        return Currency.from_document(value)
    elif type_ == "month":
        return Month.from_document(value)
    elif type_ == "map":
        return MapLocation.from_document(value)
    elif type_ == "config":
        return Config.from_document(value)
    elif type_ == "selecter":
        return Selection.from_document(data)
    raise ValueError(f"Unkwnown parameter type: {type_}")


def get_parameters_dict(
    data: list[dict[str, Any]], file_manager_client: FileManagerStub
) -> dict[str, Parameter]:
    return {
        param.id: param
        for param in get_parameters_list(data, file_manager_client=file_manager_client)
    }


def get_parameters_list(
    data: list[dict[str, Any]], file_manager_client: FileManagerStub
) -> list[Parameter]:
    return [Parameter.from_document(param, file_manager_client) for param in data]
