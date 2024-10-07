from datetime import datetime, timedelta

import bcrypt
import jwt

from src.config import settings


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    expire_timedelta: timedelta | None = None,
) -> str:
    """Encode JWT"""
    to_encode = payload.copy()
    now = datetime.utcnow()
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(exp=expire, iat=now)
    encoded = jwt.encode(to_encode, private_key, algorithm=algorithm)
    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
) -> dict:
    """Decode JWT"""
    decoded = jwt.decode(token, public_key, algorithms=[algorithm])
    return decoded


async def hash_password(password: str) -> bytes:
    """Hash password"""
    pwd_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password


async def validate_password(password: str, hashed_password: bytes) -> bool:
    """Check valid password"""
    password_byte_enc = password.encode("utf-8")
    hashed_password = hashed_password
    return bcrypt.checkpw(password=password_byte_enc, hashed_password=hashed_password)
