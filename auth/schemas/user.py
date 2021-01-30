from pydantic import BaseModel, validator
from typing import Optional, List
import re


class UserBase(BaseModel):
    username: str
    email: str

    @validator('email')
    def validate_email(cls, v):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", v):
            raise ValueError('must be a valid email')
        return v

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            'example': {
                'username': 'noob',
                'password': '1234'
            }
        }


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    id: int

