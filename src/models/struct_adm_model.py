from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey, Sequence, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import Ltree, LtreeType

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import integer_pk
from src.schemas.struct_adm_schema import StructAdmDB

if TYPE_CHECKING:
    from src.models import CompanyModel, StructAdmPositionModel, User


id_seq = Sequence("struct_adm_id_seq")


class StructAdmModel(BaseModel):
    __tablename__ = "struct_adm_table"

    id: Mapped[integer_pk]
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    path: Mapped[Ltree] = mapped_column(LtreeType, unique=True, nullable=False)
    company_id: Mapped[uuid4] = mapped_column(
        ForeignKey("company_table.id", ondelete="CASCADE"), nullable=False
    )
    head_user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="SET NULL"), nullable=True
    )
    company: Mapped["CompanyModel"] = relationship(back_populates="struct_adm")
    head_user: Mapped["User"] = relationship(back_populates="struct_adm")

    struct_adm_position: Mapped[list["StructAdmPositionModel"]] = relationship(
        back_populates="struct_adm",
        cascade="all, delete",
        passive_deletes=True,
    )

    __table_args__ = (UniqueConstraint("head_user_id"),)

    def to_pydantic_schema(self) -> StructAdmDB:
        return StructAdmDB(
            id=self.id,
            name=self.name,
            company_id=self.company_id,
            head_user_id=self.head_user_id,
            path=str(self.path),
        )
