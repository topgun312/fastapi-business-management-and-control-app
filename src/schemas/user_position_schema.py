from pydantic import BaseModel, UUID4


class IdUserPositionSchema(BaseModel):
    id: UUID4


class CreateUserPositionSchema(BaseModel):
    user_id: UUID4
    position_id: UUID4


class UpdateUserPositionSchema(IdUserPositionSchema, CreateUserPositionSchema): ...


class UserPositionSchema(IdUserPositionSchema, CreateUserPositionSchema): ...
