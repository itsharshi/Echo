import io
import uuid

from fastapi import Depends, FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from minio.error import S3Error
from sqlalchemy.orm import Session

import models
import schemas
from db import Base, engine, get_db
from storage import MINIO_BUCKET, ensure_bucket, minio_client

Base.metadata.create_all(bind=engine)
ensure_bucket()

app = FastAPI(title="Echo Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/people", response_model=schemas.PersonOut)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    db_person = models.Person(name=person.name)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


@app.get("/people/{person_id}", response_model=schemas.PersonOut)
def get_person(person_id: uuid.UUID, db: Session = Depends(get_db)):
    db_person = db.get(models.Person, person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@app.get("/people", response_model=list[schemas.PersonOut])
def list_people(db: Session = Depends(get_db)):
    return db.query(models.Person).all()


@app.post("/people/{person_id}/recordings", response_model=schemas.RecordingOut)
async def upload_recording(
    person_id: uuid.UUID, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    person = db.get(models.Person, person_id)
    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    data = await file.read()
    recording_id = uuid.uuid4()
    object_key = f"{person_id}/{recording_id}"
    content_type = file.content_type or "application/octet-stream"

    minio_client.put_object(
        MINIO_BUCKET,
        object_key,
        data=io.BytesIO(data),
        length=len(data),
        content_type=content_type,
    )

    recording = models.Recording(
        id=recording_id,
        person_id=person_id,
        object_key=object_key,
        content_type=content_type,
        size_bytes=len(data),
    )
    db.add(recording)
    db.commit()
    db.refresh(recording)
    return recording


@app.get("/people/{person_id}/recordings", response_model=list[schemas.RecordingOut])
def list_recordings(person_id: uuid.UUID, db: Session = Depends(get_db)):
    return db.query(models.Recording).filter(models.Recording.person_id == person_id).all()


@app.get("/recordings/{recording_id}/audio")
def get_recording_audio(recording_id: uuid.UUID, db: Session = Depends(get_db)):
    recording = db.get(models.Recording, recording_id)
    if recording is None:
        raise HTTPException(status_code=404, detail="Recording not found")

    try:
        response = minio_client.get_object(MINIO_BUCKET, recording.object_key)
    except S3Error:
        raise HTTPException(status_code=404, detail="Audio file not found in storage")

    return StreamingResponse(response.stream(32 * 1024), media_type=recording.content_type)
