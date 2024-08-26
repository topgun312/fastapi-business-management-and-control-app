from src.models import InviteModel
from src.utils.repository import SQLAlchemyRepository


class InviteRepository(SQLAlchemyRepository):
    model = InviteModel
