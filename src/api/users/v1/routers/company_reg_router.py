from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from fastapi.responses import RedirectResponse


from src.models import AccountModel
from src.schemas.account_schema import UpdateAccountSchemabyEmail
from src.utils.unit_of_work import UnitOfWork
from src.api.users.v1.service import CompanyRegService
from pydantic import EmailStr
from src.schemas.user_schema import CreateUserSchema
from src.schemas.company_schema import CreateCompanySchema
from src.schemas.secret_schema import CreateSecretSchema


router = APIRouter(prefix="/company/reg", tags=["Company Registration"])


@router.get("/check_account/{account_email}")
async def get_check_account(
    account_email: EmailStr,
    request: Request,
    background_tasks: BackgroundTasks,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    account: AccountModel | None = await CompanyRegService.check_account(
        uow=uow, email=account_email, background_tasks=background_tasks
    )
    if account:
        raise HTTPException(status_code=404, detail="Such an email already exists")
    redirect_url = request.url_for("sign_up")
    return RedirectResponse(url=redirect_url)


@router.post("/sign_up")
async def sign_up(
    account: EmailStr,
    invite_code: int,
    request: Request,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    result = await CompanyRegService.sign_up(uow=uow, code=invite_code, email=account)

    if not result:
        raise HTTPException(status_code=404, detail="Incorrect data has been entered")

    redirect_url = request.url_for("sign_up_complete")
    return RedirectResponse(url=redirect_url, status_code=302)


@router.post("/sign_up_complete")
async def sign_up_complete(
    user: CreateUserSchema,
    secret: CreateSecretSchema,
    account: UpdateAccountSchemabyEmail,
    company: CreateCompanySchema,
    uow: UnitOfWork = Depends(UnitOfWork),
):
    result = await CompanyRegService.sign_up_complete(
        uow=uow,
        user_data=user.model_dump(),
        secret_data=secret.model_dump(),
        account_data=account.model_dump(),
        company_data=company.model_dump(),
    )
    if not result:
        raise HTTPException(
            status_code=404,
            detail="Company and user not create. Probably incorrect data has been entered!",
        )
    return {"status_code": 200, "detail": "The company and the head are registered!"}
