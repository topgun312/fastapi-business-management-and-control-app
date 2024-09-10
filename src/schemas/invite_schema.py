from pydantic import UUID4, BaseModel, Field
import datetime

from src.schemas.response import BaseResponse


class InviteId(BaseModel):
    id: UUID4


class CreateInviteRequest(BaseModel):
    code: int = Field(max_length=4)
    user_id: UUID4


class UpdateInviteRequest(InviteId, CreateInviteRequest): ...


class InviteDB(InviteId, CreateInviteRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class InviteResponse(BaseResponse):
    payload: InviteDB


class InviteListResponse(BaseResponse):
    payload: list[InviteDB]