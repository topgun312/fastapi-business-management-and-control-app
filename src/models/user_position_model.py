from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import uuid_pk
from src.schemas.user_position_schema import UserPositionDB

if TYPE_CHECKING:
    from src.models import PositionModel, User


class UserPositionModel(BaseModel):
    __tablename__ = "user_position_table"

    id: Mapped[uuid_pk]
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    position_id: Mapped[int] = mapped_column(
        ForeignKey("position_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(back_populates="user_position")
    position: Mapped["PositionModel"] = relationship(back_populates="user_position")

    def to_pydantic_schema(self) -> UserPositionDB:
        return UserPositionDB(**self.__dict__)
