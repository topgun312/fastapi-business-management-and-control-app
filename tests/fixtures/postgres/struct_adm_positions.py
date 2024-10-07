from uuid import UUID

from src.schemas.struct_adm_position_schema import TestStructAdmPositionSchema

FAKE_STRUCT_ADM_POSITIONS: list[TestStructAdmPositionSchema] = [
    TestStructAdmPositionSchema(
        id=UUID("88bc79ef-5818-4866-9091-12bf678f2828"),
        struct_adm_id=3,
        position_id=1,
    ),
    TestStructAdmPositionSchema(
        id=UUID("33f08fa2-2d7c-4880-819d-abc50600d0f9"),
        struct_adm_id=3,
        position_id=2,
    ),
    TestStructAdmPositionSchema(
        id=UUID("b7aaee1e-431d-4970-b4e1-d143aa26fb7e"),
        struct_adm_id=3,
        position_id=3,
    ),
    TestStructAdmPositionSchema(
        id=UUID("a2d93dec-772b-41f7-8a57-43b2d69abf7d"),
        struct_adm_id=4,
        position_id=1,
    ),
    TestStructAdmPositionSchema(
        id=UUID("39c750bf-90b7-4ebd-88f3-e26b9c008e0e"),
        struct_adm_id=4,
        position_id=2,
    ),
    TestStructAdmPositionSchema(
        id=UUID("e889b815-d856-4d98-ace4-1b735b904f27"),
        struct_adm_id=4,
        position_id=3,
    ),
]
