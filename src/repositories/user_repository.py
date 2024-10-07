from collections.abc import Sequence

from pydantic import EmailStr
from sqlalchemy import Result, select

from src.models import AccountModel, User
from src.utils.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

    async def get_user_by_email(self, username: EmailStr) -> type(model) | None:
        query = (
            select(self.model)
            .join(AccountModel.user)
            .where(AccountModel.email == username)
        )
        res: Result = await self.session.execute(query)
        return res.unique().scalar_one_or_none()

    async def get_by_query_all_in_users_list(
        self, task_data: dict
    ) -> Sequence[type(model)]:
        id_user_list = [id.get("id") for id in task_data]
        query = select(self.model).filter(self.model.id.in_(id_user_list))
        res: Result = await self.session.execute(query)
        return res.scalars().all()
