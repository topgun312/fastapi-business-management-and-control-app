from pydantic import UUID4, BaseModel

from src.schemas.response import BaseResponse, BaseCreateResponse


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