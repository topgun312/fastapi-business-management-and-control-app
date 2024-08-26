from fastapi import HTTPException
from pydantic import EmailStr
from utils.service import BaseService
from utils.unit_of_work import UnitOfWork


class WorkDataService(BaseService):
    account_repository: str = "account"
    user_repository: str = "user"

    @classmethod
    async def update_email(cls, uow: UnitOfWork, _email: EmailStr, email: dict):
        async with uow:
            account = await uow.__dict__[
                cls.account_repository
            ].get_by_query_one_or_none(email=_email)
            if not account:
                raise HTTPException(status_code=404, detail="Account not found")
            result = await uow.__dict__[cls.account_repository].update_one_by_email(
                _email=_email, email=email.get("email")
            )
            return result

    @classmethod
    async def update_user_data(
        cls, uow: UnitOfWork, first_name: str, last_name: str, values: dict
    ):
        async with uow:
            user = await uow.__dict__[cls.user_repository].get_by_query_one_or_none(
                first_name=first_name, last_name=last_name
            )
            if not user:
                raise HTTPException(status_code=404, detail="User not found")
            new_user = await uow.__dict__[cls.user_repository].update_one_by_id(
                _id=user.id, values=values
            )
            return new_user
