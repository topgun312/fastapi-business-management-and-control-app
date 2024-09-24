from uuid import UUID
from src.schemas.task_schema import TestTaskSchema, TestObserversSchema, TestPerformersSchema


FAKE_TASKS: list[TestTaskSchema] = [
  TestTaskSchema(
        id=UUID('97fa13cb-d481-4772-b27d-954c1a217702'),
        title='Sell a Boing 777',
        description='Sell a Boing 777',
        author_id=UUID('fba99cad-8e39-4108-b692-ffe8ce3c5d70'),
        responsible_id=UUID('7a937595-1206-4dae-8934-56cf4f46e71e'),
        deadline='2024-09-16 21:03:48',
        status='TASK IN PROCESS',
        time_estimate=24,
  ),
]

FAKE_OBSERVERS_TASKS: list[TestObserversSchema] = [
      TestObserversSchema(
            tasks_id=UUID('97fa13cb-d481-4772-b27d-954c1a217702'),
            users_id=UUID('0982d535-c313-4832-8855-8189f47ce06d')
      )
]

FAKE_PERFORMERS_TASKS: list[TestPerformersSchema] = [
      TestPerformersSchema(
            tasks_id=UUID('97fa13cb-d481-4772-b27d-954c1a217702'),
            users_id=UUID('7a937595-1206-4dae-8934-56cf4f46e71e')
      )
]