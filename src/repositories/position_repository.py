from src.models import PositionModel
from src.utils.repository import SQLAlchemyRepository


class PositionRepository(SQLAlchemyRepository):
    model = PositionModel
