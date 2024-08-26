from src.models import StructAdmPositionModel
from src.utils.repository import SQLAlchemyRepository


class StructAdmPositionRepository(SQLAlchemyRepository):
    model = StructAdmPositionModel
