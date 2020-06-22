from pydantic import BaseModel


class User(BaseModel):
    email: str


class UserResponse(BaseModel):
    msg: str
