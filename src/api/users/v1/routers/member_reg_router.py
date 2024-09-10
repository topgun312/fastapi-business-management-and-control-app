from fastapi import APIRouter, Depends, BackgroundTasks

from src.api.users.v1.auth_utils.validate import get_current_admin_auth_user
from schemas.account_schema import CreateAccountRequest
from src.schemas.user_schema import CreateUserRequest, UserResponse, UserAuthSchema
from src.models import User
from api.users.v1.service import MemberService


router = APIRouter(prefix="/member/reg", tags=["Member Registration"])


@router.post("/add_member")
async def add_member_to_company(
    user: CreateUserRequest,
    account: CreateAccountRequest,
    background_tasks: BackgroundTasks,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: MemberService = Depends(MemberService)
) -> dict:
    """
    Add member to company
    """
    if admin:
        member: User | None = await service.add_member(
            admin=admin,
            email=account.model_dump(),
            user_data=user.model_dump(),
            background_tasks=background_tasks
        )
        return {
            "status": 200,
            "detail": f"User {member.first_name} {member.last_name} create. Confirm your profile in the email and complete the registration",
        }



@router.post("/add_password")
async def add_password_and_end_registration(
    invite_code: int, password: str,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: MemberService = Depends(MemberService)
) -> UserResponse:
    """
    Add password and end registration
    """
    if admin:
        user_reg: User = await service.enter_password_for_registration(
            code=invite_code, password=password
        )
        return UserResponse(payload=user_reg)
