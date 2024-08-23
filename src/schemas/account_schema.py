import datetime
from pydantic import BaseModel, UUID4, EmailStr


class IdAccountSchema(BaseModel):
    id: UUID4


class CreateAccountSchema(BaseModel):
    email: EmailStr


class UpdateAccountSchemabyID(IdAccountSchema, CreateAccountSchema):
    user_id: UUID4


class UpdateAccountSchemabyEmail(BaseModel):
    email: EmailStr


class AccountSchema(IdAccountSchema, CreateAccountSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
