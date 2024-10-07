from uuid import UUID

from src.schemas.account_schema import TestAccountSchema

FAKE_ACCOUNTS: list[TestAccountSchema] = [
    TestAccountSchema(
        email="ivan@example.com",
        id=UUID("4311b77d-11bf-45ab-bbaf-a153ccab56bc"),
        user_id=UUID("0a11b269-d752-43e3-a836-1b7b8d8a78c3"),
    ),
    TestAccountSchema(
        email="petr@example.com",
        id=UUID("ea1112ab-32b0-4737-84e3-fd272d1613dd"),
        user_id=UUID("e58196d8-82eb-4f18-8f64-9db0bdfaf3b7"),
    ),
    TestAccountSchema(
        email="oleg@example.com",
        id=UUID("958b4855-5953-44a5-ad82-27c6a034d772"),
        user_id=UUID("0982d535-c313-4832-8855-8189f47ce06d"),
    ),
    TestAccountSchema(
        email="nikita@example.com",
        id=UUID("5cdd0e9c-4ea2-429b-b108-b39eea7f3b77"),
        user_id=UUID("07cd5c88-214e-432b-8da0-9f840beca0aa"),
    ),
    TestAccountSchema(
        email="andrey@example.com",
        id=UUID("bf5d5543-7e8b-4ae1-a02e-be20d53e363a"),
        user_id=None,
    ),
    TestAccountSchema(
        email="john@example.com",
        id=UUID("c5560d18-9ff9-44be-b1eb-62794b7f9d69"),
        user_id=UUID("fba99cad-8e39-4108-b692-ffe8ce3c5d70"),
    ),
    TestAccountSchema(
        email="lev@example.com",
        id=UUID("060a0348-cafc-4f14-84ca-7172c9b84982"),
        user_id=UUID("7a937595-1206-4dae-8934-56cf4f46e71e"),
    ),
]
