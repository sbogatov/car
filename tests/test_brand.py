from http import HTTPStatus

import pytest
from httpx import Response, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from brand.entities import Brand
from tests.base_test import BaseTest


@pytest.mark.asyncio
class TestBrand(BaseTest):
    async def test_get_brands(self, client: AsyncClient, test_db_session: AsyncSession) -> None:
        payload: dict = {"id": 1, "name": "Saab"}
        test_db_session.add(Brand(**payload))
        await test_db_session.commit()

        response: Response = await client.get("/brands")
        assert response.status_code == HTTPStatus.OK
        assert response.json() == [payload]
