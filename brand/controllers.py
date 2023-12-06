from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from brand.entities import Brand
from brand.repositories import BrandRepository
from config.database import get_session

brand_router = APIRouter()


@brand_router.get("/brands", response_model=None)
async def get_brands(session: AsyncSession = Depends(get_session)) -> list[Brand]:
    return await BrandRepository.all(session=session)