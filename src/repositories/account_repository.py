from pydantic import EmailStr
from sqlalchemy import Result, update

from src.models import AccountModel
from src.utils.repository import SQLAlchemyRepository


class AccountRepository(SQLAlchemyRepository):
    model = AccountModel

    async def update_one_by_email(
        self,
        _email: EmailStr,
        **kwargs,
    ) -> type(model) | None:
        query = (
            update(self.model)
            .filter(self.model.email == _email)
            .values(**kwargs)
            .returning(self.model)
        )
        _obj: Result | None = await self.session.execute(query)
        return _obj.scalar_one_or_none()
