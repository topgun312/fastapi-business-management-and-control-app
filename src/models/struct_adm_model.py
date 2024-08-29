from sqlalchemy import String, Index, func, ForeignKey, Sequence, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship, remote, foreign
from sqlalchemy_utils import LtreeType, Ltree
from src.models import BaseModel
from src.models.mixins.custom_types import integer_pk, created_at_ct, updated_at_ct
from typing import TYPE_CHECKING
from uuid import uuid4
# from sqlalchemy.ext.asyncio import AsyncSession
#
# s = AsyncSession()
from src.database.db import async_session_maker
a = async_session_maker()


if TYPE_CHECKING:
    from src.models import StructAdmPositionModel, CompanyModel

id_seq = Sequence('struct_adm_id_seq')


class StructAdmModel(BaseModel):
    __tablename__ = "struct_adm_table"

    id: Mapped[integer_pk]
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    path: Mapped[Ltree] = mapped_column(LtreeType, nullable=False)
    created_at: Mapped[created_at_ct]
    updated_at: Mapped[updated_at_ct]
    company_id: Mapped[uuid4] = mapped_column(ForeignKey("company_table.id", ondelete="CASCADE"))
    company: Mapped["CompanyModel"] = relationship(back_populates="struct_adm")
    parent = relationship(
        "StructAdmModel",
        primaryjoin=remote(path) == foreign(func.subpath(path, 0, -1)),
        backref="children",
        viewonly=True,
    )
    struct_adm_position: Mapped["StructAdmPositionModel"] = relationship(
        back_populates="struct_adm", cascade="all, delete", passive_deletes=True
    )

    def __init__(self, name, parent=None):
        _id = a.execute(id_seq)
        self.id = _id
        self.name = name
        ltree_id = Ltree(str(_id))
        self.path = ltree_id if parent is None else parent.path + ltree_id



    __table_args__ = (Index("struct_path", path, postgresql_using="gist"),)






































































# class StructAdmModel(BaseModel):
#     __tablename__ = "struct_adm_table"
#
#     id: Mapped[uuid_pk]
#     name: Mapped[str] = mapped_column(String(50), nullable=False)
#     path: Mapped[Ltree] = mapped_column(LtreeType, nullable=False)
#     created_at: Mapped[created_at_ct]
#     updated_at: Mapped[updated_at_ct]
#     company_id: Mapped[uuid4] = mapped_column(ForeignKey("company_table.id", ondelete="CASCADE"))
#     company: Mapped["CompanyModel"] = relationship(back_populates="struct_adm")
#     parent = relationship(
#         "StructAdmModel",
#         primaryjoin=remote(path) == foreign(func.subpath(path, 0, -1)),
#         backref="children",
#         viewonly=True,
#     )
#     struct_adm_position: Mapped["StructAdmPositionModel"] = relationship(
#         back_populates="struct_adm", cascade="all, delete", passive_deletes=True
#     )
#
#     def __init__(self, name, parent=None):
#         # _id = a.execute(id_seq)
#         self.name = name
#         ltree_id = self.id
#         self.path = ltree_id if parent is None else parent.path + ltree_id
#
#
#
#     __table_args__ = (Index("struct_path", path, postgresql_using="gist"),)
