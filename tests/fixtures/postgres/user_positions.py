from uuid import UUID

from src.schemas.user_position_schema import TestUserPositionSchema

FAKE_USER_POSITIONS: list[TestUserPositionSchema] = [
    TestUserPositionSchema(
        id=UUID("30d0cb99-e02e-488b-bc31-a7b9b0ccad35"),
        user_id=[UUID("0a11b269-d752-43e3-a836-1b7b8d8a78c3")],
        position_id=1,
    ),
    TestUserPositionSchema(
        id=UUID("ef3f79f5-04b1-4ace-9fd1-45d3bdd57c1e"),
        user_id=[UUID("e58196d8-82eb-4f18-8f64-9db0bdfaf3b7")],
        position_id=2,
    ),
    TestUserPositionSchema(
        id=UUID("eed1178a-b3b2-41ed-8950-1b1da97bb9f9"),
        user_id=[UUID("0982d535-c313-4832-8855-8189f47ce06d")],
        position_id=3,
    ),
    TestUserPositionSchema(
        id=UUID("515044f2-a3c8-4351-961b-be9624496f43"),
        user_id=[UUID("07cd5c88-214e-432b-8da0-9f840beca0aa")],
        position_id=4,
    ),
]
