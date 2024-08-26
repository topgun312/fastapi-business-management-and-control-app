import datetime
from pydantic import BaseModel, UUID4


class IdSecretSchema(BaseModel):
    id: UUID4


class CreateSecretSchema(BaseModel):
    password: str


class UpdateSecretSchema(IdSecretSchema, CreateSecretSchema): ...


class SecretSchema(IdSecretSchema, CreateSecretSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
