from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.conftest import auth_user_issue_jwt_test
from tests.utils import prepare_payload, list_prepare_payload


class TestTaskRouter:

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'task_id', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_TASK_ROUTE,
  )
  async def test_get_task(
          url: str,
          task_id: str,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, add_tasks, add_observers, add_performers
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_tasks()
      await add_performers()
      await add_observers()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.get(url, params={"task_id": task_id}, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['deadline']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_ALL_TASKS_ROUTE,
  )
  async def test_get_all_tasks(
          url: str,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, add_tasks,
          add_observers, add_performers
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_tasks()
      await add_performers()
      await add_observers()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.get(url, headers=headers)
      assert response.status_code == expected_status_code
      assert list_prepare_payload(response, ['deadline']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_CREATE_TASK_ROUTE,
  )
  async def test_create_task(
          url: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, add_tasks
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_tasks()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id', 'deadline']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'task_id', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_TASK_ROUTE,
  )
  async def test_update_task(
          url: str,
          task_id: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, add_tasks,
          add_observers, add_performers
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_tasks()
      await add_performers()
      await add_observers()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.put(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id', 'deadline']) == expected_payload


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'task_id', 'expected_status_code', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_TASK_ROUTE,
  )
  async def test_delete_task(
          url: str,
          task_id: str,
          expected_status_code: int,
          expectation: Any,
          async_client: AsyncClient,
          user_test,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, add_tasks,
          add_observers, add_performers
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_tasks()
      await add_performers()
      await add_observers()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.delete(url, headers=headers)
      assert response.status_code == expected_status_code

