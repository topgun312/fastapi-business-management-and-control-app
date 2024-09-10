from uuid import uuid4

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.schemas.secret_schema import SecretDB
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import User, AccountModel


class SecretModel(BaseModel):
    __tablename__ = "secret_table"

    id: Mapped[uuid_pk]
    password: Mapped[bytes] = mapped_column(nullable=False)
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    user_id: Mapped[uuid4] = mapped_column(
        ForeignKey("user_table.id", ondelete="CASCADE"), nullable=False
    )
    account_id: Mapped[uuid4] = mapped_column(
        ForeignKey("account_table.id", ondelete="CASCADE"), nullable=False
    )
    user: Mapped["User"] = relationship(back_populates="secret")
    account: Mapped["AccountModel"] = relationship(back_populates="secret")

    __table_args__ = (
        UniqueConstraint("user_id"),
        UniqueConstraint("account_id"),
    )

    def to_pydantic_schema(self) -> SecretDB:
        return SecretDB(**self.__dict__)
