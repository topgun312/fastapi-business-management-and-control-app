import asyncio
from collections.abc import AsyncGenerator, Generator

import pytest
import pytest_asyncio
import sqlalchemy.schema
from config import settings
from httpx import AsyncClient
from models.base_model import BaseModel
from sqlalchemy import Result, sql
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from src.api.structure.v1.service import WorkStructureService
from src.api.tasks.v1.service import TasksService
from src.api.users.v1.service import CompanyRegService, MemberService, WorkDataService
from src.main import app
from tests.fixtures import (
  FakeCompanyRegService,
  FakeMemberService,
  FakeTasksService,
  FakeWorkDataService,
  FakeWorkStructureService,
)


@pytest.fixture(scope='session')
def event_loop(request: pytest.FixtureRequest) -> asyncio.AbstractEventLoop:
  """Return a new event_loop
  """
  loop = asyncio.get_event_loop_policy().new_event_loop()
  yield loop
  loop.close()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def create_test_db(event_loop: None) -> None:
  """Create a test database for the duration of the test
  """
  assert settings.MODE == 'TEST'

  sqlalchemy_database_url = (
    f'postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}'
    f'@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'
  )
  nodb_engine = create_async_engine(
    url=sqlalchemy_database_url,
    echo=False,
    future=True,
  )
  db = AsyncSession(bind=nodb_engine)

  db_exists_query = sql.text(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{settings.DB_NAME}'")
  db_exists: Result = await db.execute(db_exists_query)
  db_exists = db_exists.fetchone() is not None
  autocommit_engine = nodb_engine.execution_options(isolation_level='AUTOCOMMIT')
  connection = await autocommit_engine.connect()
  if not db_exists:
    db_create_query = sql.text(f'CREATE DATABASE {settings.DB_NAME}')
    print('ss', db_create_query)
    await connection.execute(db_create_query)

  yield

  db_drop_query = sql.text(f'DROP DATABASE IF EXISTS {settings.DB_NAME} WITH (FORCE)')
  await db.close()
  await connection.execute(db_drop_query)
  await connection.close()
  await nodb_engine.dispose()


@pytest_asyncio.fixture(scope='session')
async def db_engine(create_test_db: None) -> AsyncGenerator[AsyncEngine, None]:
  """Return the test Engine"""
  engine = create_async_engine(
    settings.DB_URL,
    echo=False,
    future=True,
    pool_size=50,
    max_overflow=100,
  ).execution_options(compiled_cache=None)

  yield engine
  await engine.dispose()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_schemas(db_engine: AsyncEngine) -> None:
  """Create schemas in the test database"""
  assert settings.MODE == 'TEST'

  schemas = (
    'schema_for_example'
  )

  async with db_engine.connect() as conn:
    for schema in schemas:
      await conn.execute(sqlalchemy.schema.CreateSchema(schema))
      await conn.commit()


@pytest_asyncio.fixture(scope='session', autouse=True)
async def setup_db(db_engine: AsyncEngine, setup_schemas: None) -> None:
  """Create tables in the test database and insert needs data"""
  assert settings.MODE == 'TEST'

  async with db_engine.begin() as db_conn:
    await db_conn.run_sync(BaseModel.metadata.drop_all)
    await db_conn.run_sync(BaseModel.metadata.create_all)


@pytest_asyncio.fixture
async def transaction_session(db_engine: AsyncEngine) -> AsyncGenerator[AsyncSession, None]:
  """Return a connection to the database.
  Any changes made to the database will NOT be applied, only for the duration of the TestCase.
  """
  connection = await db_engine.connect()
  await connection.begin()
  session = AsyncSession(bind=connection)

  yield session

  await session.rollback()
  await connection.close()


@pytest_asyncio.fixture
def fake_work_structure_service(transaction_session: AsyncSession) -> Generator[FakeWorkStructureService, None]:
  """Create fake work structure service"""
  _fake_work_structure_service = FakeWorkStructureService(transaction_session)
  yield _fake_work_structure_service


@pytest_asyncio.fixture
def fake_tasks_service(transaction_session: AsyncSession) -> Generator[FakeTasksService, None]:
    """Create fake tasks service"""
    _fake_tasks_service = FakeTasksService(transaction_session)
    yield _fake_tasks_service


@pytest_asyncio.fixture
def fake_company_reg_service(transaction_session: AsyncSession) -> Generator[FakeCompanyRegService, None]:
  """Create fake company registration service"""
  _fake_company_reg_service = FakeCompanyRegService(transaction_session)
  yield _fake_company_reg_service


@pytest_asyncio.fixture
def fake_member_service(transaction_session: AsyncSession) -> Generator[FakeMemberService, None]:
  """Create fake member service"""
  _fake_member_service = FakeMemberService(transaction_session)
  yield _fake_member_service


@pytest_asyncio.fixture
def fake_work_data_service(transaction_session: AsyncSession) -> Generator[FakeWorkDataService, None]:
  """Create fake work data service"""
  _fake_work_data_service = FakeWorkDataService(transaction_session)
  yield _fake_work_data_service


@pytest_asyncio.fixture
async def async_client(
        fake_member_service: FakeMemberService,
        fake_tasks_service: FakeTasksService,
        fake_company_reg_service: FakeCompanyRegService,
        fake_work_data_service: FakeWorkDataService,
        fake_work_structure_service: FakeWorkStructureService,
) -> AsyncGenerator[AsyncClient, None]:
  """Create async client"""
  app.dependency_overrides[MemberService] = lambda: fake_member_service
  app.dependency_overrides[TasksService] = lambda: fake_tasks_service
  app.dependency_overrides[CompanyRegService] = lambda: fake_company_reg_service
  app.dependency_overrides[WorkDataService] = lambda: fake_work_data_service
  app.dependency_overrides[WorkStructureService] = lambda: fake_work_structure_service
  async with AsyncClient(app=app, base_url='http://test') as ac:
    yield ac
