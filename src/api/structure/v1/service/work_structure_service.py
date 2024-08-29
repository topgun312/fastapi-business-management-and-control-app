from fastapi import HTTPException
from utils.service import BaseService
from utils.unit_of_work import UnitOfWork


class WorkStructureService(BaseService):
  struct_adm_repository: str = "struct_adm"
  position_repository: str = "position"
  struct_adm_positions_repository: str = "struct_adm_positions"
  member_repository: str = "member"
  user_position_repository: str = "user_position"
  company_repository: str = "company"

  @classmethod
  async def create_head_company_division(cls, uow: UnitOfWork, company_name: str):
    async with uow:
      company = await uow.__dict__[cls.company_repository].get_by_one_or_none(name=company_name)
      if not company:
        raise HTTPException(status_code=404, detail="Company not found")
      await uow.__dict__[cls.struct_adm_repository].add_one(company)

  #     • Создание подразделений вложенной структуры (ltree postgres)

  @classmethod
  async def create_divisions(cls, uow: UnitOfWork, division_name: str):
    async with uow:
      company = await uow.__dict__[cls.struct_adm_repository].get_by_one_or_none(name=division_name)
      if not company:
        raise HTTPException(status_code=404, detail="Company not found")



