import datetime
from pydantic import BaseModel, UUID4


class IdSecretSchema(BaseModel):
    id: UUID4


class CreateSecretSchema(BaseModel):
    password: str
    user_id: UUID4
    account_id: UUID4


class UpdateSecretSchema(IdSecretSchema, CreateSecretSchema): ...


class SecretSchema(IdSecretSchema, CreateSecretSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
