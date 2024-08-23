from src.models import MemberModel
from src.utils.repository import SQLAlchemyRepository


class MemberRepository(SQLAlchemyRepository):
    model = MemberModel
