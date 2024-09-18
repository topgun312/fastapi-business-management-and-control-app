from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.utils import prepare_payload


class TestMemberRegRoute:

    @staticmethod
    @pytest.mark.parametrize(
      ('url', 'json', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
      fixtures.test_cases.PARAMS_TEST_ADD_MEMBER_TO_COMPANY_ROUTE,
    )
    async def test_add_member_to_company(
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
      ('url', 'invite_code', 'password', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
      fixtures.test_cases.PARAMS_TEST_ADD_PASSWORD_AND_END_REGISTRATION_ROUTE,
    )
    async def test_add_password_and_end_registration(
            url: str,
            invite_code: int,
            password: bytes,
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
      ('url', 'user_id', 'headers', 'expected_status_code', 'expected_payload', 'expectation'),
      fixtures.test_cases.PARAMS_TEST_GET_MEMBER_INFO_BY_USER_ID_ROUTE,
    )
    async def test_get_member_info_by_user_id(
            url: str,
            user_id: str,
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
      fixtures.test_cases.PARAMS_TEST_GET_ALL_USERS_INFO_ROUTE,
    )
    async def test_get_all_members_info(
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
