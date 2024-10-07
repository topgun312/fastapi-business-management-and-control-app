from fastapi import APIRouter, Depends, status
from fastapi_cache.decorator import cache
from pydantic import UUID4

from src.api.tasks.v1.service import TasksService
from src.api.users.v1.auth_utils.validate import (
    get_current_active_auth_user,
    get_current_admin_auth_user,
)
from src.schemas.task_schema import (
    CreateTaskRequest,
    TaskCreateResponse,
    TaskDB,
    TaskListResponse,
    TaskResponse,
    UpdateTaskRequest,
)
from src.schemas.user_schema import UserAuthSchema

router = APIRouter(prefix="/tasks", tags=["Tasks work"])


@router.get("/get_task/{task_id}", status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def get_task(
    task_id: UUID4,
    active_account: UserAuthSchema = Depends(get_current_active_auth_user),
    service: TasksService = Depends(TasksService),
) -> TaskResponse:
    """Get task by id"""
    if active_account:
        task: TaskDB | None = await service.get_task_by_id(task_id)
        return TaskResponse(payload=task)


@router.get("/get_tasks", status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def get_all_tasks(
    active_account: UserAuthSchema = Depends(get_current_active_auth_user),
    service: TasksService = Depends(TasksService),
) -> TaskListResponse:
    """Get all tasks"""
    if active_account:
        tasks: list[TaskDB] | None = await service.get_all_tasks()
        return TaskListResponse(payload=tasks)


@router.post("/create_task", status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: CreateTaskRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: TasksService = Depends(TasksService),
) -> TaskCreateResponse:
    """Create task"""
    if admin:
        created_task: TaskDB = await service.create_task(task_data.model_dump())
        return TaskCreateResponse(payload=created_task)


@router.put("/update_task/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(
    task_id: UUID4,
    task_data: UpdateTaskRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: TasksService = Depends(TasksService),
) -> TaskResponse:
    """Update task by id"""
    if admin:
        updated_task: TaskDB = await service.update_task(
            task_id, task_data.model_dump()
        )
        return TaskResponse(payload=updated_task)


@router.delete("/delete_task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID4,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: TasksService = Depends(TasksService),
) -> None:
    """Delete task by id"""
    if admin:
        await service.delete_task(task_id)
