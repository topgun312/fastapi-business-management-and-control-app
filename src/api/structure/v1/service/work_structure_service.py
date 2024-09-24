from collections.abc import Sequence
from typing import Any

from fastapi import HTTPException, status
from pydantic import UUID4
from sqlalchemy import Row
from sqlalchemy_utils import Ltree

from src.models import CompanyModel, PositionModel, StructAdmModel, StructAdmPositionModel, User, UserPositionModel
from src.schemas.position_schema import PositionDB
from src.schemas.struct_adm_position_schema import StructAdmPositionDB
from src.schemas.struct_adm_schema import StructAdmDB
from src.schemas.user_position_schema import UserPositionDB
from src.utils.service import BaseService
from src.utils.unit_of_work import transaction_mode


class WorkStructureService(BaseService):


  @transaction_mode
  async def create_department(self, company_name: str, struct_adm_data: dict) -> StructAdmDB:
      """Create department of company
      """
      struct_adm_name, struct_adm_parent = struct_adm_data['name'], struct_adm_data['parent']
      company: CompanyModel = await self.uow.company.get_by_query_one_or_none(name=company_name)
      self._check_company_exists(company=company)

      if struct_adm_name == company_name:
        self._incorrect_parent_or_name_exists_error()
      elif struct_adm_name == struct_adm_parent:
        try:
          struct_adm: StructAdmModel = await self.uow.struct_adm.add_one_and_get_obj(
            name=struct_adm_name,
            company_id=company.id,
            path=Ltree(struct_adm_parent),
          )
          return struct_adm.to_pydantic_schema()
        except Exception:
          self._incorrect_parent_or_name_exists_error()
      parent_struct_adm: Ltree | None = await self.uow.struct_adm.get_all_path_of_parent(struct_adm_parent)
      self._check_parent_struct_adm_exists(parent_struct_adm=parent_struct_adm)
      try:
        struct_adm: StructAdmModel = await self.uow.struct_adm.add_one_and_get_obj(
          name=struct_adm_name,
          company_id=company.id,
          path=Ltree(str(parent_struct_adm) + f'.{struct_adm_name}'),

        )
        return struct_adm.to_pydantic_schema()
      except Exception:
        self._incorrect_parent_or_name_exists_error()

  @transaction_mode
  async def update_department_by_name(self, struct_adm_name: str, department_data: dict) -> StructAdmDB:
    """Update department of company by name
    """
    children: Sequence[Row[tuple[Any, ...] | Any]] = await self.uow.struct_adm.get_children_paths(struct_adm_name=struct_adm_name)
    department: StructAdmModel = await self.uow.struct_adm.get_by_query_one_or_none(name=struct_adm_name)
    self._check_department_exists(department=department)
    path = str(department.path)
    dep_data_name = department_data['name']
    new_path = path.replace(f'{struct_adm_name}', f'{dep_data_name}')
    updated_department: StructAdmModel = await self.uow.struct_adm.update_one_by_name(_name=struct_adm_name, name=dep_data_name, path=Ltree(new_path))
    await self.uow.struct_adm.update_children_paths(children, dep_data_name)
    return updated_department.to_pydantic_schema()

  @transaction_mode
  async def delete_department_by_name(self, struct_adm_name: str) -> None:
    """Delete department of company by name
    """
    children: Sequence[Row[tuple[Any, ...] | Any]] = await self.uow.struct_adm.get_children_paths(struct_adm_name=struct_adm_name)
    department: StructAdmModel = await self.uow.struct_adm.get_by_query_one_or_none(name=struct_adm_name)
    self._check_department_exists(department=department)
    await self.uow.struct_adm.change_children_paths(children)
    await self.uow.struct_adm.delete_by_query(name=struct_adm_name)

  @transaction_mode
  async def create_position(self, position_data: dict) -> PositionDB:
    """Create position of department
    """
    position: PositionModel = await self.uow.position.get_by_query_one_or_none(name=position_data['name'])
    self._check_position_already_exists(position=position)
    created_position: PositionModel = await self.uow.position.add_one_and_get_obj(**position_data)
    return created_position.to_pydantic_schema()

  @transaction_mode
  async def update_position_by_name(self, position_name: str, position_data: dict) -> PositionDB:
    """Update position of department by name
    """
    position: PositionModel = await self.uow.position.get_by_query_one_or_none(name=position_name)
    self._check_position_exists(position=position)
    updated_position: PositionModel = await self.uow.position.update_one_by_name(_name=position_name, **position_data)
    return updated_position.to_pydantic_schema()

  @transaction_mode
  async def delete_position_by_name(self, position_name: str) -> None:
    """Delete position of department by name
    """
    position: PositionModel = await self.uow.position.get_by_query_one_or_none(name=position_name)
    self._check_position_exists(position=position)
    await self.uow.position.delete_by_query(name=position_name)

  @transaction_mode
  async def add_users_to_position(self, users_position_data: dict) -> list[UserPositionDB]:
    """Add users to position
    """
    position: PositionModel = await self.uow.position.get_by_query_one_or_none(id=users_position_data['position_id'])
    self._check_position_exists(position=position)
    users_position_list = []
    for user_id in users_position_data['user_id']:
      user: User = await self.uow.user.get_by_query_one_or_none(id=user_id)
      self._check_user_exists(user=user)
      user_position: UserPositionModel = await self.uow.user_position.add_one_and_get_obj(user_id=user_id,
                                                                       position_id=position.id)
      users_position_list.append(user_position.to_pydantic_schema())
    return users_position_list

  @transaction_mode
  async def add_position_to_department(self, struct_adm_pos_data: dict) -> StructAdmPositionDB:
    """Add position to department
    """
    struct_adm: StructAdmModel = await self.uow.struct_adm.get_by_query_one_or_none(id=struct_adm_pos_data['struct_adm_id'])
    self._check_department_exists(department=struct_adm)
    position: PositionModel = await self.uow.position.get_by_query_one_or_none(id=struct_adm_pos_data['position_id'])
    self._check_position_exists(position=position)
    struct_adm_pos: StructAdmPositionModel = await self.uow.struct_adm_position.add_one_and_get_obj(struct_adm_id=struct_adm.id,
                                                                            position_id=position.id)
    return struct_adm_pos.to_pydantic_schema()

  @transaction_mode
  async def add_department_head(self, user_id: UUID4, struct_adm_name: str) -> StructAdmDB:
    """Add department head
    """
    user: User = await self.uow.user.get_by_query_one_or_none(id=user_id)
    self._check_user_exists(user=user)
    struct_adm: StructAdmModel = await self.uow.struct_adm.get_by_query_one_or_none(name=struct_adm_name)
    self._check_department_exists(department=struct_adm)
    try:
      struct_adm_head: StructAdmModel = await self.uow.struct_adm.update_one_by_name(_name=struct_adm_name, head_user_id=user.id)
      return struct_adm_head.to_pydantic_schema()
    except Exception:
      self._incorrect_head_exists_error()

  @staticmethod
  def _check_company_exists(company: CompanyModel | None) -> None:
    if not company:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Company not found')

  @staticmethod
  def _incorrect_parent_or_name_exists_error() -> None:
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail='Incorrect parent or name already exists!',
      )

  @staticmethod
  def _incorrect_head_exists_error() -> None:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT, detail='The user is already the head of another department',
    )

  @staticmethod
  def _check_parent_struct_adm_exists(parent_struct_adm: Ltree | None) -> None:
    if not parent_struct_adm:
          raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Parent doesn't exists!",
          )

  @staticmethod
  def _check_department_exists(department: StructAdmModel | None) -> None:
    if not department:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Department not found',
      )

  @staticmethod
  def _check_position_already_exists(position: PositionModel | None) -> None:
    if position:
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT, detail='Position already exists!',
      )

  @staticmethod
  def _check_position_exists(position: PositionModel | None) -> None:
    if not position:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='Position not found!',
      )

  @staticmethod
  def _check_user_exists(user: User | None) -> None:
    if not user:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='User not found!',
      )
