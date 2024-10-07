from typing import Annotated

from fastapi import Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from src.api.users.v1.auth_utils import utils as auth_utils
from src.api.users.v1.auth_utils.helpers import (
    ACCESS_TOKEN_TYPE,
    REFRESH_TOKEN_TYPE,
    TOKEN_TYPE_FIELD,
)
from src.api.users.v1.service.jwt_auth_service import JWTAuthService
from src.schemas.user_schema import UserAuthSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/jwt/login")


def get_current_token_payload(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    """Get current token payload"""
    try:
        payload = auth_utils.decode_jwt(token=token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid token error",
        )
    return payload


def validate_token_type(payload: dict, token_type: str) -> bool:
    """Check valid token type"""
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Invalid token type {current_token_type!r} expected {token_type!r}",
    )


async def get_user_by_token_sub(payload: dict, service) -> UserAuthSchema:
    """Get user by token sub"""
    username: str | None = payload.get("sub")
    user = await service.get_user(username=username)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_auth_user_from_token_of_type(token_type: str):
    """Get auth user from token of type"""

    async def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
        service: JWTAuthService = Depends(JWTAuthService),
    ) -> UserAuthSchema:
        validate_token_type(payload, token_type)
        return await get_user_by_token_sub(payload, service)

    return get_auth_user_from_token


get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)

get_current_auth_user_for_refresh = get_auth_user_from_token_of_type(REFRESH_TOKEN_TYPE)


async def get_current_active_auth_user(
    user: UserAuthSchema = Depends(get_current_auth_user),
) -> UserAuthSchema:
    """Get current active auth user"""
    if user.is_active:
        return user

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user inactive")


async def get_current_admin_auth_user(
    user: UserAuthSchema = Depends(get_current_auth_user),
) -> UserAuthSchema:
    """Get current admin auth user"""
    if user.is_admin:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN, detail="user is not admin"
    )


async def validate_auth_user(
    username: str = Form(),
    password: str = Form(),
    service: JWTAuthService = Depends(JWTAuthService),
):
    """Check valid auth user"""
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )

    if not (user := await service.get_user(username=username)):
        raise unauthed_exc

    if not await auth_utils.validate_password(
        password=password,
        hashed_password=user.password,
    ):
        raise unauthed_exc

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user unactive",
        )
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user  is not an admin",
        )
    return user
