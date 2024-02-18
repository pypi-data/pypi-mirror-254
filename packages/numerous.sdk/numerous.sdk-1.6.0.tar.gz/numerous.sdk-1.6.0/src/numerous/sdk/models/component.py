"""Components are the basic building blocks of systems.

This module contains the definition of Components, and the implementation of
functionality to create them.
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import Any

from numerous.grpc.spm_pb2_grpc import FileManagerStub

from numerous.sdk.models.input import (
    InputSource,
    InputVariable,
    InputVariableScenarioSource,
    InputVariableStaticSource,
)
from numerous.sdk.models.parameter import Parameter, get_parameters_dict


@dataclass
class SubComponentNotFound(Exception):
    """Raised when creating a :class:`Component` is configured with a subcomponent that
    does not exist.
    """

    component_uuid: str


@dataclass
class Component:
    """A component of a :class:`~numerous.sdk.models.scenario.Scenario`, containing
    parameters, input variables, and any subcomponents."""

    uuid: str
    id: str
    type: str
    name: str
    item_class: list[str]
    is_enabled: bool
    is_main: bool
    input_variables: dict[str, InputVariable]
    components: dict[str, list["Component"]]
    parameters: dict[str, Parameter]
    """The subcomponents of this component."""

    @staticmethod
    def from_document(
        path: list[str],
        component: dict[str, Any],
        all_components: list[dict[str, Any]],
        input_sources_mapping: dict[str, InputSource],
        file_manager_client: FileManagerStub,
    ) -> "Component":
        component_path = path + [component["name"]]
        return Component(
            uuid=component["uuid"],
            id=component["id"],
            type=component["type"],
            name=component["name"],
            is_enabled=not bool(component["disabled"]),
            is_main=bool(component["isMainComponent"]),
            components=_extract_subcomponents(
                component_path,
                component,
                all_components,
                input_sources_mapping,
                file_manager_client,
            ),
            item_class=component["item_class"].split("."),
            input_variables=_extract_input_variables(
                component_path, component, input_sources_mapping
            ),
            parameters=get_parameters_dict(
                component.get("parameters", []), file_manager_client
            ),
        )


def _extract_subcomponents(
    path: list[str],
    component: dict[str, Any],
    all_components: list[dict[str, Any]],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client: FileManagerStub,
) -> dict[str, list[Component]]:
    subcomponents = defaultdict(list)
    for subcomponent_ref in component.get("subcomponents", []):
        subcomponents[subcomponent_ref["name"]].append(
            _extract_subcomponent(
                path,
                subcomponent_ref["uuid"],
                all_components,
                input_sources_mapping,
                file_manager_client,
            )
        )
    return subcomponents


def _extract_subcomponent(
    path: list[str],
    subcomponent_uuid: str,
    all_components: list[dict[str, Any]],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client: FileManagerStub,
) -> Component:
    subcomponent = next(
        (
            subcomponent
            for subcomponent in all_components
            if subcomponent.get("uuid") == subcomponent_uuid
        ),
        None,
    )

    if subcomponent is None:
        raise SubComponentNotFound(component_uuid=subcomponent_uuid)

    return Component.from_document(
        path,
        subcomponent,
        all_components,
        input_sources_mapping=input_sources_mapping,
        file_manager_client=file_manager_client,
    )


def extract_components(
    data: dict[str, Any],
    input_sources_mapping: dict[str, InputSource],
    file_manager_client,
) -> dict[str, Component]:
    components = data.get("simComponents", [])
    subcomponent_uuids = _get_all_subcomponent_uuids(components)
    return {
        component["name"]: Component.from_document(
            [], component, components, input_sources_mapping, file_manager_client
        )
        for component in components
        if component["uuid"] not in subcomponent_uuids
    }


def _get_all_subcomponent_uuids(components: list[dict[str, Any]]) -> set[str]:
    all_subcomponent_uuids = set()

    for component in components:
        for subcomponent in component.get("subcomponents", []):
            all_subcomponent_uuids.add(subcomponent["uuid"])

    return all_subcomponent_uuids


def _extract_input_variable(
    path: list[str], data: dict[str, Any], input_sources_mapping: dict[str, InputSource]
) -> InputVariable:
    input_variable_path = path + [data["id"]]

    input_variable = InputVariable(
        id=data["id"],
        uuid=data["uuid"],
        path=input_variable_path,
        display_name=data["display"],
        source=_extract_input_variable_source(data, input_sources_mapping),
        scale=data["scaling"],
        offset=data["offset"],
    )
    return input_variable


def _extract_input_variable_source(
    input_variable: dict[str, Any], input_sources_mapping: dict[str, InputSource]
):
    data_source_type = input_variable["dataSourceType"]
    if data_source_type == "static":
        return InputVariableStaticSource(value=input_variable["value"])
    elif data_source_type in ["scenario", "control_machines"]:
        data_source_id = input_variable["dataSourceID"]
        tag_source = input_variable["tagSource"]
        input_source = input_sources_mapping[data_source_id]
        if (
            tag_source["projectID"] != input_source.project_id
            or tag_source["scenarioID"] != input_source.scenario_id
        ):
            raise ValueError("Tag source does not match selected input source")
        return InputVariableScenarioSource(input_source, tag=tag_source["tag"])
    else:
        raise ValueError(f"Invalid data source type: {data_source_type}")


def _extract_input_variables(
    path: list[str],
    component: dict[str, Any],
    input_sources_mapping: dict[str, InputSource],
) -> dict[str, InputVariable]:
    variables = component.get("inputVariables", [])
    variables_list: list[InputVariable] = [
        _extract_input_variable(path, variable, input_sources_mapping)
        for variable in variables
    ]
    return {variable.id: variable for variable in variables_list}
