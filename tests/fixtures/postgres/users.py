from uuid import UUID

from src.schemas.user_schema import TestUserSchema

FAKE_USERS: list[TestUserSchema] = [
    TestUserSchema(
        first_name="Ivan",
        last_name="Ivanov",
        id=UUID("0a11b269-d752-43e3-a836-1b7b8d8a78c3"),
        is_active=True,
        is_admin=False,
    ),
    TestUserSchema(
        first_name="Petr",
        last_name="Petrov",
        id=UUID("e58196d8-82eb-4f18-8f64-9db0bdfaf3b7"),
        is_active=True,
        is_admin=False,
    ),
    TestUserSchema(
        first_name="Oleg",
        last_name="Olegov",
        id=UUID("0982d535-c313-4832-8855-8189f47ce06d"),
        is_active=True,
        is_admin=False,
    ),
    TestUserSchema(
        first_name="Nikita",
        last_name="Naumov",
        id=UUID("07cd5c88-214e-432b-8da0-9f840beca0aa"),
        is_active=True,
        is_admin=False,
    ),
    TestUserSchema(
        first_name="John",
        last_name="Travolta",
        id=UUID("fba99cad-8e39-4108-b692-ffe8ce3c5d70"),
        is_active=True,
        is_admin=True,
    ),
    TestUserSchema(
        first_name="Lev",
        last_name="Yashin",
        id=UUID("7a937595-1206-4dae-8934-56cf4f46e71e"),
        is_active=True,
        is_admin=False,
    ),
]
