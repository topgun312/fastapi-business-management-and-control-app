from pydantic import UUID4, BaseModel, Field

from src.schemas.response import BaseCreateResponse, BaseResponse


class InviteId(BaseModel):
    id: UUID4


class InviteCode(BaseModel):
    code: int


class CreateInviteRequest(InviteCode):
    account_id: UUID4


class InviteDB(InviteId, CreateInviteRequest): ...


class InviteResponse(BaseResponse):
    payload: InviteDB


class InviteListResponse(BaseResponse):
    payload: list[InviteDB]


class InviteCreateResponse(BaseCreateResponse):
    payload: InviteDB


class TestInviteSchema(BaseModel):
    id: UUID4
    code: int
    account_id: UUID4
