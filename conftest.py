import warnings
import os

import pytest
from asgi_lifespan import LifespanManager

from fastapi import FastAPI
# from httpx import AsyncClient
# from fastapi.testclient import TestClient
from starlette.testclient import TestClient


# Create a new application for testing
@pytest.fixture
def app() -> FastAPI:
    from server import get_application

    return get_application()
#     from main import app
#
#     return  app


# Make requests in our tests
@pytest.fixture
def client(app: FastAPI) -> TestClient:
#     async with LifespanManager(app):
#         async with AsyncClient(
#             app=app,
#             base_url="http://testserver",
#             headers={"Content-Type": "application/json"}
#         ) as client:
#             yield client
      return TestClient(app)

