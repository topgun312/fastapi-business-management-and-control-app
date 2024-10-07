from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    String,
    Table,
    UniqueConstraint,
    nulls_last,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import created_at_ct, updated_at_ct, uuid_pk
from src.schemas.task_schema import TaskDB, TaskStatus

if TYPE_CHECKING:
    from src.models import User


observers_table = Table(
    "observers_table",
    BaseModel.metadata,
    Column("tasks_id", ForeignKey("task_table.id", ondelete="CASCADE")),
    Column("users_id", ForeignKey("user_table.id", ondelete="SET NULL")),
)

performers_table = Table(
    "performers_table",
    BaseModel.metadata,
    Column("tasks_id", ForeignKey("task_table.id", ondelete="CASCADE")),
    Column("users_id", ForeignKey("user_table.id", ondelete="SET NULL")),
)


class TaskModel(BaseModel):
    __tablename__ = "task_table"

    id: Mapped[uuid_pk]
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="SET NULL"),
        nullable=True,
    )
    responsible_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="SET NULL"),
        nullable=True,
    )
    observers: Mapped[list["User"]] = relationship(
        secondary=observers_table, lazy="selectin"
    )
    performers: Mapped[list["User"]] = relationship(
        secondary=performers_table, lazy="selectin"
    )
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    deadline: Mapped[str]
    status: Mapped[Enum] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.IN_PROCESS
    )
    time_estimate: Mapped[int]
    author_user: Mapped["User"] = relationship(
        back_populates="author",
        foreign_keys="TaskModel.author_id",
    )
    responsible_user: Mapped["User"] = relationship(
        back_populates="responsible",
        foreign_keys="TaskModel.responsible_id",
    )

    __table_args__ = (UniqueConstraint("responsible_id"),)

    def to_pydantic_schema(self) -> TaskDB:
        return TaskDB(**self.__dict__)
