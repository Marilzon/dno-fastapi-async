from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreateSchema(UserBase):
    password: str


class UserPublicSchema(UserBase):
    id: int


class UserPrivateSchema(UserCreateSchema):
    id: int
