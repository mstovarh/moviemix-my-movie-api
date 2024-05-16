from fastapi import APIRouter, HTTPException
from jwt_manager import create_token
from fastapi.responses import JSONResponse
from config.database import Session
from models.user import User as UserModel
from schemas.user import User
from services.user import UserService

user_router = APIRouter()

""" @user_router.post( "/logup", tags=['auth'], response_model=dict)
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={"message": "Usted se ha registrado"}) """

@user_router.post('/login', tags=['auth'])
def login(user: User):
    db = Session()
    user_service = UserService(db)
    
    db_user = user_service.get_user_by_email(user.email, user.password)
    if db_user is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    
    token: str = create_token(user.model_dump())
    return JSONResponse(status_code=200, content={"token": token})