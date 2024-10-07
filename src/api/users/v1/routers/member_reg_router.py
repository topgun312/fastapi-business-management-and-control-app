from fastapi import APIRouter, BackgroundTasks, Depends, status
from fastapi_cache.decorator import cache
from pydantic import UUID4

from schemas.invite_schema import InviteCode
from schemas.secret_schema import CreateSecretRequest
from src.api.users.v1.auth_utils.validate import get_current_admin_auth_user
from src.api.users.v1.service import MemberService
from src.schemas.account_schema import CreateAccountRequest
from src.schemas.user_schema import (
    CreateUserRequest,
    UserAuthSchema,
    UserCreateResponse,
    UserDB,
    UserResponse,
)

router = APIRouter(prefix="/member/reg", tags=["Member Registration"])


@router.post("/add_member", status_code=status.HTTP_201_CREATED)
async def add_member_to_company(
    user: CreateUserRequest,
    account: CreateAccountRequest,
    background_tasks: BackgroundTasks,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: MemberService = Depends(MemberService),
) -> dict:
    """Add member to company"""
    if admin:
        member: UserDB | None = await service.add_member(
            admin=admin,
            email=account.model_dump(),
            user_data=user.model_dump(),
            background_tasks=background_tasks,
        )
        return {
            "status": status.HTTP_201_CREATED,
            "detail": f"User {member.first_name} {member.last_name} create. Confirm your profile in the email and complete the registration",
        }


@router.post("/add_password", status_code=status.HTTP_201_CREATED)
async def add_password_and_end_registration(
    invite_code: InviteCode,
    password: CreateSecretRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: MemberService = Depends(MemberService),
) -> UserCreateResponse:
    """Add password and end registration"""
    if admin:
        user_reg: UserDB = await service.enter_password_for_registration(
            code=invite_code.model_dump(),
            password=password.model_dump(),
        )
        return UserCreateResponse(payload=user_reg)


@router.get("/get_member_info/{user_id}", status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def get_member_info_by_user_id(
    user_id: UUID4,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: MemberService = Depends(MemberService),
) -> UserResponse:
    """Get member info by id"""
    if admin:
        user: UserDB = await service.get_member_info_by_id(user_id=user_id)
        return UserResponse(payload=user)
