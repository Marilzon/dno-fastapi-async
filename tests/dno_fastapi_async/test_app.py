from http import HTTPStatus
from fastapi.testclient import TestClient


def test_home(client: TestClient):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Fast Works!"}


def test_about(client: TestClient):
    response = client.get("/about")

    assert response.status_code == HTTPStatus.OK
    assert "<h1>About Works!</h1>" in response.text


def test_create_user(client: TestClient):
    response = client.post(
        "/user",
        json={"username": "max", "email": "max@max.com", "password": "secret"},
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "max",
        "email": "max@max.com",
        "id": 1,
    }


def test_get_users(client):
    response = client.get("/users")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "max",
                "email": "max@max.com",
                "id": 1,
            }
        ]
    }
