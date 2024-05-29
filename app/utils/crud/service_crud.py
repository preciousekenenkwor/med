import datetime
from turtle import up
from typing import Any, Dict, List, Optional

from fastapi import HTTPException, status
from pydantic import AnyUrl
from sqlalchemy import delete, func, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.future import select

from app.config.database.db import Base
from app.utils.crud.types_crud import ResponseMessage, response_message

from .queries import Queries


class CrudService[X]:
    # def __init__(self, model: DeclarativeMeta, db: AsyncSession):
    def __init__(self, model: DeclarativeMeta, db: AsyncSession):
        self.model = model
        self.db = db

    async def get_many(
        self,
        query: Dict[str, Any],
        filter: Optional[Dict[str, Any]] = None,
        select: Optional[List[str]] = None
    ) -> ResponseMessage:
        query_model = select(self.model) # type: ignore

        if filter:
            for key, value in filter.items():
                query_model = query_model.where(getattr(self.model, key) == value)

        query_handler = Queries(query_model, query)

        # Apply select fields if provided
        if select:
            query_handler.model = query_handler.model.with_only_columns(*[getattr(self.model, field) for field in select]) # type: ignore

        query_handler.filter().limit_fields().paginate().sort()

        results = (await self.db.execute(query_handler.model)).scalars().all()

        if not results:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=response_message(data=None, error="Data not found", message="Data not found", success_status=False)
            )

        return response_message(
            success_status=True,
            message="Data fetched successfully",
            data=results,
            doc_length=len(results)
        )

    async def get_one(self, data: Dict[str, Any], select: Optional[List[str]] = None) -> ResponseMessage:
        query = select(self.model).filter_by(**data) # type: ignore
        if select:
            query = query.with_only_columns(*[getattr(self.model, field) for field in select])

        result:X|None = (await self.db.execute(query)).scalar_one_or_none()
        if result is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=response_message(data=None, error="Data not found", message="Data not found", success_status=False)
            )
        return response_message(data=result, doc_length=1, error=None, message="Data fetched successfully", success_status=True)

    async def create(self, data: dict[str, Any]):
        db_item = self.model(**data)
        self.db.add(db_item)
        await self.db.commit()
        await self.db.refresh(db_item)
        return response_message(data=db_item, doc_length=1, error=None, message="Data created successfully", success_status=True)

    async def update(self, filter: dict[str, Any], data: Dict[str, Any]):
        query = update(self.model).filter_by(**filter). values(**data, updated_at=func.now()).execution_options(synchronize_session="fetch")
        await self.db.execute(query)
        await self.db.commit()

        updated_item = await self.get_one(**filter)
        if updated_item:
            return response_message(data=updated_item, doc_length=1, error=None, message="Data updated successfully", success_status=True)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=response_message(data=None, error="Data not found", message="Data not found", success_status=False)
        )

    async def delete(self, filter: dict[str, Any]):
        query = delete(self.model).filter_by(**filter).execution_options(synchronize_session="fetch")
        result = await self.db.execute(query)
        await self.db.commit()

        if result.rowcount > 0:
            return response_message(data=None, error=None, message="Data deleted successfully", success_status=True)

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=response_message(data=None, error="Data not found", message="Data not found", success_status=False)
        )

    async def _include_fields(self, field: str) -> Any:
        return getattr(self.model, field, None)

    async def _exclude_fields(self, field: str) -> Any:
        return getattr(self.model, field, None)
