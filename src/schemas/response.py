from pydantic import BaseModel
from fastapi import status


class BaseResponse(BaseModel):
    status: int = status.HTTP_200_OK
    error: bool = False

class BaseCreateResponse(BaseModel):
    status: int = status.HTTP_201_CREATED
    error: bool = False