import datetime

from pydantic import UUID4, BaseModel, EmailStr, Field

from src.schemas.account_schema import AccountDB
from src.schemas.member_schema import MemberDB
from src.schemas.response import BaseResponse, BaseCreateResponse


class UserId(BaseModel):
    id: UUID4


class UserBase(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)


class CreateUserRequest(UserBase): ...


class UpdateUserRequest(CreateUserRequest): ...


class UserDB(UserId, UserBase):
    registered_at: datetime.datetime
    updated_at: datetime.datetime
    account: AccountDB
    member: MemberDB


class UserAuthSchema(UserId):
    username: EmailStr
    password: bytes
    is_active: bool = True
    is_admin: bool = False


class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = 'Bearer'


class UserResponse(BaseResponse):
    payload: UserDB


class UserListResponse(BaseResponse):
    payload: list[UserDB]


class UserCreateResponse(BaseCreateResponse):
    payload: UserDB


class TestUserSchema(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    id: UUID4
    is_active: bool
    is_admin: bool

