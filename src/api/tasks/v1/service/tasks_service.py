from collections.abc import Sequence

from fastapi import HTTPException, status
from pydantic import UUID4

from src.models import TaskModel, User
from src.schemas.task_schema import TaskDB
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode


class TasksService(BaseService):

    @transaction_mode
    async def get_task_by_id(self, task_id: UUID4) -> TaskDB:
        """Get task by id"""
        task: TaskModel | None = await self.uow.task.get_by_query_one_or_none(
            id=task_id
        )
        self._check_task_exists(task)
        return self._correct_task_schema_answer(task=task)

    @transaction_mode
    async def get_all_tasks(self, **kwargs) -> Sequence[TaskDB]:
        """Get all tasks"""
        tasks: Sequence[TaskModel] = await self.uow.task.get_by_query_all(**kwargs)
        return [self._correct_task_schema_answer(task=task) for task in tasks]

    @transaction_mode
    async def create_task(self, task_data: dict) -> TaskDB:
        """Create task"""
        observers, performers = await self.add_observers_and_performers(task_data)
        task: TaskModel = await self.uow.task.add_one_and_get_obj(**task_data)
        task_with_users: TaskModel = await self.uow.task.add_users_to_task_and_get_obj(
            task=task, observers=observers, performers=performers
        )
        return self._correct_task_schema_answer(task=task_with_users)

    @transaction_mode
    async def update_task(self, task_id: UUID4, task_data: dict) -> TaskDB:
        """Update task by id"""
        observers, performers = await self.add_observers_and_performers(task_data)
        task: TaskModel | None = await self.uow.task.update_one_by_id(
            _id=task_id, **task_data
        )
        updated_task: TaskModel = await self.uow.task.update_users_to_task_and_get_obj(
            task=task, observers=observers, performers=performers
        )
        return self._correct_task_schema_answer(task=updated_task)

    @transaction_mode
    async def delete_task(self, task_id: UUID4) -> None:
        """Delete task by id"""
        task: TaskModel | None = await self.uow.task.get_by_query_one_or_none(
            id=task_id
        )
        self._check_task_exists(task)
        await self.uow.task.delete_by_query(id=task_id)

    async def add_observers_and_performers(
        self, task_data: dict
    ) -> tuple[Sequence, Sequence]:
        """Add observers and performers to a task"""
        observers = await self.uow.user.get_by_query_all_in_users_list(
            task_data.get("observers")
        )
        self._check_users_exists(observers)
        performers = await self.uow.user.get_by_query_all_in_users_list(
            task_data.get("performers")
        )
        self._check_users_exists(performers)
        del task_data["observers"]
        del task_data["performers"]
        return observers, performers

    def _correct_task_schema_answer(self, task: TaskModel) -> TaskDB:
        """Get correct answer with schema TaskDB"""
        return TaskDB(
            id=task.id,
            title=task.title,
            description=task.title,
            author_id=task.author_id,
            responsible_id=task.responsible_id,
            observers=[user.to_pydantic_schema() for user in task.observers],
            performers=[user.to_pydantic_schema() for user in task.performers],
            deadline=task.deadline,
            status=task.status,
            time_estimate=task.time_estimate,
        )

    @staticmethod
    def _check_task_exists(task: TaskModel | None) -> None:
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
            )

    @staticmethod
    def _check_users_exists(users: Sequence[User]) -> None:
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Users not found"
            )
