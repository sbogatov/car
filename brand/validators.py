from sqlalchemy.ext.asyncio import AsyncSession

from brand.entities import Brand
from brand.exceptions import BrandNotFoundException
from brand.repositories import BrandRepository


class BrandValidator:
    @staticmethod
    async def validate_brand_id(brand_id: int, session: AsyncSession) -> None:
        brand: Brand | None = await BrandRepository.get_by_id(brand_id=brand_id, session=session)
        if not brand:
            raise BrandNotFoundException()
