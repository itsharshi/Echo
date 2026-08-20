import datetime
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


class RecordingOut(BaseModel):
    id: uuid.UUID
    person_id: uuid.UUID
    content_type: str
    size_bytes: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True
