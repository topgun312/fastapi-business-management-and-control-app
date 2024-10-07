from datetime import timedelta

from src.api.users.v1.auth_utils import utils as auth_utils
from src.config import settings
from src.schemas.user_schema import UserAuthSchema

TOKEN_TYPE_FIELD = "token_type"
ACCESS_TOKEN_TYPE = "access_token"
REFRESH_TOKEN_TYPE = "refresh_token"


def create_jwt(
    token_type: str,
    token_data: dict,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    """Create JWT"""
    jwt_payload = {TOKEN_TYPE_FIELD: token_type}
    jwt_payload.update(token_data)
    return auth_utils.encode_jwt(
        payload=jwt_payload,
        expire_minutes=expire_minutes,
        expire_timedelta=expire_timedelta,
    )


def create_access_token(user: UserAuthSchema) -> str:
    """Create access token"""
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "is_active": user.is_active,
    }
    return create_jwt(
        token_type=ACCESS_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_minutes=settings.auth_jwt.access_token_expire_minutes,
    )


def create_refresh_token(user: UserAuthSchema) -> str:
    """Create refresh token"""
    jwt_payload = {
        "sub": user.username,
    }
    return create_jwt(
        token_type=REFRESH_TOKEN_TYPE,
        token_data=jwt_payload,
        expire_timedelta=timedelta(days=settings.auth_jwt.refresh_token_expire_days),
    )
