from dataclasses import Field
from typing import Optional
from sqlmodel import SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    hashed_password: str