from src.models import StructAdmModel
from src.utils.repository import SQLAlchemyRepository


class StructAdmRepository(SQLAlchemyRepository):
    model = StructAdmModel
