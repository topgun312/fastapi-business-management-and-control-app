from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base_model import BaseModel
from src.models.mixins.custom_types import created_at_ct, updated_at_ct, uuid_pk
from src.schemas.user_schema import UserDB

if TYPE_CHECKING:
    from src.models import (
        AccountModel,
        MemberModel,
        SecretModel,
        StructAdmModel,
        TaskModel,
        UserPositionModel,
    )


class User(BaseModel):
    __tablename__ = "user_table"

    id: Mapped[uuid_pk]
    first_name: Mapped[str] = mapped_column(String(30))
    last_name: Mapped[str] = mapped_column(String(30))
    registered_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    account: Mapped["AccountModel"] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    secret: Mapped["SecretModel"] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    member: Mapped["MemberModel"] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
        lazy="selectin",
    )
    user_position: Mapped["UserPositionModel"] = relationship(
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True,
    )
    struct_adm: Mapped["StructAdmModel"] = relationship(
        back_populates="head_user",
        passive_deletes=True,
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

    def to_pydantic_schema(self) -> UserDB:
        return UserDB(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            registered_at=self.registered_at,
            updated_at=self.updated_at,
            is_active=self.is_active,
            is_admin=self.is_admin,
            account=self.account.to_pydantic_schema(),
            member=self.member.to_pydantic_schema(),
        )
