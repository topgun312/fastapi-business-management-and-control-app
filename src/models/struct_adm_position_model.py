from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import uuid_pk
from src.schemas.struct_adm_position_schema import StructAdmPositionDB

if TYPE_CHECKING:
    from src.models import PositionModel, StructAdmModel


class StructAdmPositionModel(BaseModel):
    __tablename__ = "struct_adm_position_table"

    id: Mapped[uuid_pk]
    struct_adm_id: Mapped[int] = mapped_column(
        ForeignKey("struct_adm_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    position_id: Mapped[int] = mapped_column(
        ForeignKey("position_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    struct_adm: Mapped["StructAdmModel"] = relationship(
        back_populates="struct_adm_position",
    )
    position: Mapped["PositionModel"] = relationship(
        back_populates="struct_adm_position",
    )

    def to_pydantic_schema(self) -> StructAdmPositionDB:
        return StructAdmPositionDB(**self.__dict__)
