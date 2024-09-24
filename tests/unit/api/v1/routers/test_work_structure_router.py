from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.conftest import auth_user_issue_jwt_test
from tests.utils import prepare_payload, list_prepare, prepare_without_payload


class TestWorkStructureRouter:

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'company_name', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_CREATE_DEPARTMENT_ROUTE,
  )
  async def test_create_department(
          url: str,
          company_name: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, user_test, add_struct_adms
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_struct_adms()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'struct_adm_name', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_DEPARTMENT_ROUTE,
  )
  async def test_update_department(
          url: str,
          struct_adm_name: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, user_test, add_struct_adms
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_struct_adms()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.put(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'struct_adm_name', 'expected_status_code',  'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_DEPARTMENT_ROUTE,
  )
  async def test_delete_department(
          url: str,
          struct_adm_name: str,
          expected_status_code: int,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, user_test, add_struct_adms

  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_struct_adms()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.delete(url, headers=headers)
      assert response.status_code == expected_status_code


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_CREATE_POSITION_ROUTE,
  )
  async def test_create_position(
          url: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts,
          add_secrets, user_test
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_without_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'position_name', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_POSITION_ROUTE,
  )
  async def test_update_position(
          url: str,
          position_name: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts,
          add_secrets, user_test, add_positions
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_positions()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.put(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert response.json() == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'position_name',  'expected_status_code',  'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_POSITION_ROUTE,
  )
  async def test_delete_position(
          url: str,
          position_name: str,
          expected_status_code: int,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts,
          add_secrets, user_test, add_positions

  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_positions()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.delete(url, headers=headers)
      assert response.status_code == expected_status_code


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_ADD_USERS_TO_POSITION_ROUTE,
  )
  async def test_add_users_to_position(
          url: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts,
          add_secrets, user_test, add_positions

  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_positions()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert list_prepare(response, ['id']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_ADD_POSITION_TO_DEPARTMENT_ROUTE,
  )
  async def test_add_position_to_department(
          url: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, user_test, add_struct_adms,
          add_positions
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_struct_adms()
      await add_positions()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_without_payload(response, ['id']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'user_id', 'struct_adm_name', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_ADD_DEPARTMENT_HEAD_ROUTE,
  )
  async def test_add_department_head(
          url: str,
          user_id: str,
          struct_adm_name: str,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          clean_data, add_users, add_accounts, add_members,
          add_companies, add_secrets, user_test, add_struct_adms,
          add_positions
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      await add_members()
      await add_struct_adms()
      await add_positions()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.put(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_without_payload(response) == expected_payload
