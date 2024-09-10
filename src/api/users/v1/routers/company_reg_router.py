from fastapi import APIRouter, HTTPException, Request, Depends, BackgroundTasks
from fastapi.responses import RedirectResponse
from src.models import AccountModel
from src.schemas.account_schema import UpdateAccountRequestByEmail
from src.api.users.v1.service import CompanyRegService
from pydantic import EmailStr
from src.schemas.user_schema import CreateUserRequest
from src.schemas.company_schema import CreateCompanyRequest
from src.schemas.secret_schema import CreateSecretRequest


router = APIRouter(prefix="/company/reg", tags=["Company Registration"])


@router.get("/check_account/{account_email}")
async def get_check_account(
    account_email: EmailStr,
    request: Request,
    background_tasks: BackgroundTasks,
    service: CompanyRegService = Depends(CompanyRegService)
) -> RedirectResponse:
    """
    Get check account
    """
    account: AccountModel | None = await service.check_account(
        email=account_email, background_tasks=background_tasks
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
    service: CompanyRegService = Depends(CompanyRegService)
) -> RedirectResponse:
    """
    Sigh up after receiving the code
    """
    await service.sign_up(code=invite_code, email=account)
    redirect_url = request.url_for("sign_up_complete")
    return RedirectResponse(url=redirect_url, status_code=302)


@router.post("/sign_up_complete")
async def sign_up_complete(
    user: CreateUserRequest,
    secret: CreateSecretRequest,
    account: UpdateAccountRequestByEmail,
    company: CreateCompanyRequest,
    service: CompanyRegService = Depends(CompanyRegService)
) ->  dict[str, int | str]:
    """
    Completion of the registration of the company and its head
    """
    result = await service.sign_up_complete(
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
