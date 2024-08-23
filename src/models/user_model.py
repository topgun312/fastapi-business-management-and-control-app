from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import (
        SecretModel,
        InviteModel,
        AccountModel,
        MemberModel,
        UserPositionModel,
        TaskModel,
    )


class User(BaseModel):
    __tablename__ = "user_table"

    id: Mapped[uuid_pk]
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    registered_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    account: Mapped["AccountModel"] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    secret: Mapped["SecretModel"] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True
    )
    member: Mapped["MemberModel"] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True
    )
    user_position: Mapped["UserPositionModel"] = relationship(
        back_populates="user", cascade="all, delete", passive_deletes=True
    )
    author: Mapped["TaskModel"] = relationship(
        back_populates="author_user",
        passive_deletes=True,
        foreign_keys="TaskModel.author_id",
    )
    responsible: Mapped["TaskModel"] = relationship(
        back_populates="responsible_user",
        passive_deletes=True,
        foreign_keys="TaskModel.responsible_id",
    )
