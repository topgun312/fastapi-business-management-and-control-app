from pydantic.v1 import UUID4
from sqlalchemy import Result, update

from src.models import TaskModel
from src.utils.repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = TaskModel

    async def add_users_to_task_and_get_obj(
        self, task: TaskModel, **users
    ) -> TaskModel:
        task.observers.extend(users.get("observers"))
        task.performers.extend(users.get("performers"))
        await self.session.commit()
        return task

    async def update_users_to_task_and_get_obj(
        self, task: TaskModel, **users
    ) -> TaskModel:
        task.observers = users.get("observers")
        task.performers = users.get("performers")
        await self.session.commit()
        return task

    async def update_one_by_id(
        self, _id: int | str | UUID4, **task_data
    ) -> type(model) | None:
        query = (
            update(self.model)
            .filter(self.model.id == _id)
            .values(**task_data)
            .returning(self.model)
        )
        _obj: Result | None = await self.session.execute(query)
        return _obj.scalar_one_or_none()
