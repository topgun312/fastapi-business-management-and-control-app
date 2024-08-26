from pydantic import BaseModel

from api.users.v1.auth_utils.validate import (
    get_current_auth_user_for_refresh,
    get_current_active_auth_user,
    validate_auth_user,
)

from src.schemas.user_schema import UserAuthSchema

from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from api.users.v1.auth_utils.helpers import create_refresh_token, create_access_token

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(prefix="/jwt", tags=["JWT"], dependencies=[Depends(http_bearer)])


class Token(BaseModel):
    access_token: str
    refresh_token: str | None = None
    token_type: str = "Bearer"


@router.post("/login", response_model=Token)
def auth_user_issue_jwt(user: UserAuthSchema = Depends(validate_auth_user)):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return Token(access_token=access_token, refresh_token=refresh_token)


@router.get("/users/me")
def auth_user_check_self_info(
    user: UserAuthSchema = Depends(get_current_active_auth_user),
):
    return {"username": user.username, "email": user.email}


@router.post("/refresh", response_model=Token, response_model_exclude_none=True)
def auth_refresh_jwt(user: UserAuthSchema = Depends(get_current_auth_user_for_refresh)):
    access_token = create_access_token(user)
    return Token(access_token=access_token)
