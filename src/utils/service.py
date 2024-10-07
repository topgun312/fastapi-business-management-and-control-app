from collections.abc import Sequence
from typing import Any

from pydantic import UUID4

from src.utils.unit_of_work import UnitOfWork, transaction_mode


class BaseService:
    base_repository: str = None

    def __init__(self) -> None:
        self.uow: UnitOfWork = UnitOfWork()

    @transaction_mode
    async def add_one(self, **kwargs) -> None:
        await self.uow.__dict__[self.base_repository].add_one(**kwargs)

    @transaction_mode
    async def add_one_and_get_id(self, **kwargs) -> int | str:
        _id = await self.uow.__dict__[self.base_repository].add_one_and_get_id(**kwargs)
        return _id

    @transaction_mode
    async def add_one_and_get_obj(self, **kwargs) -> Any:
        _obj = await self.uow.__dict__[self.base_repository].add_one_and_get_obj(
            **kwargs
        )
        return _obj

    @transaction_mode
    async def get_bu_query_one_or_none(self, **kwargs) -> Any | None:
        _result = await self.uow.__dict__[
            self.base_repository
        ].get_by_query_one_or_none(
            **kwargs,
        )
        return _result

    @transaction_mode
    async def get_by_query_all(self, **kwargs) -> Sequence[Any]:
        _result = await self.uow.__dict__[self.base_repository].get_by_query_all(
            **kwargs
        )
        return _result

    @transaction_mode
    async def update_one_by_id(
        self,
        _id: int | str | UUID4,
        values: dict,
    ) -> Any:
        _obj = await self.uow.__dict__[self.base_repository].update_one_by_id(
            _id=_id,
            values=values,
        )

    @transaction_mode
    async def delete_by_query(self, **kwargs) -> None:
        await self.uow.__dict__[self.base_repository].delety_by_query(**kwargs)

    @transaction_mode
    async def delete_all(self) -> None:
        await self.uow.__dict__[self.base_repository].delete_all()
