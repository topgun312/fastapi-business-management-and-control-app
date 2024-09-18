from pydantic import EmailStr

from src.schemas.user_schema import UserAuthSchema
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode


class JWTAuthService(BaseService):

  @transaction_mode
  async def get_user(
          self, username: EmailStr,
  ) -> UserAuthSchema:
    """Get user by email
    """
    user = await self.uow.user.get_user_by_email(username=username)
    return UserAuthSchema(
            id=user.id,
            username=user.account.email,
            password=user.secret.password,
            is_active=user.is_active,
            is_admin=user.is_admin,
        )
