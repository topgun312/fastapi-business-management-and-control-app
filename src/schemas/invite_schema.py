from pydantic import UUID4, BaseModel, Field

from src.schemas.response import BaseResponse, BaseCreateResponse


class InviteId(BaseModel):
    id: UUID4


class CreateInviteRequest(BaseModel):
    code: int = Field(max_length=4)
    user_id: UUID4


class InviteDB(InviteId, CreateInviteRequest): ...


class InviteResponse(BaseResponse):
    payload: InviteDB


class InviteListResponse(BaseResponse):
    payload: list[InviteDB]

class InviteCreateResponse(BaseCreateResponse):
    payload: InviteDB