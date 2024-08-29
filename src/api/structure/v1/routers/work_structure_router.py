

from fastapi import APIRouter


router = APIRouter(prefix="/structure", tags=["Work Structure"])

#     • Создание подразделений вложенной структуры (ltree postgres)
@router.post("/create_divisions")
async def create_divisions_of_nested_structure():
  pass

#     • Создание должностей
@router.post("/create_posts")
async def create_posts():
  pass

#     • Привязка должностей к сотрудникам и подразделениям
@router.put("/linking_positions")
async def linking_positions_employees_and_departments():
  pass

#     • Назначение руководителей подразделений
@router.put("/appointment_heads")
async def appointment_heads_of_departments():
  pass


#     • Удаление подразделений, должностей
@router.delete("/delete_dep_and_pos")
async def deleting_departments_and_positions():
  pass


#     • Редактирование подразделений, должностей
@router.put("/edit_dep_and_pos")
async def editing_departments_and_positions():
  pass