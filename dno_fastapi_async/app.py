from fastapi import FastAPI
from http import HTTPStatus
from dno_fastapi_async.schema import (
    Message,
    UserCreateSchema,
    UserPublicSchema,
    UserPrivateSchema,
)

app = FastAPI()
database = []


@app.get(path="/", status_code=HTTPStatus.OK, response_model=Message)
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
