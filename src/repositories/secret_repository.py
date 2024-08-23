from src.models import SecretModel
from src.utils.repository import SQLAlchemyRepository


class SecretRepository(SQLAlchemyRepository):
    model = SecretModel
