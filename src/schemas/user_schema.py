import datetime

from pydantic import BaseModel, UUID4, Field, ConfigDict
from src.models import AccountModel


class IdUserSchema(BaseModel):
    id: UUID4


class UserBase(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)


class CreateUserSchema(UserBase): ...


class UpdateUserSchema(CreateUserSchema): ...


class UserSchema(IdUserSchema, UserBase):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    username: AccountModel.email
    email: AccountModel.email
    registered_at: datetime.datetime
    updated_at: datetime.datetime


class UserAuthSchema(BaseModel):
    username: str
    email: str
    password: bytes
    active: bool = True
