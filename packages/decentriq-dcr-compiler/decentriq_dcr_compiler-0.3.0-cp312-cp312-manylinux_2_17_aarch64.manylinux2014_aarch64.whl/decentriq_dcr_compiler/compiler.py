from dataclasses import dataclass
from typing import List
from enum import Enum

from . import _ddc_py  # type: ignore
from .schemas.data_science_commit import DataScienceCommitItem
from .schemas.data_science_data_room import DataScienceDataRoomItem
from .schemas.lookalike_media_request import LookalikeMediaRequest
from .schemas.lookalike_media_response import LookalikeMediaResponse
from .schemas.requirement_list import RequirementList
from .schemas.data_lab import DataLab, EnclaveSpecification
from .schemas.create_data_lab import CreateDataLab
from .schemas.lookalike_media_data_room import LookalikeMediaDataRoom
from .schemas.create_lookalike_media_data_room import CreateLookalikeMediaDataRoom


@dataclass
class DataScienceDataRoomCompileOutput:
    data_room: bytes
    commits: List[bytes]
    datascience_data_room_encoded: bytes
    compile_context: _ddc_py.PyCommitCompileContext


def compile_data_science_data_room(
    input: DataScienceDataRoomItem,
) -> DataScienceDataRoomCompileOutput:
    compile_output = _ddc_py.compile_data_science_data_room(input.json())
    return DataScienceDataRoomCompileOutput(
        data_room=bytes(compile_output.data_room),
        commits=[bytes(commit) for commit in compile_output.commits],
        datascience_data_room_encoded=bytes(compile_output.high_level),
        compile_context=compile_output.commit_context,
    )


def verify_data_room(
    data_room: bytes, commits: List[bytes], high_level: bytes
) -> DataScienceDataRoomItem:
    result = _ddc_py.verify_data_room(data_room, commits, high_level)
    parsed = DataScienceDataRoomItem.parse_raw(result)
    return parsed


@dataclass
class DataScienceCommitCompileOutput:
    commit: bytes
    datascience_commit_encoded: bytes
    compile_context: _ddc_py.PyCommitCompileContext


def compile_data_science_commit(
    input: DataScienceCommitItem,
    context: _ddc_py.PyCommitCompileContext,
) -> DataScienceCommitCompileOutput:
    compile_output = _ddc_py.compile_data_science_commit(input.json(), context)
    return DataScienceCommitCompileOutput(
        commit=compile_output.commit,
        datascience_commit_encoded=compile_output.high_level,
        compile_context=compile_output.commit_context,
    )


def verify_configuration_commit(
    low_level: bytes,
    high_level: bytes,
    context: _ddc_py.PyCommitCompileContext,
) -> DataScienceCommitItem:
    result = _ddc_py.verify_configuration_commit(low_level, high_level, context)
    parsed = DataScienceCommitItem.parse_raw(result)
    return parsed


def compile_lookalike_media_request_serialized(
    input: LookalikeMediaRequest, user_auth_serialized: bytes
) -> bytes:
    return _ddc_py.compile_lookalike_media_request_serialized(
        input.json(), user_auth_serialized
    )


def decompile_lookalike_media_response(
    request: LookalikeMediaRequest,
    response_serialized: bytes,
) -> LookalikeMediaResponse:
    response = _ddc_py.decompile_lookalike_media_response_serialized(
        request.json(), response_serialized
    )
    parsed = LookalikeMediaResponse.parse_raw(response)
    return parsed


def compile_lookalike_media_data_room(
    input: LookalikeMediaDataRoom,
) -> bytes:
    return _ddc_py.compile_lookalike_media_data_room_serialized(input.json())


def compile_data_lab(
    input: DataLab,
) -> bytes:
    return _ddc_py.compile_data_lab_serialized(input.json())


class DataLabNode(Enum):
    Users = 1
    Segments = 2
    Demographics = 3
    Embeddings = 4
    Statistics = 5


def get_data_lab_node_id(input: DataLabNode) -> str:
    if input == DataLabNode.Users:
        node_type = _ddc_py.DataLabNode.Users
    elif input == DataLabNode.Segments:
        node_type = _ddc_py.DataLabNode.Segments
    elif input == DataLabNode.Demographics:
        node_type = _ddc_py.DataLabNode.Demographics
    elif input == DataLabNode.Embeddings:
        node_type = _ddc_py.DataLabNode.Embeddings
    elif input == DataLabNode.Statistics:
        node_type = _ddc_py.DataLabNode.Statistics
    return _ddc_py.get_data_lab_node_id(node_type)


def get_data_lab_validation_node_id(input: DataLabNode) -> str:
    if input == DataLabNode.Users:
        node_type = _ddc_py.DataLabNode.Users
    elif input == DataLabNode.Segments:
        node_type = _ddc_py.DataLabNode.Segments
    elif input == DataLabNode.Demographics:
        node_type = _ddc_py.DataLabNode.Demographics
    elif input == DataLabNode.Embeddings:
        node_type = _ddc_py.DataLabNode.Embeddings
    elif input == DataLabNode.Statistics:
        node_type = _ddc_py.DataLabNode.Statistics
    return _ddc_py.get_data_lab_validation_node_id(node_type)


def create_data_lab(
    input: CreateDataLab,
) -> DataLab:
    response = _ddc_py.create_data_lab_serialized(input.json())
    data_lab = DataLab.parse_raw(response)
    return data_lab


def create_lookalike_media_data_room(
    input: CreateLookalikeMediaDataRoom,
) -> LookalikeMediaDataRoom:
    response = _ddc_py.create_lookalike_media_data_room_serialized(input.json())
    return LookalikeMediaDataRoom.parse_raw(response)


def is_data_lab_compatible_with_lookalike_media_data_room(
    data_lab: DataLab,
    lm_dcr: LookalikeMediaDataRoom,
) -> bool:
    return _ddc_py.is_data_lab_compatible_with_lookalike_media_dcr_serialized(
        data_lab.json(), lm_dcr.json()
    )


def get_consumed_datasets(lm_dcr: LookalikeMediaDataRoom) -> RequirementList:
    req_list_serialized = (
        _ddc_py.get_lookalike_media_data_room_consumed_datasets_serialized(
            lm_dcr.json()
        )
    )
    return RequirementList.parse_raw(req_list_serialized)


def update_data_lab_enclave_specifications(
    data_lab: DataLab,
    driver_spec: EnclaveSpecification,
    python_spec: EnclaveSpecification,
    root_certificate_pem: str,
) -> DataLab:
    result = _ddc_py.update_data_lab_enclave_specifications_serialized(
        data_lab.json(), driver_spec.json(), python_spec.json(), root_certificate_pem
    )
    return DataLab.parse_raw(result)


def get_data_lab_features(
    data_lab: DataLab,
) -> List[str]:
    return _ddc_py.get_data_lab_features_serialized(data_lab.json())


def get_lookalike_media_data_room_features(
    lm_dcr: LookalikeMediaDataRoom,
) -> List[str]:
    return _ddc_py.get_lookalike_media_data_room_features_serialized(lm_dcr.json())


def get_lookalike_media_node_names_from_data_lab_data_type(input: str) -> str:
    return _ddc_py.get_lookalike_media_node_names_from_data_lab_data_type(input)
