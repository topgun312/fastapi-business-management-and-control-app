import datetime

from pydantic import BaseModel, UUID4


class IdMemberSchema(BaseModel):
    id: UUID4


class CreateMemberSchema(BaseModel):
    user_id: UUID4
    company_id: UUID4


class UpdateMemberSchema(IdMemberSchema, CreateMemberSchema): ...


class MemberSchema(IdMemberSchema, CreateMemberSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
