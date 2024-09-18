__all__ = [
  'FakeBaseService',
  'FakeCompanyRegService',
  'FakeMemberService',
  'FakeTasksService',
  'FakeUnitOfWork',
  'FakeWorkDataService',
  'FakeWorkStructureService',
  'postgres',
  'test_cases',
]

from types import TracebackType

from sqlalchemy.ext.asyncio import AsyncSession

from src import repositories
from src.api.structure.v1.service import WorkStructureService
from src.api.tasks.v1.service import TasksService
from src.api.users.v1.service import CompanyRegService, MemberService, WorkDataService
from src.utils.service import BaseService
from src.utils.unit_of_work import UnitOfWork
from tests.fixtures import postgres, test_cases


class FakeUnitOfWork(UnitOfWork):
  """Test class for overriding the standard UnitOfWork.
  Provides isolation using transactions at the level of a single TestCase.
  """

  def __init__(self, session: AsyncSession) -> None:
    super().__init__()
    self._session = session

  async def __aenter__(self) -> None:
    self.user = repositories.UserRepository(self._session)
    self.user_position = repositories.UserPositionRepository(self._session)
    self.position = repositories.PositionRepository(self._session)
    self.secret = repositories.SecretRepository(self._session)
    self.invite = repositories.InviteRepository(self._session)
    self.member = repositories.MemberRepository(self._session)
    self.company = repositories.CompanyRepository(self._session)
    self.struct_adm = repositories.StructAdmRepository(self._session)
    self.struct_adm_position = repositories.StructAdmPositionRepository(self._session)
    self.account = repositories.AccountRepository(self._session)
    self.task = repositories.TaskRepository(self._session)

  async def __aexit__(
          self,
          exc_type: type[BaseException] | None,
          exc_val: BaseException | None,
          exc_tb: TracebackType | None,
  ) -> None:
    await self._session.flush()


class FakeBaseService(BaseService):
  """Create fake base service"""

  def __init__(self, session: AsyncSession) -> None:
    super().__init__()
    self.uow = FakeUnitOfWork(session)


class FakeMemberService(FakeBaseService, MemberService):
  """Create fake member service"""


class FakeWorkDataService(FakeBaseService, WorkDataService):
  """Create fake work data service"""


class FakeCompanyRegService(FakeBaseService, CompanyRegService):
  """Create fake company registration service"""


class FakeTasksService(FakeBaseService, TasksService):
  """Create fake tasks service"""


class FakeWorkStructureService(FakeBaseService, WorkStructureService):
  """Create fake work structure service"""
