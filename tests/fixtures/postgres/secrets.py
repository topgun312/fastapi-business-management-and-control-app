from uuid import UUID

from src.schemas.secret_schema import TestSecretSchema

FAKE_SECRETS: list[TestSecretSchema] = [
    TestSecretSchema(
        id=UUID("6b029418-cb57-48d1-9244-5ac1b7fef5bb"),
        password=b"$2b$12$i0heW6lJoavLo1Sqn/8SUe0euS/tstahCMjgtlaXVHrE5eY.PVi..",  # (qwerty)
        user_id=UUID("0a11b269-d752-43e3-a836-1b7b8d8a78c3"),
        account_id=UUID("4311b77d-11bf-45ab-bbaf-a153ccab56bc"),
    ),
    TestSecretSchema(
        id=UUID("31b2fbc4-0561-44d5-ab0c-dd7e2413362d"),
        password=b"$2b$12$2Z2xcfotuUW6pGwVoYD2S.RjXI1x5FAskWv7iB2dCqdSoZtyzQ/f2",  # (super)
        user_id=UUID("e58196d8-82eb-4f18-8f64-9db0bdfaf3b7"),
        account_id=UUID("ea1112ab-32b0-4737-84e3-fd272d1613dd"),
    ),
    TestSecretSchema(
        id=UUID("e63d94af-d979-4445-b694-b86a349b2b7c"),
        password=b"$2b$12$t4cQOcNEHPmAkRZeG/vDb.L0fKVvQofpufWXIuCYitPOYhFjIT4x2",  # (topgun)
        user_id=UUID("0982d535-c313-4832-8855-8189f47ce06d"),
        account_id=UUID("958b4855-5953-44a5-ad82-27c6a034d772"),
    ),
    TestSecretSchema(
        id=UUID("110d12c8-c956-4e3e-b9c9-9ec218f5bb81"),
        password=b"$2b$12$DiRFQCxvocFHAodCGkvyqe3NbymOHpPWaw/1AzYc7QYajqEExjLWm",  # (nikita)
        user_id=UUID("07cd5c88-214e-432b-8da0-9f840beca0aa"),
        account_id=UUID("5cdd0e9c-4ea2-429b-b108-b39eea7f3b77"),
    ),
    TestSecretSchema(
        id=UUID("34186616-7bcd-4966-9d14-9f633439a082"),
        password=b"$2b$12$aMboy6/TH5kOVfZfoJyH9.sf1/KkdXiK2tJgMwe5oCHdgDDgyyeKW",  # (bumer)
        user_id=UUID("fba99cad-8e39-4108-b692-ffe8ce3c5d70"),
        account_id=UUID("c5560d18-9ff9-44be-b1eb-62794b7f9d69"),
    ),
]
