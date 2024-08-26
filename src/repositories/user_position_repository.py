from src.models import UserPositionModel
from src.utils.repository import SQLAlchemyRepository


class UserPositionRepository(SQLAlchemyRepository):
    model = UserPositionModel
