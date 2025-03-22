from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.workout_db_sql import SessionLocal
from db.models.entities import User
from api.utils.utility_functions import create_hash_password
user_router = APIRouter(prefix ="/user", tags=["User"])

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserCreate(BaseModel):
    username:str
    email:str
    password:str
    class Config:
        orm_mode = True

@user_router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@user_router.post("/add/new")
def add_user(user:UserCreate, db: Session = Depends(get_db)):

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=create_hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@user_router.post("/delete/user/{user_id}")
def delete_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail={"No user found"})
    db.delete(user)
    db.commit()
    return {"message":"successfully deleted account"}
