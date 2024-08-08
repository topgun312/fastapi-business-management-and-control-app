from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import UserPositionModel, StructAdmPositionModel


class PositionModel(BaseModel):
    __tablename__ = "position_table"

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str]
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    user_position: Mapped["UserPositionModel"] = relationship(
        back_populates="position", cascade="all, delete", passive_deletes=True
    )
    struct_adm_position: Mapped["StructAdmPositionModel"] = relationship(
        back_populates="position", cascade="all, delete", passive_deletes=True
    )
