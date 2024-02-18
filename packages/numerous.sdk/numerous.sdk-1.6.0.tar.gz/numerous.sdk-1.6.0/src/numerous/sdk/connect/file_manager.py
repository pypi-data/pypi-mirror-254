import io
import mimetypes
import os
import tempfile
from typing import IO, Optional

import requests
from numerous.grpc.spm_pb2 import ScenarioFilePath
from numerous.grpc.spm_pb2_grpc import SPMStub


class FileManager:
    def __init__(self, spm_client: SPMStub, project_id: str, scenario_id: str):
        self._spm_client = spm_client
        self._project_id = project_id
        self._scenario_id = scenario_id

    def upload_bytes(
        self, file_name: str, content: bytes, content_type: Optional[str] = None
    ) -> None:
        """Uploads the given content with the given file name, as the content type if specified.

        :param file_name:
        :param content: The bytes file content.
        :param content_type: The file content media type.
        """
        buffer = io.BytesIO(content)
        self._upload(file_name, file_name, buffer, content_type)

    def upload_stream(
        self, file_name: str, stream: IO[bytes], content_type: Optional[str] = None
    ) -> None:
        """Uploads the content read from the given content stream.
        Uses the given file name, and content type, if specified.

        :param file_name:
        :param stream: The file content bytes stream.
        :param content_type: The file content media type.
        """
        self._upload(file_name, file_name, stream, content_type)

    def upload_text(self, file_name: str, content: str) -> None:
        """Uploads the content with the given file name, as plain text.

        :param file_name:
        :param content: The text file content.
        """
        buffer = io.BytesIO(content.encode("utf-8"))
        self._upload(file_name, file_name, buffer, "text/plain")

    def upload_path(self, path: str) -> None:
        """Uploads the file at the given path, inferring the content type.

        :param path:
        """
        with open(path, "rb") as f:
            self._upload(path, os.path.split(path)[-1], f)

    def _upload(
        self,
        path: str,
        file_id: str,
        data: IO[bytes],
        content_type: Optional[str] = None,
    ):
        if content_type is None:
            content_type = mimetypes.guess_type(path)[0] or "application/octet-stream"
        scenario_file_path = ScenarioFilePath(
            project=self._project_id,
            scenario=self._scenario_id,
            path=path,
            file_id=file_id,
            content_type=content_type,
        )
        upload_url = self._spm_client.GenerateScenarioUploadSignedURL(
            scenario_file_path
        )
        requests.post(
            upload_url.url,
            headers={"Content-Type": "multipart/related"},
            params={"name": path, "mimeType": content_type},
            data=data,
        )


class FileUploadContext:
    _chunk_size = 4096

    def __init__(self, file_manager: FileManager, file_name: str):
        """
        :param file_manager: A file manager which is used to upload the content.
        :param file_name: The output file name.
        """
        self._file_manager = file_manager
        self._file_name = file_name
        self._buffer: Optional[io.BytesIO] = None

    def __enter__(self):
        """Creates a buffer for the content to be uploaded."""
        self._buffer = tempfile.TemporaryFile(prefix="numerous_sdk")
        return self

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        """Executes actual content upload from a buffer."""
        if not self._buffer:
            raise RuntimeError("Buffer is not initialized")

        try:
            self._buffer.seek(0)
            self._file_manager.upload_stream(self._file_name, self._buffer)
        finally:
            self._buffer.close()

    def write(self, data: str):
        """Adds the content of a given string.

        :param data: The content.
        """
        if not self._buffer:
            raise RuntimeError("Buffer is not initialized")

        self._buffer.write(data.encode())

    def write_from_file(self, file_name: str):
        """Adds the content from a given file.

        :param file_name: the name of a file with the content.
        """
        if not self._buffer:
            raise RuntimeError("Buffer is not initialized")

        with open(file_name, "rb") as f:
            while buffer := f.read(self._chunk_size):
                self._buffer.write(buffer)
