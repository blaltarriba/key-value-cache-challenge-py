import pytest
from starlette.testclient import TestClient
from fastapi import FastAPI
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY

from cache.models.item import Item


class TestCleaningsRoutes:

    def test_get_item_return_item_when_exists(self, client: TestClient) -> None:
        expected_item = Item(code='a_code', description='a_description')

        response = client.get("/fetch/a_code")

        assert response.status_code == HTTP_200_OK
        assert response.json() == {"code": "a_code", "description": "a_description"}

    def test_get_item_does_not_return_item_when_not_exists(self, client: TestClient) -> None:

        response = client.get("/fetch/fake_code")

        assert response.status_code == HTTP_404_NOT_FOUND