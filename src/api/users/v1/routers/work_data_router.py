from fastapi import APIRouter, Depends
from pydantic import EmailStr

from api.users.v1.service import WorkDataService
from models import AccountModel, User
from src.schemas.user_schema import UpdateUserRequest, UserResponse
from src.schemas.account_schema import UpdateAccountRequestByEmail, AccountResponse


router = APIRouter(prefix="/work_data", tags=["Work with member data"])


@router.put("/email_update")
async def update_account_email(
    email: EmailStr,
    update_data: UpdateAccountRequestByEmail,
    service: WorkDataService = Depends(WorkDataService)
) -> AccountResponse:
    """
    Update an account by email
    """
    account: AccountModel | None = await service.update_email(
         _email=email, email=update_data.model_dump()
    )
    return AccountResponse(payload=account)


@router.put("/user_update")
async def update_user_first_and_last_name(
    first_name: str,
    last_name: str,
    user_data: UpdateUserRequest,
    service: WorkDataService = Depends(WorkDataService)
) -> UserResponse:
    """
    Update user first and last name
    """
    user: User | None = await service.update_user_data(
        first_name=first_name,
        last_name=last_name,
        values=user_data.model_dump(),
    )
    return UserResponse(payload=user)