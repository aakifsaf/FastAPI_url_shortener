from fastapi import FastAPI,Depends,HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
import random
import string

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters+string.digits, k=length))

@app.post("/shorten/")
async def shorten_url(orgurl: str, db: db_dependency):
    while True:
        short_code = generate_short_code()
        if not db.query(models.URLS).filter(models.URLS.shortcode == short_code).first():
            break 
    db_url = models.URLS(org_url = orgurl, shortcode = short_code)
    db.add(db_url)
    db.commit()
    return {"shortcode": short_code, "message": "successful"}



@app.get("/{short_code}")
async def get_url(short_code: str, db:db_dependency):
    org_url = db.query(models.URLS).filter(models.URLS.shortcode == short_code).first()
    if not org_url:
        raise HTTPException(status_code=404, detail="Shortcode not found")
    return RedirectResponse(url=org_url.org_url, status_code=307)
    
