from pydantic import BaseModel, UUID4


class IdStructAdmPositionSchema(BaseModel):
    id: UUID4


class CreateStructAdmPositionSchema(BaseModel):
    struct_adm_id: UUID4
    position_id: UUID4


class UpdateStructAdmPositionSchema(
    IdStructAdmPositionSchema, CreateStructAdmPositionSchema
): ...


class StructAdmPositionSchema(
    IdStructAdmPositionSchema, CreateStructAdmPositionSchema
): ...
