from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestWorkDataRouter:

  @staticmethod
  @pytest.mark.parametrize(
  ('url', 'email', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_ACCOUNT_EMAIL_ROUTE,
  )
  async def test_update_account_email(
          url: str,
          email: str,
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
  ('url', 'first_name', 'last_name', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
  fixtures.test_cases.PARAMS_TEST_UPDATE_USER_FIRST_AND_LAST_NAME_ROUTE,
  )
  async def test_update_user_first_and_last_name(
          url: str,
          first_name: str,
          last_name: str,
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