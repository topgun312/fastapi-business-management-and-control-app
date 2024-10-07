from fastapi import status
from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: int = status.HTTP_200_OK
    error: bool = False


class BaseCreateResponse(BaseModel):
    status: int = status.HTTP_201_CREATED
    error: bool = False
