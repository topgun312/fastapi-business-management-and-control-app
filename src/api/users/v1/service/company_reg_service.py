from pydantic import EmailStr
from src.utils.service import BaseService
from src.workers.tasks import get_invite_code_report
from fastapi import BackgroundTasks, HTTPException
from src.utils.unit_of_work import UnitOfWork
from api.users.v1.user_utils.invite_utils import (
    create_invite_code,
    validate_invite_code,
)


class CompanyRegService(BaseService):
    account_repository: str = "account"
    invite_repository: str = "invite"
    user_repository: str = "user"
    company_repository: str = "company"
    secret_repository: str = "secret"
    member_repository: str = "member"

    @classmethod
    async def check_account(
        cls, uow: UnitOfWork, background_tasks: BackgroundTasks, **kwargs
    ) -> None:
        async with uow:
            account = await uow.__dict__[
                cls.account_repository
            ].get_by_query_one_or_none(**kwargs)
            if account is not None:
                return account
            new_account = await uow.__dict__[
                cls.account_repository
            ].add_one_and_get_obj(**kwargs)
            invite_code = create_invite_code()
            await uow.__dict__[cls.invite_repository].add_one(
                code=invite_code, account_id=new_account.id
            )
            get_invite_code_report(
                background_tasks,
                username=new_account.email,
                email_to=kwargs.get("email"),
                invite_code=invite_code,
            )

    @classmethod
    async def sign_up(cls, uow: UnitOfWork, code: int, email: EmailStr):
        async with uow:
            correct_invite_code = validate_invite_code(code)
            if not correct_invite_code:
                raise HTTPException(status_code=404, detail="Invite invalid")
            account = await uow.__dict__[
                cls.account_repository
            ].get_by_query_one_or_none(email=email)
            if not account:
                raise HTTPException(status_code=404, detail="Account not found")

            result = await uow.__dict__[cls.invite_repository].get_by_query_one_or_none(
                code=code, account_id=account.id
            )
            return result

    @classmethod
    async def sign_up_complete(
        cls, uow: UnitOfWork, user_data, secret_data, account_data, company_data
    ):
        async with uow:
            try:
                user_id = await uow.__dict__[cls.user_repository].add_one_and_get_id(
                    is_superuser=True, **user_data
                )
                account = await uow.__dict__[
                    cls.account_repository
                ].update_one_by_email(
                    _email=account_data["email"],
                    user_id=user_id,
                    email=account_data["email"],
                )  # user_id
                company_id = await uow.__dict__[
                    cls.company_repository
                ].add_one_and_get_id(
                    account_id=account.id, **company_data
                )  # account_id
                await uow.__dict__[cls.secret_repository].add_one(
                    user_id=user_id, account_id=account.id, **secret_data
                )  # user_id, account_id
                await uow.__dict__[cls.member_repository].add_one(
                    user_id=user_id, company_id=company_id
                )
                return True
            except Exception as ex:
                print("Error:" + str(ex))
