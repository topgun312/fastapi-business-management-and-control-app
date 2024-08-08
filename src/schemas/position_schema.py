import datetime

from pydantic import BaseModel, UUID4, Field


class IdPositionSchema(BaseModel):
    id: UUID4


class CreatePositionSchema(BaseModel):
    name: str = Field(max_length=50)
    description: str | None


class UpdatePositionSchema(IdPositionSchema, CreatePositionSchema): ...


class PositionSchema(IdPositionSchema, CreatePositionSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
