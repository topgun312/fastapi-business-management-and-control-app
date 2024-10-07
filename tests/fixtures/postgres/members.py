from uuid import UUID

from src.schemas.member_schema import TestMemberSchema

FAKE_MEMBERS: list[TestMemberSchema] = [
    TestMemberSchema(
        user_id=UUID("0982d535-c313-4832-8855-8189f47ce06d"),
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        id=UUID("6e949c9b-549e-4c5a-a062-601ec80e2692"),
    ),
    TestMemberSchema(
        user_id=UUID("e58196d8-82eb-4f18-8f64-9db0bdfaf3b7"),
        company_id=UUID("fa6ce865-fb2f-4d8a-b80f-fdbd121ff095"),
        id=UUID("8d6192eb-489f-44f7-9d63-86aebe8ef430"),
    ),
    TestMemberSchema(
        user_id=UUID("0a11b269-d752-43e3-a836-1b7b8d8a78c3"),
        company_id=UUID("fa6ce865-fb2f-4d8a-b80f-fdbd121ff095"),
        id=UUID("55f45683-5d5a-4b16-88ba-ea5163a84429"),
    ),
    TestMemberSchema(
        user_id=UUID("07cd5c88-214e-432b-8da0-9f840beca0aa"),
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        id=UUID("e6627a72-9d7f-48ae-80ea-b661d294c6c2"),
    ),
    TestMemberSchema(
        user_id=UUID("7a937595-1206-4dae-8934-56cf4f46e71e"),
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        id=UUID("4d98bde4-b2d5-454c-8fee-e4fd9da627a4"),
    ),
    TestMemberSchema(
        user_id=UUID("fba99cad-8e39-4108-b692-ffe8ce3c5d70"),
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        id=UUID("ae888cca-2dc1-4af9-997f-28ff5975f7be"),
    ),
]
