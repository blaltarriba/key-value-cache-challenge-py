import warnings
import os

import pytest
from asgi_lifespan import LifespanManager

from fastapi import FastAPI
from starlette.testclient import TestClient


# Create a new application for testing
@pytest.fixture
def app() -> FastAPI:
    from server import get_application

    return get_application()


# Make requests in our tests
@pytest.fixture
def client(app: FastAPI) -> TestClient:
      return TestClient(app)
