from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks

from schemas.account_schema import CreateAccountSchema
from src.schemas.user_schema import CreateUserSchema
from src.models import User
from api.users.v1.service import MemberService
from src.utils.unit_of_work import UnitOfWork


router = APIRouter(prefix="/member/reg", tags=["Member Registration"])


@router.get("/check_admin/{first_name}")
async def get_check_admin_account(
    first_name: str, uow: UnitOfWork = Depends(UnitOfWork)
):
    admin: User | None = await MemberService.check_admin_account(
        uow=uow, first_name=first_name
    )
    if not admin:
        raise HTTPException(
            status_code=404, detail=f"The user {first_name} does not have admin rights"
        )
    return {"status_code": 200, "detail": f"The user {first_name} has admin rights!"}


@router.post("/add_member")
async def add_member_to_company(
    user: CreateUserSchema,
    account: CreateAccountSchema,
    background_tasks: BackgroundTasks,
    admin: User = Depends(get_check_admin_account),
    uow: UnitOfWork = Depends(UnitOfWork),
):
    if admin:
        member: User | None = await MemberService.add_member(
            uow=uow,
            admin=admin,
            background_tasks=background_tasks,
            email=account.model_dump(),
            user_data=user.model_dump(),
        )
        return {
            "status": 200,
            "detail": f"User {member.first_name} create. Confirm your profile in the email and complete the registration",
        }
    else:
        raise HTTPException(
            status_code=404,
            detail=f"User {admin.first_name} is not an admin of the company!",
        )


@router.post("/add_password")
async def add_password_and_end_registration(
    invite_code: int, password: str, uow: UnitOfWork = Depends(UnitOfWork)
):
    secret: bool = await MemberService.enter_password_for_registration(
        uow=uow, code=invite_code, password=password
    )
    if not secret:
        raise HTTPException(
            status_code=404,
            detail="The password has not been added. Enter the correct data ",
        )
    return {"status_code": 200, "detail": "The password was successfully added!"}
