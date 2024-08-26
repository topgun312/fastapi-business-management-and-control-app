from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr

from api.users.v1.service import WorkDataService
from models import AccountModel, User
from src.schemas.user_schema import UpdateUserSchema
from src.schemas.account_schema import UpdateAccountSchemabyEmail
from src.utils.unit_of_work import UnitOfWork


router = APIRouter(prefix="/work_data", tags=["Work with member data"])


@router.put("/email_update")
async def update_account_email(
    email: EmailStr,
    update_data: UpdateAccountSchemabyEmail,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    account: AccountModel | None = await WorkDataService.update_email(
        uow=uow, _email=email, email=update_data.model_dump()
    )
    if not account:
        raise HTTPException(status_code=404, detail="Account email editing error!")

    return {
        "status_code": 201,
        "detail": "The email has been successfully edited",
        "email": f"Account email: {account.email}",
    }


@router.put("/user_update")
async def update_user_first_and_last_name(
    first_name: str,
    last_name: str,
    user_data: UpdateUserSchema,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    user: User | None = await WorkDataService.update_user_data(
        uow=uow,
        first_name=first_name,
        last_name=last_name,
        values=user_data.model_dump(),
    )
    if not user:
        raise HTTPException(status_code=404, detail="User data editing error!")
    return {
        "status_code": 201,
        "detail": "The user's data has been successfully edited",
        "user": f"User first_name: {user.first_name}, last_name: {user.last_name}",
    }
