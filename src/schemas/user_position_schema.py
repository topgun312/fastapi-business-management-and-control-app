from pydantic import BaseModel, UUID4

from src.schemas.response import BaseResponse


class UserPositionId(BaseModel):
    id: UUID4


class CreateUserPositionRequest(BaseModel):
    user_id: UUID4
    position_id: UUID4


class UpdateUserPositionRequest(UserPositionId, CreateUserPositionRequest): ...


class UserPositionDB(UserPositionId, CreateUserPositionRequest): ...


class UserPositionResponse(BaseResponse):
    payload: UserPositionDB


class UserPositionListResponse(BaseResponse):
    payload: list[UserPositionDB]
