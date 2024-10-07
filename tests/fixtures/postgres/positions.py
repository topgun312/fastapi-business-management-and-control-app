from src.schemas.position_schema import TestPositionSchema

FAKE_POSITIONS: list[TestPositionSchema] = [
    TestPositionSchema(
        id=1,
        name="Sales department head",
        description="Heads the sales department",
    ),
    TestPositionSchema(
        id=2,
        name="Sales manager",
        description="Helps customers choose a car and arrange a sale",
    ),
    TestPositionSchema(
        id=3,
        name="Junior sales manager",
        description="Helps the manager with the paperwork",
    ),
    TestPositionSchema(
        id=4,
        name="Repair department head",
        description="Heads the repair department",
    ),
    TestPositionSchema(
        id=5,
        name="Senior repairman",
        description="Repair of broken cars",
    ),
    TestPositionSchema(
        id=6,
        name="Junior repairman",
        description="Helps the senior repairman with the repair",
    ),
]
