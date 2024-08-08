import datetime

from pydantic import BaseModel, UUID4, Field


class IdUserSchema(BaseModel):
    id: UUID4


class CreateUserSchema(BaseModel):
    email: str = Field(max_length=100)
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    is_active: bool = Field(default=False)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)


class UpdateUserSchema(IdUserSchema, CreateUserSchema): ...


class UserSchema(IdUserSchema, CreateUserSchema):
    registered_at: datetime.datetime
    updated_at: datetime.datetime
