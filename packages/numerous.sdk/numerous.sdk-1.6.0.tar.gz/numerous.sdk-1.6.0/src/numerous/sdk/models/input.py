from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Optional, Union


class InputSourceType(Enum):
    SCENARIO = "scenario"
    DATASET = "dataset"


@dataclass
class InputSource:
    project_id: str
    scenario_id: str
    type: InputSourceType
    offset: float = 0.0

    def job_time_to_base_time(self, time: datetime) -> float:
        return time.timestamp() - self.offset


@dataclass
class InputVariableScenarioSource:
    source: InputSource
    tag: str
    value: Optional[float] = field(default=None, init=False)
    """Should only be set by `InputReader`"""


@dataclass
class InputVariableStaticSource:
    value: float


def get_input_sources_from_scenario_document(
    data: dict[str, Any]
) -> dict[str, InputSource]:
    input_sources: list[dict[str, Any]] = data.get("inputScenarios", [])
    return {
        input_source["scenarioID"]: InputSource(
            project_id=input_source["projectID"],
            scenario_id=input_source["scenarioID"],
            type=InputSourceType(input_source["type"]),
            offset=input_source.get("offset", 0.0),
        )
        for input_source in input_sources
    }


@dataclass
class InputVariable:
    uuid: str
    id: str
    path: list[str]
    display_name: str
    source: Union[InputVariableScenarioSource, InputVariableStaticSource]
    scale: float = 1.0
    offset: float = 0.0

    @property
    def key(self) -> str:
        return ".".join(self.path)

    @property
    def value(self) -> Optional[float]:
        return self.source.value
