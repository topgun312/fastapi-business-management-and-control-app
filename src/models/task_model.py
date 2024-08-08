import datetime
from typing import List

from sqlalchemy import String, ForeignKey, UUID, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from src.models import BaseModel, User
from src.models.mixins.custom_types import uuid_pk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import User


class TaskModel(BaseModel):
    __tablename__ = "task_table"

    id: Mapped[uuid_pk]
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    author_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="SET NULL"), nullable=True
    )
    responsible_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="SET NULL"), nullable=True
    )
    observers: Mapped[List["User"]] = mapped_column(ARRAY(UUID), default=[])
    performers: Mapped[List["User"]] = mapped_column(ARRAY(UUID), default=[])
    deadline: Mapped[datetime.datetime]
    status: Mapped[bool] = mapped_column(default=False)
    time_estimate: Mapped[str]
    author_user: Mapped["User"] = relationship(back_populates="author")
    responsible_user: Mapped["User"] = relationship(back_populates="responsible")

    __table_args__ = (UniqueConstraint("author_id"), UniqueConstraint("responsible_id"))
