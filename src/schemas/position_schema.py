import datetime

from pydantic import BaseModel, UUID4, Field

from src.schemas.response import BaseResponse


class PositionId(BaseModel):
    id: UUID4


class CreatePositionRequest(BaseModel):
    name: str = Field(max_length=50)
    description: str | None


class UpdatePositionRequest(PositionId, CreatePositionRequest): ...


class PositionDB(PositionId, CreatePositionRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class PositionResponse(BaseResponse):
    payload: PositionDB


class PositionListResponse(BaseResponse):
    payload: list[PositionDB]
