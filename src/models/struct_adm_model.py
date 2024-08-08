from sqlalchemy import String, Index, func
from sqlalchemy.orm import Mapped, mapped_column, relationship, remote, foreign
from sqlalchemy_utils import LtreeType, Ltree
from src.models import BaseModel
from src.models.mixins.custom_types import uuid_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models import StructAdmPositionModel


class StructAdmModel(BaseModel):
    __tablename__ = "struct_adm_table"

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    path: Mapped[Ltree] = mapped_column(LtreeType)
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    parent = relationship(
        "StructAdmModel",
        primaryjoin=remote(path) == foreign(func.subpath(path, 0, -1)),
        backref="children",
        viewonly=True,
    )
    struct_adm_position: Mapped["StructAdmPositionModel"] = relationship(
        back_populates="struct_adm", cascade="all, delete", passive_deletes=True
    )

    __table_args__ = (Index("struct_path", path, postgresql_using="gist"),)
