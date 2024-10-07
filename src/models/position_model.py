from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import integer_pk
from src.schemas.position_schema import PositionDB

if TYPE_CHECKING:
    from src.models import StructAdmPositionModel, UserPositionModel


class PositionModel(BaseModel):
    __tablename__ = "position_table"

    id: Mapped[integer_pk]
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[str]
    user_position: Mapped["UserPositionModel"] = relationship(
        back_populates="position",
        cascade="all, delete",
        passive_deletes=True,
    )
    struct_adm_position: Mapped[list["StructAdmPositionModel"]] = relationship(
        back_populates="position",
        cascade="all, delete",
        passive_deletes=True,
    )

    def to_pydantic_schema(self) -> PositionDB:
        return PositionDB(**self.__dict__)
