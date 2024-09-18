from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestWorkStructureRouter:

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'company_name', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_CREATE_DEPARTMENT_ROUTE,
  )
  async def test_create_department(
          url: str,
          company_name: str,
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
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'struct_adm_name', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_DEPARTMENT_ROUTE,
  )
  async def test_update_department(
          url: str,
          struct_adm_name: str,
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
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'struct_adm_name', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_DEPARTMENT_ROUTE,
  )
  async def test_delete_department(
          url: str,
          struct_adm_name: str,
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

  @staticmethod
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_CREATE_POSITION_ROUTE,
  )
  async def test_create_position(
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
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'position_name', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_POSITION_ROUTE,
  )
  async def test_update_position(
          url: str,
          position_name: str,
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
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'position_name', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_POSITION_ROUTE,
  )
  async def test_delete_position(
          url: str,
          position_name: str,
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

  @staticmethod
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_ADD_USERS_TO_POSITION_ROUTE,
  )
  async def test_add_users_to_position(
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
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_ADD_POSITION_TO_DEPARTMENT_ROUTE,
  )
  async def test_add_position_to_department(
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
  @pytest.mark.usefixtures('')
  @pytest.mark.parametrize(
  ('url', 'user_id', 'struct_adm_name', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_ADD_DEPARTMENT_HEAD_ROUTE,
  )
  async def test_add_department_head(
          url: str,
          user_id: str,
          struct_adm_name: str,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,

  ) -> None:
    with expectation:
      response = await async_client.put(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload
