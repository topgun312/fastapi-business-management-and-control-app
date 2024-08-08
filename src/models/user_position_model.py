from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import User, PositionModel


class UserPositionModel(BaseModel):
    __tablename__ = "user_position_table"

    id: Mapped[uuid_pk]
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"), nullable=False
    )
    position_id: Mapped[uuid4] = mapped_column(
        ForeignKey("position_table.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="user_position")
    position: Mapped["PositionModel"] = relationship(back_populates="user_position")

    __table_args__ = (UniqueConstraint("user_id"), UniqueConstraint("position_id"))
