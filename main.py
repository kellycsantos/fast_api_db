from fastapi import Depends, FastAPI
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from database import get_db
from models import Usuario

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensagem": "Minha primeira API!"
    }
@app.get("/users")
def users(db: Session = Depends(get_db)):
    stmt = select(Usuario)
    usuarios = db.scalars(stmt).all()
    return usuarios

@app.get("/ping")
def ping_db(db: Session = Depends(get_db)):
    resultado = db.execute(text("SELECT NOW()"))
    return {
        "database_time": resultado.scalar()
    }