from typing import Any

from sqlalchemy import Result, select
from sqlalchemy.ext.asyncio import AsyncSession

from brand.entities import Brand


class BrandRepository:
    @staticmethod
    async def all(session: AsyncSession) -> list[Brand]:
        result: Result[Any] = await session.execute(select(Brand))
        return result.scalars().all()

    @staticmethod
    async def get_by_id(brand_id: int, session: AsyncSession) -> Brand | None:
        result: Result[Any] = await session.execute(select(Brand).where(Brand.id == brand_id))
        return result.scalars().first()