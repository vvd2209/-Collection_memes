import boto3
from botocore.client import Config
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import uuid

from app import models, schemas, crud
from app.database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

s3 = boto3.client('s3',
                  endpoint_url='http://minio:9000',
                  aws_access_key_id='minioadmin',
                  aws_secret_access_key='minioadmin',
                  config=Config(signature_version='s3v4'),
                  region_name='us-east-1')

BUCKET_NAME = 'memes'


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/memes/", response_model=schemas.Meme)
async def create_meme(meme: schemas.MemeCreate, file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_name = f"{uuid.uuid4()}.{file.filename.split('.')[-1]}"
    s3.upload_fileobj(file.file, BUCKET_NAME, file_name, ExtraArgs={"ContentType": file.content_type})
    image_url = f"http://minio:9000/{BUCKET_NAME}/{file_name}"
    return crud.create_meme(db=db, meme=meme, image_url=image_url)


@app.get("/memes/", response_model=List[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes


@app.get("/memes/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = crud.get_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme


@app.put("/memes/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    db_meme = crud.update_meme(db, meme_id=meme_id, meme=meme)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme


@app.delete("/memes/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = crud.delete_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme
