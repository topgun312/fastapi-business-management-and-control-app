from collections.abc import Sequence
from copy import deepcopy

import pytest
import pytest_asyncio
from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import (
  AccountModel,
  CompanyModel,
  InviteModel,
  MemberModel,
  PositionModel,
  SecretModel,
  StructAdmModel,
  StructAdmPositionModel,
  TaskModel,
  User,
  UserPositionModel,
)
from src.utils.unit_of_work import AsyncFunc
from tests import fixtures
from tests.utils import bulk_save_models


@pytest_asyncio.fixture
async def setup_companies(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, CompanyModel, companies)


@pytest_asyncio.fixture
async def setup_users(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, User, companies)


@pytest_asyncio.fixture
async def setup_accounts(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, AccountModel, companies)


@pytest_asyncio.fixture
async def setup_struct_adms(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, StructAdmModel, companies)


@pytest_asyncio.fixture
async def setup_struct_adm_positions(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, StructAdmPositionModel, companies)


@pytest_asyncio.fixture
async def setup_tasks(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, TaskModel, companies)


@pytest_asyncio.fixture
async def setup_secrets(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, SecretModel, companies)


@pytest_asyncio.fixture
async def setup_positions(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, PositionModel, companies)


@pytest_asyncio.fixture
async def setup_user_positions(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, UserPositionModel, companies)


@pytest_asyncio.fixture
async def setup_invites(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, InviteModel, companies)


@pytest_asyncio.fixture
async def setup_members(transaction_session: AsyncSession, companies: tuple[dict]) -> None:
  await bulk_save_models(transaction_session, MemberModel, companies)


@pytest_asyncio.fixture
def get_users(transaction_session: AsyncSession) -> AsyncFunc:
    """..."""
    async def _get_users() -> Sequence[User]:
        res: Result = await transaction_session.execute(select(User))
        return res.scalars().all()
    return _get_users


@pytest.fixture
def companies() -> tuple[dict]:
    return deepcopy(fixtures.postgres.COMPANIES)


@pytest.fixture
def users() -> tuple[dict]:
    return deepcopy(fixtures.postgres.USERS)


@pytest.fixture
def struct_adms() -> tuple[dict]:
    return deepcopy(fixtures.postgres.STRUCT_ADMS)


@pytest.fixture
def struct_adm_positions() -> tuple[dict]:
    return deepcopy(fixtures.postgres.STRUCT_ADM_POSITIONS)


@pytest.fixture
def invites() -> tuple[dict]:
    return deepcopy(fixtures.postgres.INVITES)


@pytest.fixture
def secrets() -> tuple[dict]:
    return deepcopy(fixtures.postgres.SECRETS)


@pytest.fixture
def members() -> tuple[dict]:
    return deepcopy(fixtures.postgres.MEMBERS)


@pytest.fixture
def tasks() -> tuple[dict]:
    return deepcopy(fixtures.postgres.TASKS)


@pytest.fixture
def user_positions() -> tuple[dict]:
    return deepcopy(fixtures.postgres.USER_POSITIONS)


@pytest.fixture
def accounts() -> tuple[dict]:
    return deepcopy(fixtures.postgres.ACCOUNTS)


@pytest.fixture
def first_user() -> dict:
    return deepcopy(fixtures.postgres.USERS[0])
