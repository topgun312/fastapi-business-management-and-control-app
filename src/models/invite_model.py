from uuid import uuid4


from src.models import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.mixins.custom_types import uuid_pk, created_at_ct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import AccountModel


# class InviteModel(BaseModel):
#     __tablename__ = "invite_table"
#
#     id: Mapped[uuid_pk]
#     code: Mapped[int] = mapped_column(nullable=False)
#     created_at: Mapped[created_at_ct]
#     user_id: Mapped[uuid4] = mapped_column(
#         ForeignKey("user_table.id", ondelete="CASCADE")
#     )
#     user: Mapped["User"] = relationship(back_populates="invite")


class InviteModel(BaseModel):
    __tablename__ = "invite_table"

    id: Mapped[uuid_pk]
    code: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[created_at_ct]
    account_id: Mapped[uuid4] = mapped_column(
        ForeignKey("account_table.id", ondelete="CASCADE")
    )
    account: Mapped["AccountModel"] = relationship(back_populates="invite")
