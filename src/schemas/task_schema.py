import datetime
from enum import Enum


from pydantic import UUID4, BaseModel, Field, model_validator
from typing_extensions import Self

from src.schemas.response import BaseResponse, BaseCreateResponse
from src.schemas.user_schema import UserId


class TaskStatus(str, Enum):
    IN_PROCESS = 'TASK IN PROCESS'
    FINISH = 'FINISH TASK'


class TaskId(BaseModel):
    id: UUID4


class CreateTaskRequest(BaseModel):
    title: str = Field(max_length=100)
    description: str
    author_id: UUID4
    responsible_id: UUID4
    observers: list[UserId] = Field(default_factory=list)
    performers: list[UserId] = Field(default_factory=list)
    deadline: str = Field(default='')
    status: TaskStatus
    time_estimate: int

    @model_validator(mode='after')
    def create_deadline(self) -> Self:
        today = datetime.datetime.utcnow()
        deadline_time = today + datetime.timedelta(hours=self.time_estimate)
        self.deadline = deadline_time.strftime('%Y-%m-%d %H:%M:%S')
        return self


class UpdateTaskRequest(CreateTaskRequest): ...


class TaskDB(TaskId, CreateTaskRequest): ...


class TaskResponse(BaseResponse):
    payload: TaskDB


class TaskListResponse(BaseResponse):
    payload: list[TaskDB]


class TaskCreateResponse(BaseCreateResponse):
    payload: TaskDB