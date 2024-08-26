import datetime

from pydantic import BaseModel, Field, UUID4


class IdCompanySchema(BaseModel):
    id: UUID4


class CreateCompanySchema(BaseModel):
    name: str = Field(max_length=100)
    address: str = Field(max_length=100)
    description: str
    website: str = Field(max_length=30)


class UpdateCompanySchema(IdCompanySchema, CreateCompanySchema): ...


class CompanySchema(IdCompanySchema, CreateCompanySchema):
    created_at: datetime.datetime
    updated_at: datetime.datetime
