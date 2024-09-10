import datetime
from pydantic import BaseModel, UUID4

from src.schemas.response import BaseResponse


class SecretId(BaseModel):
    id: UUID4


class CreateSecretRequest(BaseModel):
    password: str


class UpdateSecretRequest(SecretId, CreateSecretRequest): ...


class SecretDB(SecretId, CreateSecretRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class SecretResponse(BaseResponse):
    payload: SecretDB


class SecretListResponse(BaseResponse):
    payload: list[SecretDB]
