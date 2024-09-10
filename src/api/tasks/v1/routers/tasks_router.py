
from fastapi import APIRouter, Depends
from pydantic import UUID4
from src.api.tasks.v1.service import TasksService
from src.models import TaskModel
from src.schemas.task_schema import CreateTaskRequest, UpdateTaskRequest, TaskResponse, TaskListResponse


router = APIRouter(prefix="/tasks", tags=["Tasks work"])


@router.get("/get_task/{task_id}")
async def get_task(task_id: UUID4, service: TasksService = Depends(TasksService)) -> TaskResponse:
  """
  Get task by id
  """
  task: TaskModel | None = await service.get_task_by_id(task_id)
  return TaskResponse(payload=task)


@router.get("/get_tasks")
async def get_all_tasks(service: TasksService = Depends(TasksService)) -> TaskListResponse:
  """
  Get all tasks
  """
  tasks: list[TaskModel] | None = await service.get_all_tasks()
  return TaskListResponse(payload=tasks)


@router.post("/create_task")
async def create_task(task_data: CreateTaskRequest,
                      service: TasksService = Depends(TasksService)) -> TaskResponse:
  """
  Create task
  """
  created_task: TaskModel = await service.create_task(task_data.model_dump())
  return TaskResponse(payload=created_task)



@router.put("/update_task/{task_id}")
async def update_task(task_id: UUID4, task_data: UpdateTaskRequest,
                      service: TasksService = Depends(TasksService)) -> TaskResponse:
  """
  Update task by id
  """
  updated_task: TaskModel = await service.update_task(task_id, task_data.model_dump())
  return TaskResponse(payload=updated_task)


@router.delete("/delete_task/{task_id}")
async def delete_task(task_id: UUID4, service: TasksService = Depends(TasksService)) -> dict[str, int | str]:
  """
  Delete task by id
  """
  await service.delete_task(task_id)
  return {"status_code": 200, "detail": "The task success delete"}


@router.delete("/delete_tasks")
async def delete_all_tasks(service: TasksService = Depends(TasksService)) -> dict[str, int | str]:
  """
  Delete all tasks
  """
  await service.delete_all_tasks()
  return {"status_code": 200, "detail": "The all tasks success delete"}