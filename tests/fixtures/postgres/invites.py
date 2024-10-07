from uuid import UUID

from src.schemas.invite_schema import TestInviteSchema

FAKE_INVITES: list[TestInviteSchema] = [
    TestInviteSchema(
        id=UUID("a8a47b57-43ad-4797-9378-7e099d8585e4"),
        code=4433,
        account_id=UUID("4311b77d-11bf-45ab-bbaf-a153ccab56bc"),
    ),
    TestInviteSchema(
        id=UUID("0e39d05d-1a03-42a8-b4a6-9387eff8ff74"),
        code=3322,
        account_id=UUID("ea1112ab-32b0-4737-84e3-fd272d1613dd"),
    ),
    TestInviteSchema(
        id=UUID("819700e7-575d-431c-9ef9-038a6ffeb644"),
        code=1234,
        account_id=UUID("958b4855-5953-44a5-ad82-27c6a034d772"),
    ),
    TestInviteSchema(
        id=UUID("cc75940e-76c1-4c29-8f63-a5d2dd425fc9"),
        code=4321,
        account_id=UUID("5cdd0e9c-4ea2-429b-b108-b39eea7f3b77"),
    ),
    TestInviteSchema(
        id=UUID("c099bba5-acfb-4a1e-a2a9-1c26e83b33e0"),
        code=9999,
        account_id=UUID("060a0348-cafc-4f14-84ca-7172c9b84982"),
    ),
]
