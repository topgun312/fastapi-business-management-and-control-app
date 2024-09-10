from typing import Optional

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4

from src.schemas.company_schema import CompanyDB
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.models import AccountModel, MemberModel, StructAdmModel


class CompanyModel(BaseModel):
    __tablename__ = "company_table"

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    website: Mapped[str] = mapped_column(String(30), nullable=False)
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    account_id: Mapped[Optional[uuid4]] = mapped_column(
        ForeignKey("account_table.id", ondelete="SET NULL"), nullable=True
    )
    director: Mapped["AccountModel"] = relationship(back_populates="company")
    member: Mapped["MemberModel"] = relationship(
        back_populates="company", cascade="all, delete", passive_deletes=True
    )
    struct_adm: Mapped["StructAdmModel"] = relationship(back_populates="company",
                                                        cascade="all, delete", passive_deletes=True)

    __table_args__ = (UniqueConstraint("account_id"),)

    def to_pydantic_schema(self) -> CompanyDB:
        return CompanyDB(**self.__dict__)

