from pydantic import BaseModel, UUID4, Field, ConfigDict
from sqlalchemy_utils import LtreeType
import datetime

from src.schemas.response import BaseResponse


class StructAdmId(BaseModel):
    id: UUID4


class CreateStructAdmRequest(BaseModel):
    name: str = Field(max_length=50)
    path: LtreeType

    model_config = ConfigDict(arbitrary_types_allowed=True)


class UpdateStructAdmRequest(StructAdmId, CreateStructAdmRequest): ...


class StructAdmDB(StructAdmId, CreateStructAdmRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class StructAdmResponse(BaseResponse):
    payload: StructAdmDB


class StructAdmListResponse(BaseResponse):
    payload: list[StructAdmDB]
