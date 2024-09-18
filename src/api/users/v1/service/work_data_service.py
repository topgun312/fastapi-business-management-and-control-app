from fastapi import HTTPException, status
from pydantic import EmailStr

from src.models import AccountModel, User
from src.schemas.account_schema import AccountDB
from src.schemas.user_schema import UserDB
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode


class WorkDataService(BaseService):

    @transaction_mode
    async def update_email(self, _email: EmailStr, email: dict) -> AccountDB:
      """Update an account by email
      """
      account: AccountModel = await self.uow.account.get_by_query_one_or_none(email=_email)
      self._check_account_exists(account)
      result: AccountModel = await self.uow.account.update_one_by_email(
                _email=_email, email=email.get('email'),
            )
      return result.to_pydantic_schema()

    @transaction_mode
    async def update_user_data(
        self, first_name: str, last_name: str, values: dict,
    ) -> UserDB:
      """Update user first and last name
      """
      user: User = await self.uow.user.get_by_query_one_or_none(
                first_name=first_name, last_name=last_name,
            )
      self._check_user_exists(user)
      new_user: User = await self.uow.user.update_one_by_id(
                _id=user.id,  **values,
            )
      return self._correct_user_schema_answer(user=new_user)

    def _correct_user_schema_answer(self, user: User) -> UserDB:
      """Get correct answer with schema UserDB
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
        member=user.member.to_pydantic_schema(),
      )

    @staticmethod
    def _check_account_exists(account: AccountModel | None) -> None:
      if not account:
        raise HTTPException(
          status_code=status.HTTP_404_NOT_FOUND, detail='Account not found',
        )

    @staticmethod
    def _check_user_exists(user: User | None) -> None:
      if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
