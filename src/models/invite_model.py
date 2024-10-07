from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import uuid_pk
from src.schemas.invite_schema import InviteDB

if TYPE_CHECKING:
    from src.models import AccountModel


class InviteModel(BaseModel):
    __tablename__ = "invite_table"

    id: Mapped[uuid_pk]
    code: Mapped[int] = mapped_column(nullable=False)
    account_id: Mapped[uuid4] = mapped_column(
        ForeignKey("account_table.id", ondelete="CASCADE"),
    )
    account: Mapped["AccountModel"] = relationship(back_populates="invite")

    def to_pydantic_schema(self) -> InviteDB:
        return InviteDB(**self.__dict__)
