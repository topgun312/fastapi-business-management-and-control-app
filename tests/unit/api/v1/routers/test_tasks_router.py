from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestTaskRouter:

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'task_id', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_TASK_ROUTE,
  )
  async def test_get_task(
          url: str,
          task_id: str,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
  ) -> None:
    with expectation:
      response = await async_client.get(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_ALL_TASKS_ROUTE,
  )
  async def test_get_all_tasks(
          url: str,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
  ) -> None:
    with expectation:
      response = await async_client.get(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_CREATE_TASK_ROUTE,
  )
  async def test_create_task(
          url: str,
          json: dict,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
  ) -> None:
    with expectation:
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'task_id', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_TASK_ROUTE,
  )
  async def test_update_task(
          url: str,
          task_id: str,
          json: dict,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
  ) -> None:
    with expectation:
      response = await async_client.put(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'task_id', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_TASK_ROUTE,
  )
  async def test_delete_task(
          url: str,
          task_id: str,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
  ) -> None:
    with expectation:
      response = await async_client.delete(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload
