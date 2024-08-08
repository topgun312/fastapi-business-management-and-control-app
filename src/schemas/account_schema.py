import datetime

from pydantic import BaseModel, UUID4, Field


class IdAccountSchema(BaseModel):
    id: UUID4


class CreateAccountSchema(BaseModel):
    email: str = Field(max_length=100)
    user_id: UUID4


class UpdateAccountSchema(IdAccountSchema, CreateAccountSchema): ...


class UserSchema(IdAccountSchema, CreateAccountSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
