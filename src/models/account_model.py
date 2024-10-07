from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import EmailType

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import uuid_pk
from src.schemas.account_schema import AccountDB

if TYPE_CHECKING:
    from models import CompanyModel, InviteModel, SecretModel, User


class AccountModel(BaseModel):
    __tablename__ = "account_table"

    id: Mapped[uuid_pk]
    email: Mapped[str] = mapped_column(EmailType, nullable=False, unique=True)
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"),
        nullable=True,
    )
    user: Mapped["User"] = relationship(back_populates="account", lazy="selectin")
    secret: Mapped["SecretModel"] = relationship(
        back_populates="account",
        cascade="all, delete",
        passive_deletes=True,
    )
    company: Mapped["CompanyModel"] = relationship(
        back_populates="director",
        passive_deletes=True,
    )
    invite: Mapped["InviteModel"] = relationship(
        back_populates="account",
        cascade="all, delete",
        passive_deletes=True,
    )
    __table_args__ = (UniqueConstraint("user_id"),)

    def to_pydantic_schema(self) -> AccountDB:
        return AccountDB(**self.__dict__)
