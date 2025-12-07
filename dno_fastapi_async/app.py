from fastapi import FastAPI, HTTPException
from http import HTTPStatus

from dno_fastapi_async.schema.message import MessageSchema

from dno_fastapi_async.schema.user import (
    UserCreateSchema,
    UserPrivateSchema,
    UserPublicSchema,
    UserList,
)

app = FastAPI()
database = []


@app.get(path="/", status_code=HTTPStatus.OK, response_model=MessageSchema)
def home():
    return {"message": "Fast Works!"}


@app.get(path="/about", status_code=HTTPStatus.OK)
def about():
    return """
    <h1>About Works!</h1>
    """


@app.post(
    "/user", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema
)
def create_user(user: UserCreateSchema):
    new_id = len(database) + 1
    user_with_id = UserPrivateSchema(id=new_id, **user.model_dump())
    database.append(user_with_id)

    return user_with_id


@app.get(path="/users", response_model=UserList)
def get_users():
    return {"users": database}


@app.put(path="/users/{user_id}", response_model=UserPublicSchema)
def update_user(user_id: int, user: UserCreateSchema):
    exists = next((True for item in database if item.id == user_id), False)

    if not exists:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User '{user_id}' not found",
        )

    user_with_id = UserPrivateSchema(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(path="/users/{user_id}")
def delete_user(user_id: int):
    exists = next((True for item in database if item.id == user_id), False)

    if not exists:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"User '{user_id}' not found",
        )

    del database[user_id - 1]

    return {"message": f"User '{user_id}' removed"}
