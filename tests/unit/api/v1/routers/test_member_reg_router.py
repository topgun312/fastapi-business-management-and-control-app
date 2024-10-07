from typing import Any

import pytest
from httpx import AsyncClient

from tests import fixtures
from tests.conftest import auth_user_issue_jwt_test
from tests.utils import prepare_payload, prepare_without_payload


class TestMemberRegRoute:

    @staticmethod
    @pytest.mark.parametrize(
        ("url", "json", "expected_status_code", "expected_payload", "expectation"),
        fixtures.test_cases.PARAMS_TEST_ADD_MEMBER_TO_COMPANY_ROUTE,
    )
    async def test_add_member_to_company(
        url: str,
        json: dict,
        expected_status_code: int,
        expected_payload: dict,
        expectation: Any,
        async_client: AsyncClient,
        user_test,
        clean_data,
        add_users,
        add_accounts,
        add_companies,
        add_secrets,
    ) -> None:
        with expectation:
            await clean_data()
            await add_users()
            await add_accounts()
            await add_secrets()
            await add_companies()
            headers = await auth_user_issue_jwt_test(async_client, user_test)
            response = await async_client.post(url, json=json, headers=headers)
            assert response.status_code == expected_status_code
            assert prepare_without_payload(response) == expected_payload

    @staticmethod
    @pytest.mark.parametrize(
        ("url", "json", "expected_status_code", "expected_payload", "expectation"),
        fixtures.test_cases.PARAMS_TEST_ADD_PASSWORD_AND_END_REGISTRATION_ROUTE,
    )
    async def test_add_password_and_end_registration(
        url: str,
        json: dict,
        expected_status_code: int,
        expected_payload: dict,
        expectation: Any,
        async_client: AsyncClient,
        user_test,
        clean_data,
        add_users,
        add_accounts,
        add_members,
        add_companies,
        add_secrets,
        add_invites,
    ) -> None:
        with expectation:
            await clean_data()
            await add_users()
            await add_accounts()
            await add_invites()
            await add_secrets()
            await add_companies()
            await add_members()
            headers = await auth_user_issue_jwt_test(async_client, user_test)
            response = await async_client.post(url, json=json, headers=headers)
            assert response.status_code == expected_status_code
            assert (
                prepare_payload(response, ["id", "registered_at", "updated_at"])
                == expected_payload
            )

    @staticmethod
    @pytest.mark.parametrize(
        ("url", "user_id", "expected_status_code", "expected_payload", "expectation"),
        fixtures.test_cases.PARAMS_TEST_GET_MEMBER_INFO_BY_USER_ID_ROUTE,
    )
    async def test_get_member_info_by_user_id(
        url: str,
        user_id: str,
        expected_status_code: int,
        expected_payload: dict,
        expectation: Any,
        async_client: AsyncClient,
        user_test,
        clean_data,
        add_users,
        add_accounts,
        add_members,
        add_companies,
        add_secrets,
        add_invites,
    ) -> None:
        with expectation:
            await clean_data()
            await add_users()
            await add_accounts()
            await add_invites()
            await add_secrets()
            await add_companies()
            await add_members()
            headers = await auth_user_issue_jwt_test(async_client, user_test)
            response = await async_client.get(
                url, params={"user_id": user_id}, headers=headers
            )
            assert response.status_code == expected_status_code
            assert (
                prepare_payload(response, ["id", "registered_at", "updated_at"])
                == expected_payload
            )
