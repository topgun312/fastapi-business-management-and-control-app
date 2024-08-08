from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import StructAdmModel, PositionModel


class StructAdmPositionModel(BaseModel):
    __tablename__ = "struct_adm_position_table"

    id: Mapped[uuid_pk]
    struct_adm_id: Mapped[uuid4] = mapped_column(
        ForeignKey("struct_adm_table.id", ondelete="CASCADE"), nullable=False
    )
    position_id: Mapped[uuid4] = mapped_column(
        ForeignKey("position_table.id", ondelete="CASCADE"), nullable=False
    )
    struct_adm: Mapped["StructAdmModel"] = relationship(
        back_populates="struct_adm_position"
    )
    position: Mapped["PositionModel"] = relationship(
        back_populates="struct_adm_position"
    )

    __table_args__ = (UniqueConstraint("struct_adm_id"),)
