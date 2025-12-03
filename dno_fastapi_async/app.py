from fastapi import FastAPI
from http import HTTPStatus
from dno_fastapi_async.schema import Message

app = FastAPI()


@app.get(path="/", status_code=HTTPStatus.OK, response_model=Message)
def home():
    return {"message": "Fast Works!"}


@app.get(path="/about", status_code=HTTPStatus.OK)
def about():
    return """
    <h1>About Works!</h1>
    """
