from fastapi import HTTPException, BackgroundTasks
from src.schemas.user_schema import UserDB
from src.models import User, AccountModel, CompanyModel, InviteModel
from api.users.v1.user_utils.invite_utils import create_invite_code
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode
from src.workers.tasks import get_invite_code_report
from src.api.users.v1.auth_utils import utils as auth_utils


class MemberService(BaseService):
    account_repository: str = "account"
    member_repository: str = "member"
    invite_repository: str = "invite"
    user_repository: str = "user"
    company_repository: str = "company"
    secret_repository: str = "secret"


    @transaction_mode
    async def add_member(
        self, admin: User, email: dict, user_data: dict, background_tasks: BackgroundTasks
    ) -> User:
      """
      Add member to company
      """
      admin_account = await self.uow.account.get_by_query_one_or_none(user_id=admin.id)
      check_account = await self.uow.account.get_by_query_one_or_none(email=email.get("email"))
      self._check_account_already_exists(check_account)
      user = await self.uow.user.add_one_and_get_obj(
                    **user_data
                )
      account = await self.uow.account.add_one_and_get_obj(user_id=user.id, email=email.get("email"))
      company = await self.uow.company.get_by_query_one_or_none(account_id=admin_account.id)
      self._check_company_exists(company)

      await self.uow.member.add_one(
                    user_id=user.id, company_id=company.id
                )
      invite_code = create_invite_code()
      print(invite_code)
      await self.uow.invite.add_one(
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


    @transaction_mode
    async def enter_password_for_registration(
        self, code: int, password: str
    ) -> UserDB:
      """
      Add password and end registration
      """
      invite_code = await self.uow.invite.get_by_query_one_or_none(code=code)
      self._check_invite_exists(invite_code)
      account = await self.uow.account.get_by_query_one_or_none(invite=invite_code)
      await self.uow.secret.add_one(
                    password=await auth_utils.hash_password(password), user_id=account.user_id, account_id=account.id
            )
      user = await self.uow.user.get_by_query_one_or_none(account=account)
      return self._correct_user_schema_answer(user=user)

    def _correct_user_schema_answer(self, user: User) -> UserDB:
      """
      Get correct answer with schema UserDB
      """
      return UserDB(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        registered_at=user.registered_at,
        updated_at=user.updated_at,
        is_active=user.is_active,
        is_admin=user.is_admin,
        account=user.account.to_pydantic_schema(),
        member=user.member.to_pydantic_schema()
      )

    @staticmethod
    def _check_user_exists(user: User | None) -> None:
      if not user:
        raise HTTPException(status_code=404, detail="User not found")

    @staticmethod
    def _check_account_already_exists(check_account: AccountModel | None) -> None:
        if check_account is not None:
            raise HTTPException(
                status_code=404, detail="Such an email already exists"
            )

    @staticmethod
    def _check_account_exists(account: AccountModel | None) -> None:
        if not account:
            raise HTTPException(
                status_code=404, detail="Account not found"
            )

    @staticmethod
    def _check_company_exists(company: CompanyModel | None) -> None:
      if not company:
        raise HTTPException(status_code=404, detail="Company not found")

    @staticmethod
    def _check_invite_exists(invite: InviteModel | None) -> None:
      if not invite:
          raise HTTPException(status_code=404, detail="Invite code not found")
