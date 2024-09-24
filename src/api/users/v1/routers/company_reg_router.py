from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, status
from fastapi_cache.decorator import cache
from pydantic import UUID4, EmailStr

from src.api.users.v1.auth_utils.validate import get_current_active_auth_user, get_current_admin_auth_user
from src.api.users.v1.service import CompanyRegService
from src.schemas.account_schema import UpdateAccountRequestByEmail
from src.schemas.company_schema import CompanyDB, CompanyResponse, CreateCompanyRequest, UpdateCompanyRequest, CompanyCreateResponse
from src.schemas.secret_schema import CreateSecretRequest
from src.schemas.user_schema import CreateUserRequest, UserAuthSchema

router = APIRouter(prefix='/company/reg', tags=['Company Registration'])


@router.get('/check_account/{account_email}', status_code=status.HTTP_200_OK)
async def get_check_account(
    account_email: EmailStr,
    background_tasks: BackgroundTasks,
    service: CompanyRegService = Depends(CompanyRegService),
) -> dict[str, int | str]:
    """Get check account
    """
    await service.check_account(
        email=account_email, background_tasks=background_tasks,
    )
    return {
        "status": status.HTTP_200_OK,
        "detail": f"A message with an invite_code has been sent to email {account_email}"
    }


@router.get('/sign_up', status_code=status.HTTP_200_OK)
async def sign_up(
    account: EmailStr,
    invite_code: int,
    service: CompanyRegService = Depends(CompanyRegService),
) -> dict[str, int | str]:
    """Sigh up after receiving the code
    """
    await service.sign_up(code=invite_code, email=account)
    return {
        "status": status.HTTP_200_OK,
        "detail": f"The invite_code and email are valid! Please complete the registration of the company"
    }


@router.post('/sign_up_complete', status_code=status.HTTP_201_CREATED)
async def sign_up_complete(
    user: CreateUserRequest,
    secret: CreateSecretRequest,
    account: UpdateAccountRequestByEmail,
    company: CreateCompanyRequest,
    service: CompanyRegService = Depends(CompanyRegService),
) -> CompanyCreateResponse:
    """Completion of the registration of the company and its head
    """
    result: CompanyDB = await service.sign_up_complete(
        user_data=user.model_dump(),
        secret_data=secret.model_dump(),
        account_data=account.model_dump(),
        company_data=company.model_dump(),
    )
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Company and user not create. Probably incorrect data has been entered!',
        )
    return CompanyCreateResponse(payload=result)


@router.get('/get_company/{company_id}', status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def get_company_by_id(company_id: UUID4,
                            active_account: UserAuthSchema = Depends(get_current_active_auth_user),
                            service: CompanyRegService = Depends(CompanyRegService)) -> CompanyResponse:
    """Get company info by id
    """
    if active_account:
        company: CompanyDB = await service.get_company_by_id(company_id=company_id)
        return CompanyResponse(payload=company)


@router.get('/get_all_companies', status_code=status.HTTP_200_OK)
@cache(expire=3600)
async def get_all_companies(active_account: UserAuthSchema = Depends(get_current_active_auth_user),
                            service: CompanyRegService = Depends(CompanyRegService)) -> list[CompanyDB]:
    """Get info about all companies
    """
    if active_account:
        companies: list[CompanyDB] | None = await service.get_all_companies()
        return companies


@router.put('/update_company/{company_id}', status_code=status.HTTP_200_OK)
async def update_company_by_id(company_id: UUID4, company_data: UpdateCompanyRequest,
                               admin: UserAuthSchema = Depends(get_current_admin_auth_user),
                               service: CompanyRegService = Depends(CompanyRegService)) -> CompanyResponse:
    """Update company info by id
    """
    if admin:
        updated_company: CompanyDB = await service.update_company_by_id(company_id=company_id, company_data=company_data.model_dump())
        return CompanyResponse(payload=updated_company)


@router.delete('/delete_company/{company_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_company_by_id(company_id: UUID4,
                               admin: UserAuthSchema = Depends(get_current_admin_auth_user),
                                service: CompanyRegService = Depends(CompanyRegService)) ->  None:
    """Delete company by id
    """
    if admin:
        await service.delete_company_by_id(company_id=company_id)
