from pydantic import UUID4, BaseModel

from src.schemas.response import BaseResponse, BaseCreateResponse


class MemberId(BaseModel):
    id: UUID4


class CreateMemberRequest(BaseModel):
    user_id: UUID4
    company_id: UUID4


class UpdateMemberRequest(MemberId, CreateMemberRequest): ...


class MemberDB(MemberId, CreateMemberRequest): ...


class MemberResponse(BaseResponse):
    payload: MemberDB


class MemberListResponse(BaseResponse):
    payload: list[MemberDB]


class MemberCreateResponse(BaseCreateResponse):
    payload: MemberDB


class TestMemberSchema(BaseModel):
    id: UUID4
    user_id: UUID4
    company_id: UUID4
