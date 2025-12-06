import pytest
from fastapi.testclient import TestClient

from dno_fastapi_async.app import app


@pytest.fixture
def client():
    return TestClient(app)
