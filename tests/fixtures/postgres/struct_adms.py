from uuid import UUID

from schemas.struct_adm_schema import TestStructAdmSchema

FAKE_STRUCT_ADMS: list[TestStructAdmSchema] = [
    TestStructAdmSchema(
        id=3,
        name="Aircraft_products",
        path="Aircraft_products",
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        head_user_id=UUID("fba99cad-8e39-4108-b692-ffe8ce3c5d70"),
    ),
    TestStructAdmSchema(
        id=4,
        name="Sale_department",
        path="Aircraft_products.Sale_department",
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        head_user_id=UUID("e58196d8-82eb-4f18-8f64-9db0bdfaf3b7"),
    ),
    TestStructAdmSchema(
        id=5,
        name="Repair_department",
        path="Aircraft_products.Repair_department",
        company_id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        head_user_id=None,
    ),
]
