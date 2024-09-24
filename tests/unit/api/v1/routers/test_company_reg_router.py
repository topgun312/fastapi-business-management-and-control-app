from typing import Any
import pytest
from httpx import AsyncClient
from tests import fixtures
from tests.conftest import auth_user_issue_jwt_test
from tests.utils import prepare_payload, list_prepare
from tests.unit.conftest import add_accounts, add_invites, add_users, clean_data, add_companies, add_secrets


class TestCompanyRegRouter:


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'account_email', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_CHECK_ACCOUNT_ROUTE,
  )
  async def test_check_account(
          url: str,
          account_email: str,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          add_accounts, add_invites, add_users, clean_data
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_invites()
      response = await async_client.get(url, params={'account_email': account_email}, headers=headers)
      assert response.status_code == expected_status_code
      assert response.json() == expected_payload


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_SIGN_UP_ROUTE,
  )
  async def test_sign_up(
          url: str,
          json: dict,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          add_accounts, add_invites, add_users, clean_data
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_invites()
      response = await async_client.get(url, params=json, headers=headers)
      assert response.status_code == expected_status_code
      assert response.json() == expected_payload


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_SIGN_UP_COMPLETE_ROUTE,
  )
  async def test_sign_up_complete(
          url: str,
          json: dict,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          add_accounts, clean_data, add_users
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id', 'created_at', 'updated_at']) == expected_payload


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'company_id', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_COMPANY_BY_ID_ROUTE,
  )
  async def test_get_company_by_id(
          url: str,
          company_id: str,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test, clean_data, add_users, add_secrets,
          add_companies, add_accounts) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.get(url, headers=headers
      )
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id', 'created_at', 'updated_at']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_ALL_COMPANIES_ROUTE,
  )
  async def test_get_all_companies(
          url: str,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test, clean_data, add_users, add_secrets,
          add_companies, add_accounts
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.get(url, headers=headers)
      assert response.status_code == expected_status_code
      assert list_prepare(response, ['id', 'created_at', 'updated_at']) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'company_id', 'json', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_COMPANY_BY_ID_ROUTE,
  )
  async def test_update_company_by_id(
          url: str,
          company_id: str,
          json: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
          user_test, clean_data, add_users, add_secrets,
          add_companies, add_accounts
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.put(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response, ['id', 'created_at', 'updated_at']) == expected_payload


  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'company_id', 'expected_status_code', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_COMPANY_BY_ID_ROUTE,
  )
  async def test_delete_company_by_id(
          url: str,
          company_id: str,
          expected_status_code: int,
          expectation: Any,
          async_client: AsyncClient,
          user_test, clean_data, add_users, add_secrets,
          add_companies, add_accounts
  ) -> None:
    with expectation:
      await clean_data()
      await add_users()
      await add_accounts()
      await add_secrets()
      await add_companies()
      headers = await auth_user_issue_jwt_test(async_client, user_test)
      response = await async_client.delete(url, headers=headers)
      assert response.status_code == expected_status_code

