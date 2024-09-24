from pydantic import UUID4, BaseModel

from src.schemas.response import BaseResponse, BaseCreateResponse


class StructAdmPositionId(BaseModel):
    id: UUID4


class CreateStructAdmPositionRequest(BaseModel):
    struct_adm_id: int
    position_id: int


class UpdateStructAdmPositionRequest(
    StructAdmPositionId, CreateStructAdmPositionRequest,
): ...


class StructAdmPositionDB(
    StructAdmPositionId, CreateStructAdmPositionRequest,
): ...


class StructAdmPositionResponse(BaseResponse):
    payload: StructAdmPositionDB


class StructAdmPositionListResponse(BaseResponse):
    payload: list[StructAdmPositionDB]


class StructAdmPositionCreateResponse(BaseCreateResponse):
    payload: StructAdmPositionDB


class TestStructAdmPositionSchema(BaseModel):
    id: UUID4
    struct_adm_id: int
    position_id: int