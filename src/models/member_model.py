from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import uuid_pk
from src.schemas.member_schema import MemberDB

if TYPE_CHECKING:
    from src.models import CompanyModel, User


class MemberModel(BaseModel):
    __tablename__ = "member_table"

    id: Mapped[uuid_pk]
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    company_id: Mapped[uuid4] = mapped_column(
        ForeignKey("company_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(back_populates="member")
    company: Mapped["CompanyModel"] = relationship(back_populates="member")

    __table_args__ = (UniqueConstraint("user_id"),)

    def to_pydantic_schema(self) -> MemberDB:
        return MemberDB(**self.__dict__)
