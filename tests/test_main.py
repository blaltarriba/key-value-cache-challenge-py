import pytest
from starlette.testclient import TestClient
from fastapi import FastAPI
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY

from cache.models.item import Item


class TestCleaningsRoutes:

    def test_health_returns_200(self, client: TestClient) -> None:
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

    def test_get_item_return_item(self, client: TestClient) -> None:
        expected_item = Item(code='a_code', description='a_description')

        response = client.get("/fetch/a_code")

        assert response.status_code == 200
        assert response.json() == {"code": "a_code", "description": "a_description"}