import datetime

from pydantic import BaseModel, UUID4

from src.schemas.response import BaseResponse


class MemberId(BaseModel):
    id: UUID4


class CreateMemberRequest(BaseModel):
    user_id: UUID4
    company_id: UUID4


class UpdateMemberRequest(MemberId, CreateMemberRequest): ...


class MemberDB(MemberId, CreateMemberRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class MemberResponse(BaseResponse):
    payload: MemberDB


class MemberListResponse(BaseResponse):
    payload: list[MemberDB]



