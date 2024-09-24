from pydantic import UUID4, BaseModel, EmailStr

from src.schemas.response import BaseResponse, BaseCreateResponse


class AccountId(BaseModel):
    id: UUID4


class CreateAccountRequest(BaseModel):
    email: EmailStr


class UpdateAccountRequestByID(AccountId, CreateAccountRequest):
    user_id: UUID4 | None


class UpdateAccountRequestByEmail(CreateAccountRequest): ...


class AccountDB(UpdateAccountRequestByID): ...


class AccountResponse(BaseResponse):
    payload: AccountDB


class AccountListResponse(BaseResponse):
    payload: list[AccountDB]


class AccountCreateResponse(BaseCreateResponse):
    payload: AccountDB


class TestAccountSchema(BaseModel):
    id: UUID4
    email: EmailStr
    user_id: UUID4 | None
