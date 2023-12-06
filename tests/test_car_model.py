from http import HTTPStatus

import pytest
from httpx import Response, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from brand.entities import Brand
from car_model.entities import CarModel
from tests.base_test import BaseTest


@pytest.mark.asyncio
class TestCarModel(BaseTest):
    async def test_get_car_models(self, client: AsyncClient, test_db_session: AsyncSession) -> None:
        test_db_session.add(Brand(id=2, name="Rover"))
        await test_db_session.commit()

        payload: dict = {"id": 1, "brand_id": 2, "name": "75"}
        test_db_session.add(CarModel(**payload))
        await test_db_session.commit()

        response: Response = await client.get("/models", params={'brand_id': 2})
        assert response.status_code == HTTPStatus.OK
        assert response.json() == [payload]

        response: Response = await client.get("/models", params={'brand_id': 99999999})
        assert response.status_code == HTTPStatus.BAD_REQUEST

        response: Response = await client.get("/models", params={'brand_id': 'rfev'})
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
