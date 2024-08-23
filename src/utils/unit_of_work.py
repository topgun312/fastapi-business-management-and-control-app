from abc import abstractmethod, ABC
from src.database.db import async_session_maker
from src.repositories import (
    UserRepository,
    UserPositionRepository,
    PositionRepository,
    SecretRepository,
    InviteRepository,
    MemberRepository,
    CompanyRepository,
    StructAdmRepository,
    StructAdmPositionRepository,
    AccountRepository,
    TaskRepository,
)


class AbstractUnitOfWork(ABC):
    user: UserRepository
    user_position: UserPositionRepository
    position: PositionRepository
    secret: SecretRepository
    invite: InviteRepository
    member: MemberRepository
    company: CompanyRepository
    struct_adm: StructAdmRepository
    struct_adm_position: StructAdmPositionRepository
    account: AccountRepository
    task: TaskRepository

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()
        self.user = UserRepository(self.session)
        self.user_position = UserPositionRepository(self.session)
        self.position = PositionRepository(self.session)
        self.secret = SecretRepository(self.session)
        self.invite = InviteRepository(self.session)
        self.member = MemberRepository(self.session)
        self.company = CompanyRepository(self.session)
        self.struct_adm = StructAdmRepository(self.session)
        self.struct_adm_position = StructAdmPositionRepository(self.session)
        self.account = AccountRepository(self.session)
        self.task = TaskRepository(self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            await self.commit()
        else:
            await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
