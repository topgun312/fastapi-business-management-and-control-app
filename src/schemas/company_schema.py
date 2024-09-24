import datetime

from pydantic import UUID4, BaseModel, Field

from src.schemas.response import BaseResponse, BaseCreateResponse


class CompanyId(BaseModel):
    id: UUID4


class CreateCompanyRequest(BaseModel):
    name: str = Field(max_length=100)
    address: str = Field(max_length=100)
    description: str
    website: str = Field(max_length=30)


class UpdateCompanyRequest(CompanyId, CreateCompanyRequest): ...


class CompanyDB(CompanyId, CreateCompanyRequest):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class CompanyResponse(BaseResponse):
    payload: CompanyDB


class CompanyListResponse(BaseResponse):
    payload: list[CompanyDB]


class CompanyCreateResponse(BaseCreateResponse):
    payload: CompanyDB


class TestCompanySchema(BaseModel):
    id: UUID4
    name: str = Field(max_length=100)
    address: str = Field(max_length=100)
    description: str
    website: str = Field(max_length=30)
    account_id: UUID4
