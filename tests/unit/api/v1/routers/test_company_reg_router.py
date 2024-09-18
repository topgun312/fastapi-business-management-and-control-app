from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestTaskRouter:

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
  ) -> None:
    with expectation:
      response = await async_client.get(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'account', 'invite_code', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_SIGN_UP_ROUTE,
  )
  async def test_sign_up(
          url: str,
          account: str,
          invite_code: int,
          headers: dict,
          expected_status_code: int,
          expected_payload: dict,
          expectation: Any,
          async_client: AsyncClient,
  ) -> None:
    with expectation:
      response = await async_client.post(url, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

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
  ) -> None:
    with expectation:
      response = await async_client.post(url, json=json, headers=headers)
      assert response.status_code == expected_status_code
      assert prepare_payload(response) == expected_payload

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'company_id', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_GET_COMPANY_BY_ID_ROUTE,
  )
  async def test_get_company_by_id(
          url: str,
          company_id: str,
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
  fixtures.test_cases.PARAMS_TEST_GET_ALL_COMPANIES_ROUTE,
  )
  async def test_get_all_companies(
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
  ('url', 'company_id', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_COMPANY_BY_ID_ROUTE,
  )
  async def test_update_company_by_id(
          url: str,
          company_id: str,
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
  ('url', 'company_id', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_DELETE_COMPANY_BY_ID_ROUTE,
  )
  async def delete_company_by_id(
          url: str,
          company_id: str,
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
