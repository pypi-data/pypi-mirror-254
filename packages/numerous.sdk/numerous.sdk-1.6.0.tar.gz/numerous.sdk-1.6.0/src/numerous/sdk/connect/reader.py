"""Functionality related to reading data and the :class:`Reader`."""

from collections import defaultdict
from typing import Generator, Optional, Union

from numerous.sdk.utils import PandasStub

try:
    import pandas
except ModuleNotFoundError:
    pandas = PandasStub()

from numerous.grpc import spm_pb2, spm_pb2_grpc

from numerous.sdk.connect.job_utils import JobIdentifier


class Reader:
    """The :class:`Reader` reads data from the server."""

    def __init__(
        self,
        spm_stub: spm_pb2_grpc.SPMStub,
        job_identity: JobIdentifier,
        execution_id: str,
    ):
        """Initialize the reader.

        :param spm_stub: The client.
        :param job_identity: The identity of the job, the :class:`Reader` is reading for.
        :param execution_id: The ID of the execution, the :class:`Reader` is reading for.
        """
        self._spm_stub = spm_stub
        self._job_identity = job_identity
        self._execution_id = execution_id

    def range(
        self, start: Optional[float], end: Optional[float]
    ) -> Generator[dict[str, list[float]], None, None]:
        """Reads a range of data and returns an iterable of data rows."""
        yield from self._data_stream(start or 0.0, end or 0.0)

    def data_frame(
        self, start: Optional[float], end: Optional[float]
    ) -> pandas.DataFrame:
        """Reads a range of data and returns a `pandas.DataFrame` with the data."""
        data = defaultdict(list)
        for data_list in self._data_stream(start or 0.0, end or 0.0):
            for key, values in data_list.items():
                data[key].extend(values)

        return pandas.DataFrame({k: v for k, v in data.items()})

    def _data_stream(
        self,
        start: float = 0.0,
        end: float = 0.0,
        tags: Union[list[str], None] = None,
        subscribe: bool = False,
    ) -> Generator[dict[str, list[float]], None, None]:
        time_range = False
        if start is not None and end is not None and start >= 0 and end > 0:
            time_range = True

        raw_data_stream = self._spm_stub.ReadData(
            spm_pb2.ReadScenario(
                project=self._job_identity.project_id,
                scenario=self._job_identity.scenario_id,
                execution=self._execution_id,
                tags=tags,
                start=start or 0.0,
                end=end or 0.0,
                time_range=time_range,
                listen=subscribe,
            )
        )

        for data_list in raw_data_stream:
            data: dict[str, list[float]] = defaultdict(list)
            for data_block in data_list.data:
                data[data_block.tag].extend(data_block.values)
            yield data
