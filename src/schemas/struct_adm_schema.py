from pydantic import BaseModel, UUID4, Field
from sqlalchemy_utils import LtreeType
import datetime


class IdStructAdmSchema(BaseModel):
    id: UUID4


class CreateStructAdmSchema(BaseModel):
    name: str = Field(max_length=50)
    path: LtreeType


class UpdateStructAdmSchema(IdStructAdmSchema, CreateStructAdmSchema): ...


class StructAdmSchema(IdStructAdmSchema, CreateStructAdmSchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
