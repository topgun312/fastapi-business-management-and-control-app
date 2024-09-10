from uuid import uuid4

from pydantic import EmailStr
from sqlalchemy_utils import Ltree

from src.models import AccountModel, InviteModel
from src.utils.service import BaseService
from src.workers.tasks import get_invite_code_report
from fastapi import BackgroundTasks, HTTPException, Depends
from src.utils.unit_of_work import transaction_mode
from api.users.v1.user_utils.invite_utils import (
    create_invite_code,
    validate_invite_code,
)
from src.api.users.v1.auth_utils import utils as auth_utils


class CompanyRegService(BaseService):
    account_repository: str = "account"
    invite_repository: str = "invite"
    user_repository: str = "user"
    company_repository: str = "company"
    secret_repository: str = "secret"
    member_repository: str = "member"
    struct_adm_repository: str = "struct_adm"

    @transaction_mode
    async def check_account(
          self, email: EmailStr, background_tasks: BackgroundTasks
    ) -> None:
            """
            Check account
            """
            account = await self.uow.account.get_by_query_one_or_none(email=email)
            if account is not None:
                return account
            new_account = await self.uow.account.add_one_and_get_obj(email=email)
            invite_code = create_invite_code()
            print(invite_code)
            await self.uow.invite.add_one(code=invite_code, account_id=new_account.id)
            get_invite_code_report(
                background_tasks,
                username=new_account.email,
                email_to=email,
                invite_code=invite_code,
            )

    @transaction_mode
    async def sign_up(self, code: int, email: EmailStr) -> None:
            """
            Sigh up after receiving the code
            """
            correct_invite_code = validate_invite_code(code)
            self._check_correct_invite_code(correct_invite_code)
            account = await self.uow.account.get_by_query_one_or_none(email=email)
            self._check_account_exists(account)
            invite = await self.uow.invite.get_by_query_one_or_none(
                code=code, account_id=account.id
            )
            self._check_invite_exists(invite)


    @transaction_mode
    async def sign_up_complete(
        self, user_data: dict, secret_data: dict, account_data: dict, company_data: dict
    ):
      """
      Completion of the registration of the company and its head
      """
      user_id = await self.uow.user.add_one_and_get_id(
                    is_admin=True, **user_data
                )
      account = await self.uow.account.update_one_by_email(
                    _email=account_data["email"],
                    user_id=user_id,
                    email=account_data["email"],
                )
      company = await self.uow.company.add_one_and_get_obj(
                    account_id=account.id, **company_data
                )

      await self.uow.secret.add_one(
                    user_id=user_id, account_id=account.id, password=await auth_utils.hash_password(secret_data.get("password"))
                )
      await self.uow.member.add_one(
                    user_id=user_id, company_id=company.id
                )

      # a = await self.uow.struct_adm.add_one_and_get_obj(
      #     name=company.name, company_id=company.id
      # ) #вот здесь пытаюсь создать вершину дерева) только в модель в поле path ничего не добавляется
      # print(a)

      return True

    @staticmethod
    def _check_account_exists(account: AccountModel | None) -> None:
      if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    @staticmethod
    def _check_correct_invite_code(code: int | None) -> None:
      if not code:
        raise HTTPException(status_code=404, detail="Invite invalid")

    @staticmethod
    def _check_invite_exists(invite: InviteModel | None) -> None:
      if not invite:
        raise HTTPException(status_code=404, detail="Incorrect data has been entered")