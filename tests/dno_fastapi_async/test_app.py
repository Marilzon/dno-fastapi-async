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


def test_update_user(client):
    response = client.put(
        "users/1",
        json={
            "username": "max",
            "email": "max@max.com",
            "password": "new_secret",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "max",
        "email": "max@max.com",
        "id": 1,
    }

def test_update_user_not_exists(client):
    user_id = 999

    response = client.put(
        f"users/{user_id}",
        json={
            "username": "max",
            "email": "max@max.com",
            "password": "new_secret",
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        "detail": "User not found"
    }
