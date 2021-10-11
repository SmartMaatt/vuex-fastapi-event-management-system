from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(User):
    class Config():
        orm_mode = True
