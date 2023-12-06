from typing import Any

from sqlalchemy import select, Result, Select
from sqlalchemy.ext.asyncio import AsyncSession

from car_model.entities import CarModel


class CarModelRepository:
    @staticmethod
    async def get_models_by_brand_id(brand_id: int, session: AsyncSession) -> list[CarModel]:
        query: Select = select(CarModel).where(CarModel.brand_id == brand_id)
        result: Result[Any] = await session.execute(query)
        return result.scalars().all()
