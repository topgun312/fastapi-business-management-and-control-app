from sqlalchemy import insert

from src.models import StructAdmModel
from src.utils.repository import SQLAlchemyRepository


class StructAdmRepository(SQLAlchemyRepository):
    model = StructAdmModel

    # async def add_one_struct_adm_company_head(self, **kwargs):
    #     query = insert(self.model).values(kwargs)
    #     await self.session.execute(query)


