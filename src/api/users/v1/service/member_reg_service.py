from fastapi import HTTPException

from api.users.v1.user_utils.invite_utils import create_invite_code
from src.utils.service import BaseService
from src.utils.unit_of_work import UnitOfWork
from src.workers.tasks import get_invite_code_report


class MemberService(BaseService):
    account_repository: str = "account"
    member_repository: str = "member"
    invite_repository: str = "invite"
    user_repository: str = "user"
    company_repository: str = "company"
    secret_repository: str = "secret"

    @classmethod
    async def check_admin_account(cls, uow: UnitOfWork, first_name: str) -> None:
        async with uow:
            admin = await uow.__dict__[cls.user_repository].get_admin(
                _first_name=first_name
            )
            return admin

    @classmethod
    async def add_member(
        cls, uow: UnitOfWork, admin, background_tasks, email, user_data
    ):
        async with uow:
            try:
                check_account = await uow.__dict__[
                    cls.account_repository
                ].get_by_query_one_or_none(email=email.get("email"))
                if check_account is not None:
                    raise HTTPException(
                        status_code=404, detail="Such an email already exists"
                    )
                user = await uow.__dict__[cls.user_repository].add_one_and_get_obj(
                    **user_data
                )
                account = await uow.__dict__[
                    cls.account_repository
                ].add_one_and_get_obj(user_id=user.id, email=email.get("email"))
                company = await uow.__dict__[
                    cls.company_repository
                ].get_by_query_one_or_none(account_id=admin.account.id)
                await uow.__dict__[cls.member_repository].add_one(
                    user_id=user.id, company_id=company.id
                )
                invite_code = create_invite_code()
                await uow.__dict__[cls.invite_repository].add_one(
                    code=invite_code, account_id=account.id
                )
                get_invite_code_report(
                    background_tasks,
                    username=account.email,
                    email_to=email.get("email"),
                    invite_code=invite_code,
                    href="http://127.0.0.1:8000/api/reg_member/member/reg/add_password",
                    href_name="End registration",
                )

                return user
            except Exception as ex:
                print("Error:" + str(ex))

    @classmethod
    async def enter_password_for_registration(
        cls, uow: UnitOfWork, code: int, password: str
    ):
        async with uow:
            try:
                invite_code = await uow.__dict__[
                    cls.invite_repository
                ].get_by_query_one_or_none(code=code)
                if not invite_code:
                    raise HTTPException(status_code=404, detail="Invite code not found")
                account = await uow.__dict__[
                    cls.account_repository
                ].get_by_query_one_or_none(invite=invite_code)
                await uow.__dict__[cls.secret_repository].add_one(
                    password=password, user_id=account.user_id, account_id=account.id
                )
                return True
            except Exception as ex:
                print("Error:" + str(ex))
