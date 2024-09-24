from pydantic import UUID4, BaseModel

from src.schemas.response import BaseResponse, BaseCreateResponse


class UserPositionId(BaseModel):
    id: UUID4


class CreateUserPositionRequest(BaseModel):
    user_id: list[UUID4]
    position_id: int


class UpdateUserPositionRequest(UserPositionId, CreateUserPositionRequest): ...


class UserPositionDB(UserPositionId):
    user_id: UUID4
    position_id: int


class UserPositionResponse(BaseResponse):
    payload: UserPositionDB


class UserPositionListResponse(BaseResponse):
    payload: list[UserPositionDB]


class UserPositionCreateResponse(BaseCreateResponse):
    payload: UserPositionDB


class TestUserPositionSchema(BaseModel):
    id: UUID4
    user_id: list[UUID4]
    position_id: int