from fastapi import APIRouter, Depends, status
from pydantic import EmailStr

from src.api.users.v1.auth_utils.validate import get_current_active_auth_user
from src.api.users.v1.service import WorkDataService
from src.models import AccountModel, User
from src.schemas.account_schema import AccountResponse, UpdateAccountRequestByEmail
from src.schemas.user_schema import UpdateUserRequest, UserAuthSchema, UserResponse

router = APIRouter(prefix="/work_data", tags=["Work with member data"])


@router.put("/email_update/{email}", status_code=status.HTTP_200_OK)
async def update_account_email(
    email: EmailStr,
    update_data: UpdateAccountRequestByEmail,
    active_account: UserAuthSchema = Depends(get_current_active_auth_user),
    service: WorkDataService = Depends(WorkDataService),
) -> AccountResponse:
    """Update an account by email"""
    if active_account:
        account: AccountModel | None = await service.update_email(
            _email=email,
            email=update_data.model_dump(),
        )
        return AccountResponse(payload=account)


@router.put("/user_update/{first_name}/{last_name}", status_code=status.HTTP_200_OK)
async def update_user_first_and_last_name(
    first_name: str,
    last_name: str,
    user_data: UpdateUserRequest,
    active_account: UserAuthSchema = Depends(get_current_active_auth_user),
    service: WorkDataService = Depends(WorkDataService),
) -> UserResponse:
    """Update user first and last name"""
    if active_account:
        user: User | None = await service.update_user_data(
            first_name=first_name,
            last_name=last_name,
            values=user_data.model_dump(),
        )
        return UserResponse(payload=user)
