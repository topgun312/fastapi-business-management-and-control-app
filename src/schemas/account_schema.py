import datetime
from pydantic import BaseModel, UUID4, EmailStr

from src.schemas.response import BaseResponse


class AccountId(BaseModel):
    id: UUID4


class CreateAccountRequest(BaseModel):
    email: EmailStr


class UpdateAccountRequestByID(AccountId, CreateAccountRequest):
    user_id: UUID4


class UpdateAccountRequestByEmail(CreateAccountRequest): ...


class AccountDB(AccountId, CreateAccountRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class AccountResponse(BaseResponse):
    payload: AccountDB


class AccountListResponse(BaseResponse):
    payload: list[AccountDB]