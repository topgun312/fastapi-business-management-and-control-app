from pydantic import BaseModel

from src.schemas.account_schema import AccountSchema


class BaseWrapper(BaseModel):
    status: int = 200
    error: bool = False


class CreatedAccountWrapper(BaseWrapper):
    status: int = 201
    payload: AccountSchema


class UpdatedAccountWrapper(BaseWrapper):
    payload: AccountSchema
