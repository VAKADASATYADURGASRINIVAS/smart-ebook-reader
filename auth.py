from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from database import users

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"])
SECRET = "SECRET_KEY"

class AuthRequest(BaseModel):
    email: str
    password: str

def create_token(email: str):
    payload = {
        "sub": email,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

@router.post("/register")
def register(data: AuthRequest):
    if users.find_one({"email": data.email}):
        raise HTTPException(400, "User already exists")
    users.insert_one({
        "email": data.email,
        "password": pwd.hash(data.password)
    })
    return {"message": "Registered"}

@router.post("/login")
def login(data: AuthRequest):
    user = users.find_one({"email": data.email})
    if not user or not pwd.verify(data.password, user["password"]):
        raise HTTPException(401, "Invalid credentials")
    return {
        "email": data.email,
        "token": create_token(data.email)
    }
