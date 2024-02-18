"""Functionality related to writing data series and the :class:`Writer`."""


import sys
from collections import defaultdict
from datetime import datetime
from typing import Any, Callable, Generator, Iterable, Optional, Sequence, Union

from numerous.grpc import spm_pb2, spm_pb2_grpc

from numerous.sdk.connect.job_utils import JobIdentifier
from numerous.sdk.connect.request_response_stream import RequestResponseStream

FLOAT_SIZE = sys.getsizeof(float())


class TagsNotAllowed(Exception):
    """An error raised when written tags are invalid according to the data series."""

    def __init__(self, tags: Iterable[str]):
        """Initialize the error.

        :param tags: The unallowed tags which triggered the error.
        """
        self.tags = tags

    def __eq__(self, __o: object) -> bool:  # pragma: no cover
        return isinstance(__o, TagsNotAllowed) and __o.tags == self.tags


def _default_tag(name: str):
    return spm_pb2.Tag(
        name=name,
        type="double",
        scaling=1,
        offset=0,
    )


class Writer:
    """The :class:`Writer` enables writing rows and series to the server.
    It manages a buffer, which is automatically flushed when it is full.
    """

    def __init__(
        self,
        spm_stub: spm_pb2_grpc.SPMStub,
        job_identity: JobIdentifier,
        start_time: datetime,
        execution_id: str,
        max_size_bytes: int,
        flush_margin_bytes: int,
    ):
        """Initialize the writer.

        :param spm_stub: The client.
        :param job_identity: The identity of the job, the :class:`Writer` is writing for.
        :param execution_id: The ID of the execution, the :class:`Writer` is writing for.
        :param max_size_bytes: The maximum buffer size of the :class:`Writer` in bytes.
        :param flush_margin_bytes: The margin that is subtracted the
        :paramref:`max_size_bytes` to determine if flushing should be performed.
        """
        self._spm_stub = spm_stub
        self._job_identity = job_identity
        self._start_time = start_time
        self._execution_id = execution_id
        self._buffer_index: list[float] = []
        self._buffer: dict[str, list[float]] = defaultdict(list)
        self._max_size_bytes = max_size_bytes
        self._flush_margin_bytes = flush_margin_bytes
        self._size_bytes: int = 0
        write_data_stream: Callable[
            [Iterable[spm_pb2.WriteDataStreamRequest]],
            Generator[spm_pb2.WriteDataStreamResponse, None, None],
        ] = spm_stub.WriteDataStream  # type: ignore[assignment]
        self._stream = RequestResponseStream(write_data_stream)
        self._allowed_tags: Optional[set[str]] = None
        self._closed: bool = False

    def _get_allowed_tags(self) -> Optional[set[str]]:
        if self._allowed_tags is not None:
            return self._allowed_tags

        metadata = self._spm_stub.GetScenarioMetaData(
            spm_pb2.Scenario(
                project=self._job_identity.project_id,
                scenario=self._job_identity.scenario_id,
                execution=self._execution_id,
            )
        )
        if metadata.tags:
            self._allowed_tags = {tag.name for tag in metadata.tags}
            return self._allowed_tags
        else:
            return None

    def _get_unallowed_tags(
        self, data: dict[str, Any], tags: Iterable[str]
    ) -> set[str]:
        return set(data.keys()).difference(tags)

    def _header_size(self, tags: Iterable[str]) -> int:
        if self._size_bytes == 0:
            return sum(sys.getsizeof(tag) for tag in tags)
        else:
            return 0

    def _list_size(self, data: Sequence[Union[float, datetime]]) -> int:
        return FLOAT_SIZE * len(data)

    def _row_and_index_size(self, data: dict[str, float]) -> int:
        return FLOAT_SIZE + FLOAT_SIZE * len(data)

    def _series_size(
        self, index: Sequence[Union[datetime, float]], data: dict[str, list[float]]
    ) -> int:
        return self._list_size(index) + sum(
            (self._list_size(values) for values in data.values())
        )

    def _must_flush_before_adding(self, added_size_bytes: int) -> bool:
        return (
            added_size_bytes + self._size_bytes + self._flush_margin_bytes
            >= self._max_size_bytes
        )

    def _set_data_series_config(self, data: dict[str, Any]) -> None:
        self._allowed_tags = set(data.keys())
        self._spm_stub.SetScenarioMetaData(
            spm_pb2.ScenarioMetaData(
                offset=self._start_time.timestamp(),
                tags=[_default_tag(tag) for tag in data.keys()],
                project=self._job_identity.project_id,
                scenario=self._job_identity.scenario_id,
                execution=self._execution_id,
            )
        )

    def _check_data_series_config(self, data: dict[str, Any]):
        if (tags := self._get_allowed_tags()) is None:
            self._set_data_series_config(data)
        elif unallowed_tags := self._get_unallowed_tags(data, tags):
            raise TagsNotAllowed(unallowed_tags)

    def row(
        self, time: Union[float, datetime], data: dict[str, float], flush: bool = False
    ) -> None:
        """Write a row of data into the data series.

        Each row written to the :class:`Writer` must have same keys as previously
        written series or rows.

        :param time: The time, at which the data is indexed. If a `float` value, it is
            interpreted as an offset in seconds since the start time of the job,
            otherwise if it is a `datetime`, it is interpreted as the time within the
            job runtime.
        :param data: The row of data to write into the data stream.
        :param flush: If true, will flush the buffer of the writer upon writing.
        :raises TagsNotAllowed: If tags that have not been previously written, are
            written.

        Writing rows can be used alongside :meth:`numerous.sdk.JobClient.read_inputs`,
        which will also iterate over the jobs runtime:

            >>> for t, data in job_client.read_inputs(step=3600.0):
            ...     job_client.writer.row(t, {"output": data["input1"] * 2})

        The type of the time values does not *have* to be the same type for each call:

            >>> job_client.job_time.start
            datetime(2023, 6, 1, 12, 0 ,0)
            >>> job_client.writer.row(datetime(2023, 6, 1, 12, 0, 0), {"value": 1.0})
            >>> job_client.writer.row(3600.0, {"value": 2.0})
            >>> job_client.writer.row(datetime(2023, 6, 1, 14, 0, 0), {"value": 4.0})
        """
        self._check_data_series_config(data)

        size_bytes = self._header_size(data) + self._row_and_index_size(data)
        if self._must_flush_before_adding(size_bytes):
            self.flush()

        index = self._time_to_index(time)
        for tag, value in data.items():
            self._buffer[tag].append(value)
        self._buffer_index.append(index)
        self._size_bytes += size_bytes

        if flush:
            self.flush()

    def series(
        self,
        times: Sequence[Union[float, datetime]],
        data: dict[str, list[float]],
        flush: bool = False,
    ) -> None:
        """Write a series of data to the data stream.

        Each series written to the :class:`Writer` must have same keys as previously
        written series or rows.

        :param times: The time values of the series, like for :meth:`row`, they
            can be either offsets from the start time, or a point in time.
        :param data: The data series to write. The keys are validated against
            previously written keys.
        :param flush: If true, will flush the buffer of the writer upon writing.
        :raises TagsNotAllowed: If tags that have not been previously written, are
            written.
        """
        self._check_data_series_config(data)

        size_bytes = self._header_size(data) + self._series_size(times, data)
        if self._must_flush_before_adding(size_bytes):
            self.flush()

        for key, value in data.items():
            self._buffer[key].extend(value)
        for time in times:
            self._buffer_index.append(self._time_to_index(time))
        self._size_bytes += size_bytes

        if flush:
            self.flush()

    def _time_to_index(self, time: Union[float, datetime]) -> float:
        return (
            (time - self._start_time).total_seconds()
            if isinstance(time, datetime)
            else time
        )

    def flush(self) -> None:
        """Flushes the buffer of the writer."""
        self._stream.send(
            spm_pb2.WriteDataStreamRequest(
                scenario=self._job_identity.scenario_id,
                execution=self._execution_id,
                overwrite=False,
                index=self._buffer_index,
                data={
                    tag: spm_pb2.StreamData(values=values)
                    for tag, values in self._buffer.items()
                },
                update_stats=True,
            )
        )
        self._buffer_index.clear()
        self._buffer.clear()
        self._size_bytes = 0

    def close(self, hibernating: bool):
        """Close the :class:`Writer`, flushing the buffer."""
        if not self._closed:
            self.flush()
            self._stream.close()
            self._spm_stub.CloseData(
                spm_pb2.DataCompleted(
                    scenario=self._job_identity.scenario_id,
                    execution=self._execution_id,
                    finalized=not hibernating,
                )
            )
            self._closed = True
