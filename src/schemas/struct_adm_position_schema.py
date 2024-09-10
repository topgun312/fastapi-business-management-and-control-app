from pydantic import BaseModel, UUID4

from src.schemas.response import BaseResponse


class StructAdmPositionId(BaseModel):
    id: UUID4


class CreateStructAdmPositionRequest(BaseModel):
    struct_adm_id: UUID4
    position_id: UUID4


class UpdateStructAdmPositionRequest(
    StructAdmPositionId, CreateStructAdmPositionRequest
): ...


class StructAdmPositionDB(
    StructAdmPositionId, CreateStructAdmPositionRequest
): ...


class StructAdmPositionResponse(BaseResponse):
    payload: StructAdmPositionDB


class StructAdmPositionListResponse(BaseResponse):
    payload: list[StructAdmPositionDB]