from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from brand.exceptions import BrandNotFoundException
from brand.validators import BrandValidator
from car_model.entities import CarModel
from car_model.repositories import CarModelRepository
from config.database import get_session

car_model_router = APIRouter()


@car_model_router.get("/models", response_model=None)
async def get_car_models(brand_id: int, session: AsyncSession = Depends(get_session)) -> list[CarModel]:
    try:
        await BrandValidator.validate_brand_id(brand_id=brand_id, session=session)
    except BrandNotFoundException as exc:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail=exc.message) from exc
    return await CarModelRepository.get_models_by_brand_id(brand_id=brand_id, session=session)
