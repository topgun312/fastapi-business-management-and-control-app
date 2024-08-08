from typing import List

from pydantic import BaseModel, UUID4, Field
from src.models import User


class IdTaskSchema(BaseModel):
    id: UUID4


class CreateTaskSchema(BaseModel):
    title: str = Field(max_length=100)
    description: str
    author_id: UUID4
    responsible_id: UUID4
    observers: List[User] = Field(default=[])
    performers: List[User] = Field(default=[])
    status: bool = Field(default=False)
    time_estimate: str


class UpdateTaskSchema(IdTaskSchema, CreateTaskSchema): ...


class TaskSchema(IdTaskSchema, CreateTaskSchema): ...
