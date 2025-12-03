from http import HTTPStatus
from fastapi.testclient import TestClient
from dno_fastapi_async.app import app


def test_home():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Fast Works!"}


def test_about():
    client = TestClient(app)

    response = client.get("/about")

    assert response.status_code == HTTPStatus.OK
    assert "<h1>About Works!</h1>" in response.text
