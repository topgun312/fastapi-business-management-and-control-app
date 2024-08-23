from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import User, CompanyModel


class MemberModel(BaseModel):
    __tablename__ = "member_table"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"), nullable=False
    )
    company_id: Mapped[uuid4] = mapped_column(
        ForeignKey("company_table.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="member")
    company: Mapped["CompanyModel"] = relationship(back_populates="member")

    __table_args__ = (UniqueConstraint("user_id"),)
