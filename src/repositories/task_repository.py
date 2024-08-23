from src.models import TaskModel
from src.utils.repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = TaskModel
