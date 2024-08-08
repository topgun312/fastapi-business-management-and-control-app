from pydantic import UUID4, BaseModel, Field
import datetime


class IdInviteSchema(BaseModel):
    id: UUID4


class CreateInviteSchema(BaseModel):
    code: int = Field(max_digits=4)
    user_id: UUID4


class UpdateInviteSchema(IdInviteSchema, CreateInviteSchema): ...


class InviteSchema(IdInviteSchema, CreateInviteSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
