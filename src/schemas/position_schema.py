from pydantic import BaseModel, Field

from src.schemas.response import BaseResponse, BaseCreateResponse


class PositionId(BaseModel):
    id: int


class CreatePositionRequest(BaseModel):
    name: str = Field(max_length=50)
    description: str | None


class UpdatePositionRequest(PositionId, CreatePositionRequest): ...


class UpdatePositionRequestByName(CreatePositionRequest): ...


class PositionDB(PositionId, CreatePositionRequest): ...


class PositionResponse(BaseResponse):
    payload: PositionDB


class PositionListResponse(BaseResponse):
    payload: list[PositionDB]


class PositionCreateResponse(BaseCreateResponse):
    payload: PositionDB


class TestPositionSchema(BaseModel):
    id: int
    name: str = Field(max_length=50)
    description: str | None