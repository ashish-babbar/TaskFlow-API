from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TaskCreate(BaseModel):
    title: str


class TaskOut(BaseModel):
    id: int
    title: str
    is_done: bool
    created_at: datetime

    class Config:
        from_attributes = True
