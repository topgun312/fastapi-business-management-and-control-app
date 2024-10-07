from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from pydantic import EmailStr

from src.api.users.v1.auth_utils.helpers import (
    create_access_token,
    create_refresh_token,
)
from src.api.users.v1.auth_utils.validate import (
    get_current_active_auth_user,
    get_current_auth_user_for_refresh,
    validate_auth_user,
)
from src.schemas.user_schema import Token, UserAuthSchema

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(prefix="/jwt", tags=["JWT"], dependencies=[Depends(http_bearer)])


@router.post("/login", response_model=Token)
async def auth_user_issue_jwt(
    user: UserAuthSchema = Depends(validate_auth_user),
) -> Token:
    """Auth user issue JWT"""
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.get("/users/me")
async def auth_user_check_self_info(
    user: UserAuthSchema = Depends(get_current_active_auth_user),
) -> dict[str, EmailStr | str | bool]:
    """Auth user check self info"""
    return {"username": user.username, "is_active": user.is_active}


@router.post("/refresh", response_model=Token, response_model_exclude_none=True)
async def auth_refresh_jwt(
    user: UserAuthSchema = Depends(get_current_auth_user_for_refresh),
) -> Token:
    """Auth refresh JWT"""
    access_token = create_access_token(user)
    return Token(access_token=access_token)
