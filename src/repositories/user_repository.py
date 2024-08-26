from sqlalchemy import select, Result

from src.models import User
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

    async def get_admin(self, _first_name: str) -> type(model) | None:
        query = select(self.model).filter_by(first_name=_first_name, is_superuser=True)
        res: Result = await self.session.execute(query)
        return res.unique().scalar_one_or_none()
