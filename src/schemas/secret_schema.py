from pydantic import UUID4, BaseModel

from src.schemas.response import BaseCreateResponse, BaseResponse


class SecretId(BaseModel):
    id: UUID4


class CreateSecretRequest(BaseModel):
    password: str


class UpdateSecretRequest(SecretId, CreateSecretRequest): ...


class SecretDB(SecretId, CreateSecretRequest): ...


class SecretResponse(BaseResponse):
    payload: SecretDB


class SecretListResponse(BaseResponse):
    payload: list[SecretDB]


class SecretCreateResponse(BaseCreateResponse):
    payload: SecretDB


class TestSecretSchema(BaseModel):
    id: UUID4
    password: bytes
    user_id: UUID4
    account_id: UUID4
