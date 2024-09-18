from pydantic import UUID4, BaseModel, Field

from src.schemas.response import BaseResponse, BaseCreateResponse


class StructAdmId(BaseModel):
    id: int


class StructAdmRequest(BaseModel):
    name: str


class CreateStructAdmRequest(BaseModel):
    name: str = Field(max_length=50)
    parent: str


class UpdateStructAdmRequest(StructAdmId, StructAdmRequest): ...


class UpdateStructAdmRequestByName(StructAdmRequest): ...


class StructAdmDB(StructAdmId, StructAdmRequest):
    company_id: UUID4
    head_user_id: UUID4 | None
    path: str


class StructAdmResponse(BaseResponse):
    payload: StructAdmDB


class StructAdmListResponse(BaseResponse):
    payload: list[StructAdmDB]


class StructAdmCreateResponse(BaseCreateResponse):
    payload: StructAdmDB