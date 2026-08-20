import uuid

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models
import schemas
from db import Base, engine, get_db

Base.metadata.create_all(bind=engine)

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
