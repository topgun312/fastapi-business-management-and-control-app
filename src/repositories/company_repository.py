from src.models import CompanyModel
from src.utils.repository import SQLAlchemyRepository


class CompanyRepository(SQLAlchemyRepository):
    model = CompanyModel
