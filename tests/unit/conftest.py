from copy import deepcopy
from typing import Callable
import pytest
from sqlalchemy import  delete, insert
from sqlalchemy_utils import Ltree


from src.models import (
  AccountModel,
  StructAdmModel,
  StructAdmPositionModel,
  PositionModel,
  TaskModel,
  CompanyModel,
  MemberModel,
  InviteModel,
  UserPositionModel,
  User, SecretModel,
  performers_table,
  observers_table)

from src.schemas.user_schema import TestUserSchema
from src.schemas.invite_schema import TestInviteSchema
from src.schemas.account_schema import TestAccountSchema
from src.schemas.company_schema import TestCompanySchema
from src.schemas.task_schema import TestTaskSchema ,TestObserversSchema, TestPerformersSchema
from src.schemas.secret_schema import TestSecretSchema
from src.schemas.member_schema import TestMemberSchema
from src.schemas.user_position_schema import TestUserPositionSchema
from src.schemas.struct_adm_schema import TestStructAdmSchema
from src.schemas.struct_adm_position_schema import TestStructAdmPositionSchema
from src.schemas.position_schema import TestPositionSchema


from tests.fixtures.postgres import (
  FAKE_STRUCT_ADM_POSITIONS, FAKE_POSITIONS, FAKE_STRUCT_ADMS, FAKE_USER_POSITIONS,
  FAKE_MEMBERS, FAKE_SECRETS, FAKE_USERS, FAKE_TASKS, FAKE_ACCOUNTS, FAKE_INVITES, FAKE_COMPANIES,
  FAKE_OBSERVERS_TASKS, FAKE_PERFORMERS_TASKS

)


model_list = [
AccountModel,
  StructAdmModel,
  StructAdmPositionModel,
  PositionModel,
  TaskModel,
  CompanyModel,
  MemberModel,
  InviteModel,
  UserPositionModel,
  User, SecretModel
]


@pytest.fixture(scope="function")
def companies() -> list[TestCompanySchema]:
    return deepcopy(FAKE_COMPANIES)


@pytest.fixture(scope="function")
def users() -> list[TestUserSchema]:
    return deepcopy(FAKE_USERS)


@pytest.fixture(scope="function")
def struct_adms() -> list[TestStructAdmSchema]:
    return deepcopy(FAKE_STRUCT_ADMS)


@pytest.fixture(scope="function")
def struct_adm_positions() -> list[TestStructAdmPositionSchema]:
    return deepcopy(FAKE_STRUCT_ADM_POSITIONS)


@pytest.fixture(scope="function")
def invites() -> list[TestInviteSchema]:
    return deepcopy(FAKE_INVITES)


@pytest.fixture(scope="function")
def secrets() -> list[TestSecretSchema]:
    return deepcopy(FAKE_SECRETS)


@pytest.fixture(scope="function")
def members() -> list[TestMemberSchema]:
    return deepcopy(FAKE_MEMBERS)

@pytest.fixture(scope="function")
def tasks() -> list[TestTaskSchema]:
    return deepcopy(FAKE_TASKS)


@pytest.fixture(scope="function")
def observers() -> list[TestObserversSchema]:
    return deepcopy(FAKE_OBSERVERS_TASKS)


@pytest.fixture(scope="function")
def performers() -> list[TestPerformersSchema]:
    return deepcopy(FAKE_PERFORMERS_TASKS)


@pytest.fixture(scope="function")
def user_positions() -> list[TestUserPositionSchema]:
    return deepcopy(FAKE_USER_POSITIONS)


@pytest.fixture(scope="function")
def accounts() -> list[TestAccountSchema]:
    return deepcopy(FAKE_ACCOUNTS)

@pytest.fixture(scope="function")
def positions() -> list[TestPositionSchema]:
    return deepcopy(FAKE_POSITIONS)


@pytest.fixture(scope="function")
def add_companies(async_session_maker, companies) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in companies:
                await session.execute(
                    insert(CompanyModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_accounts(async_session_maker, accounts) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in accounts:
                await session.execute(
                    insert(AccountModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_invites(async_session_maker, invites) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in invites:
                await session.execute(
                    insert(InviteModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_members(async_session_maker, members) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in members:
                await session.execute(
                    insert(MemberModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_positions(async_session_maker, positions) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in positions:
                await session.execute(
                    insert(PositionModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results

@pytest.fixture(scope="function")
def add_secrets(async_session_maker, secrets) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in secrets:
                await session.execute(
                    insert(SecretModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_struct_adms(async_session_maker, struct_adms) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in struct_adms:
                await session.execute(
                    insert(StructAdmModel).values(path=Ltree(res_schema.path),
                                                  id=res_schema.id, name=res_schema.name,
                                                  company_id=res_schema.company_id, head_user_id=res_schema.head_user_id)
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_struct_adm_positions(async_session_maker, struct_adm_positions) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in struct_adm_positions:
                await session.execute(
                    insert(StructAdmPositionModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="function")
def add_tasks(async_session_maker, tasks) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in tasks:
                await session.execute(
                    insert(TaskModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results

@pytest.fixture(scope="function")
def add_observers(async_session_maker, observers) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in observers:
                await session.execute(
                    insert(observers_table).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results

@pytest.fixture(scope="function")
def add_performers(async_session_maker, performers) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in performers:
                await session.execute(
                    insert(performers_table).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results

@pytest.fixture(scope="function")
def add_users(async_session_maker, users) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in users:
                await session.execute(
                    insert(User).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results

@pytest.fixture(scope="function")
def add_user_positions(async_session_maker, user_positions) -> Callable:
    async def _add_results():
        async with async_session_maker() as session:
            for res_schema in user_positions:
                await session.execute(
                    insert(UserPositionModel).values(**res_schema.model_dump())
                )
            await session.commit()

    return _add_results


@pytest.fixture(scope="session")
def clean_data(async_session_maker) -> Callable:
    async def _clear_data():
        async with async_session_maker() as session:
            for model in model_list:
                query = delete(model)
                await session.execute(query)
            await session.commit()

    return _clear_data
