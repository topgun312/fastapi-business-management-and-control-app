from fastapi import Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from api.users.v1.auth_utils.helpers import (
    REFRESH_TOKEN_TYPE,
    ACCESS_TOKEN_TYPE,
    TOKEN_TYPE_FIELD,
)
from api.users.v1.auth_utils import utils as auth_utils
from src.schemas.user_schema import UserAuthSchema


john = UserAuthSchema(
    username="john@gmail.com",
    email="john@gmail.com",
    password=auth_utils.hash_password("qwerty"),
)

sam = UserAuthSchema(
    username="sam@gmail.com",
    email="sam@gmail.com",
    password=auth_utils.hash_password("secret"),
)

users_db: dict[str, UserAuthSchema] = {john.username: john, sam.email: sam}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/jwt/login")


def get_current_token_payload(token: str = Depends(oauth2_scheme)) -> UserAuthSchema:
    try:
        payload = auth_utils.decode_jwt(token=token)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token error"
        )
    return payload


def validate_token_type(payload: dict, token_type: str) -> bool:
    current_token_type = payload.get(TOKEN_TYPE_FIELD)
    if current_token_type == token_type:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Invalid token type {current_token_type!r} expected {token_type!r}",
    )


def get_user_by_token_sub(payload: dict) -> UserAuthSchema:
    username: str | None = payload.get("sub")
    if user := users_db.get(username):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_auth_user_from_token_of_type(token_type: str):
    def get_auth_user_from_token(
        payload: dict = Depends(get_current_token_payload),
    ) -> UserAuthSchema:
        validate_token_type(payload, token_type)
        return get_user_by_token_sub(payload)

    return get_auth_user_from_token


get_current_auth_user = get_auth_user_from_token_of_type(ACCESS_TOKEN_TYPE)

get_current_auth_user_for_refresh = get_auth_user_from_token_of_type(REFRESH_TOKEN_TYPE)


def get_current_active_auth_user(user: UserAuthSchema = Depends(get_current_auth_user)):
    if user.active:
        return user

    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="user inactive")


def validate_auth_user(username: str = Form(), password: str = Form()):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid email or password"
    )
    if not (user := users_db.get(username)):
        raise unauthed_exc

    if not auth_utils.validate_password(
        password=password, hashed_password=user.password
    ):
        raise unauthed_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="user unactive"
        )
    return user
