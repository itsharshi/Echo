import uuid

from pydantic import BaseModel


class PersonCreate(BaseModel):
    name: str


class PersonOut(BaseModel):
    id: uuid.UUID
    name: str
    status: str

    class Config:
        from_attributes = True
