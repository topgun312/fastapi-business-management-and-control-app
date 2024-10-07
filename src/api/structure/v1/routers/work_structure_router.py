from fastapi import APIRouter, Depends, status
from pydantic import UUID4

from src.api.structure.v1.service.work_structure_service import WorkStructureService
from src.api.users.v1.auth_utils.validate import get_current_admin_auth_user
from src.schemas.position_schema import (
    CreatePositionRequest,
    PositionDB,
    UpdatePositionRequestByName,
)
from src.schemas.struct_adm_position_schema import (
    CreateStructAdmPositionRequest,
    StructAdmPositionDB,
)
from src.schemas.struct_adm_schema import (
    CreateStructAdmRequest,
    StructAdmCreateResponse,
    StructAdmDB,
    StructAdmResponse,
    UpdateStructAdmRequestByName,
)
from src.schemas.user_position_schema import CreateUserPositionRequest, UserPositionDB
from src.schemas.user_schema import UserAuthSchema

router = APIRouter(prefix="/structure", tags=["Work Structure"])


@router.post("/create_department/{company_name}", status_code=status.HTTP_201_CREATED)
async def create_department(
    company_name: str,
    struct_adm_data: CreateStructAdmRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> StructAdmCreateResponse:
    """Create department of company"""
    if admin:
        new_struct_adm: StructAdmDB = await service.create_department(
            company_name=company_name, struct_adm_data=struct_adm_data.model_dump()
        )
        return StructAdmCreateResponse(payload=new_struct_adm)


@router.put("/update_department/{struct_adm_name}", status_code=status.HTTP_200_OK)
async def update_department(
    struct_adm_name: str,
    department_data: UpdateStructAdmRequestByName,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> StructAdmResponse:
    """Update department of company by name"""
    if admin:
        updated_department: StructAdmDB = await service.update_department_by_name(
            struct_adm_name=struct_adm_name,
            department_data=department_data.model_dump(),
        )
        return StructAdmResponse(payload=updated_department)


@router.delete(
    "/delete_department/{struct_adm_name}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_department(
    struct_adm_name: str,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> None:
    """Delete department of company by name"""
    if admin:
        await service.delete_department_by_name(struct_adm_name=struct_adm_name)


@router.post("/create_position", status_code=status.HTTP_201_CREATED)
async def create_position(
    position_data: CreatePositionRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> PositionDB:
    """Create position of department"""
    if admin:
        created_position: PositionDB = await service.create_position(
            position_data=position_data.model_dump()
        )
        return created_position


@router.put("/update_position/{position_name}", status_code=status.HTTP_200_OK)
async def update_position(
    position_name: str,
    position_data: UpdatePositionRequestByName,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> PositionDB:
    """Update position of department by name"""
    if admin:
        updated_position: PositionDB = await service.update_position_by_name(
            position_name=position_name, position_data=position_data.model_dump()
        )
        return updated_position


@router.delete(
    "/delete_position/{position_name}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_position(
    position_name: str,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> None:
    """Delete position of department by name"""
    if admin:
        await service.delete_position_by_name(position_name=position_name)


@router.post("/add_users_to_position", status_code=status.HTTP_201_CREATED)
async def add_users_to_position(
    users_position_data: CreateUserPositionRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> list[UserPositionDB]:
    """Add users to position"""
    if admin:
        user_position: list[UserPositionDB] = await service.add_users_to_position(
            users_position_data=users_position_data.model_dump()
        )
        return user_position


@router.post("/add_position_to_division", status_code=status.HTTP_201_CREATED)
async def add_position_to_department(
    struct_adm_pos_data: CreateStructAdmPositionRequest,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> StructAdmPositionDB:
    """Add position to department"""
    if admin:
        struct_adm_pos: StructAdmPositionDB = await service.add_position_to_department(
            struct_adm_pos_data=struct_adm_pos_data.model_dump()
        )
        return struct_adm_pos


@router.put(
    "/add_department_head/{user_id}/{struct_adm_name}", status_code=status.HTTP_200_OK
)
async def add_department_head(
    user_id: UUID4,
    struct_adm_name: str,
    admin: UserAuthSchema = Depends(get_current_admin_auth_user),
    service: WorkStructureService = Depends(WorkStructureService),
) -> StructAdmDB:
    """Add department head"""
    if admin:
        add_head_dep: StructAdmDB = await service.add_department_head(
            user_id=user_id, struct_adm_name=struct_adm_name
        )
        return add_head_dep
