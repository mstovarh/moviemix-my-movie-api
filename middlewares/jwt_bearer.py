from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from jwt_manager import validate_token
from config.database import Session
from models.user import User as UserModel

#Creación de clase hija de HTTPBearer para la autenticación por medio de tokens JWT
class JWTBearer(HTTPBearer):
    #Gestionador de solicitudes que necesitan autenticación JWT
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        token_data = validate_token(auth.credentials)
        
        # Obtener el correo electrónico del token JWT
        email = token_data.get('email')
        if not email:
            raise HTTPException(status_code=403, detail="Correo electrónico no encontrado en el token")
        
        # Consultar la base de datos para verificar si existe un usuario con ese correo electrónico
        db = Session()
        db_user = db.query(UserModel).filter(UserModel.email == email).first()
        db.close()
        
        if not db_user:
            raise HTTPException(status_code=403, detail="Usuario no encontrado en la base de datos")
        
        return auth