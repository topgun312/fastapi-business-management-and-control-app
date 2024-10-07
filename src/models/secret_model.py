from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import uuid_pk
from src.schemas.secret_schema import SecretDB

if TYPE_CHECKING:
    from src.models import AccountModel, User


class SecretModel(BaseModel):
    __tablename__ = "secret_table"

    id: Mapped[uuid_pk]
    password: Mapped[bytes] = mapped_column(nullable=False)
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    account_id: Mapped[uuid4] = mapped_column(
        ForeignKey("account_table.id", ondelete="CASCADE"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(back_populates="secret")
    account: Mapped["AccountModel"] = relationship(back_populates="secret")

    __table_args__ = (
        UniqueConstraint("user_id"),
        UniqueConstraint("account_id"),
    )

    def to_pydantic_schema(self) -> SecretDB:
        return SecretDB(**self.__dict__)
