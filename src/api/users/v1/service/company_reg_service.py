from collections.abc import Sequence

from src.api.users.v1.user_utils.invite_utils import (
    create_invite_code,
    validate_invite_code,
)
from fastapi import BackgroundTasks, HTTPException, status
from pydantic import UUID4, EmailStr
from sqlalchemy_utils import Ltree

from src.api.users.v1.auth_utils import utils as auth_utils
from src.models import AccountModel, CompanyModel, InviteModel
from src.schemas.company_schema import CompanyDB
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode
from src.workers.tasks import get_invite_code_report


class CompanyRegService(BaseService):

    @transaction_mode
    async def check_account(
          self, email: EmailStr, background_tasks: BackgroundTasks,
    ) -> None:
            """Check account
            """
            account = await self.uow.account.get_by_query_one_or_none(email=email)
            self._check_account_already_exists(account=account)
            new_account: AccountModel = await self.uow.account.add_one_and_get_obj(email=email)
            invite_code = create_invite_code()
            await self.uow.invite.add_one(code=invite_code, account_id=new_account.id)
            get_invite_code_report(
                background_tasks,
                username=new_account.email,
                email_to=email,
                invite_code=invite_code,
            )

    @transaction_mode
    async def sign_up(self, code: int, email: EmailStr) -> None:
            """Sigh up after receiving the code
            """
            correct_invite_code = validate_invite_code(code)
            self._check_correct_invite_code(correct_invite_code)
            account: AccountModel = await self.uow.account.get_by_query_one_or_none(email=email)
            self._check_account_exists(account)
            invite: InviteModel = await self.uow.invite.get_by_query_one_or_none(
                code=code, account_id=account.id,
            )
            self._check_invite_exists(invite)

    @transaction_mode
    async def sign_up_complete(
        self, user_data: dict, secret_data: dict, account_data: dict, company_data: dict,
    ) -> CompanyDB:
      """Completion of the registration of the company and its head
      """
      user_id: int | str = await self.uow.user.add_one_and_get_id(
                    is_admin=True, **user_data,
                )
      account: AccountModel = await self.uow.account.update_one_by_email(
                    _email=account_data['email'],
                    user_id=user_id,
                    email=account_data['email'],
                )
      company: CompanyModel = await self.uow.company.add_one_and_get_obj(
                    account_id=account.id, **company_data,
                )

      await self.uow.secret.add_one(
                    user_id=user_id, account_id=account.id, password=await auth_utils.hash_password(secret_data.get('password')),
                )
      await self.uow.member.add_one(
                    user_id=user_id, company_id=company.id,
                )

      await self.uow.struct_adm.add_one(
          name=company.name, company_id=company.id, path=Ltree(company.name))

      return company.to_pydantic_schema()

    @transaction_mode
    async def get_company_by_id(self, company_id: UUID4) -> CompanyDB:
      """Get company info by id
      """
      company: CompanyModel = await self.uow.company.get_by_query_one_or_none(id=company_id)
      self._check_company_exists(company=company)
      return company.to_pydantic_schema()

    @transaction_mode
    async def get_all_companies(self, **kwargs) -> Sequence[CompanyDB]:
      """Get info about all companies
      """
      companies: Sequence[CompanyModel] = await self.uow.company.get_by_query_all(**kwargs)
      return [company.to_pydantic_schema() for company in companies]

    @transaction_mode
    async def update_company_by_id(self, company_id: UUID4, company_data: dict) -> CompanyDB:
      """Update company info by id
      """
      company: CompanyModel = await self.uow.company.get_by_query_one_or_none(id=company_id)
      self._check_company_exists(company=company)
      updated_company: CompanyModel = await self.uow.company.update_one_by_id(_id=company_id, **company_data)
      return updated_company.to_pydantic_schema()

    @transaction_mode
    async def delete_company_by_id(self, company_id: UUID4) -> None:
      """Delete company by id
      """
      company: CompanyModel = await self.uow.company.get_by_query_one_or_none(id=company_id)
      self._check_company_exists(company=company)
      await self.uow.company.delete_by_query(id=company_id)

    @staticmethod
    def _check_account_exists(account: AccountModel | None) -> None:
      if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Account not found')

    @staticmethod
    def _check_account_already_exists(account: AccountModel | None) -> None:
      if account is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Such an email already exists')

    @staticmethod
    def _check_correct_invite_code(code: int | None) -> None:
      if not code:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invite invalid')

    @staticmethod
    def _check_invite_exists(invite: InviteModel | None) -> None:
      if not invite:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect data has been entered')

    @staticmethod
    def _check_company_exists(company: CompanyModel | None) -> None:
      if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Company not found')
