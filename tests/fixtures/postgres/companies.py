from uuid import UUID

from src.schemas.company_schema import TestCompanySchema

FAKE_COMPANIES: list[TestCompanySchema] = [
    TestCompanySchema(
        name="Supercars_company",
        address="Moscow, Lenina 23",
        description="The company is engaged in the sale and rental of supercars",
        website="www.moscowsc.com",
        id=UUID("fa6ce865-fb2f-4d8a-b80f-fdbd121ff095"),
        account_id=UUID("4311b77d-11bf-45ab-bbaf-a153ccab56bc"),
    ),
    TestCompanySchema(
        name="Football_products",
        address="Moscow, Mira 44",
        description="The company is engaged in the sale of goods for football",
        website="www.moscowfootball.com",
        id=UUID("8e7c67ac-a027-4dc4-a418-e469c3d9a7ce"),
        account_id=UUID("5cdd0e9c-4ea2-429b-b108-b39eea7f3b77"),
    ),
    TestCompanySchema(
        name="Aircraft_products",
        address="Moscow, Gagarina 3",
        description="The company is engaged in the sale and rental of aircraft",
        website="www.moscowavia.com",
        id=UUID("07d3f795-0a6b-42af-866b-7cb517cd129a"),
        account_id=UUID("c5560d18-9ff9-44be-b1eb-62794b7f9d69"),
    ),
]
