from fastapi import HTTPException
from models.user import User as UserModel
from schemas.user import User

class UserService():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_user_by_email(self, email, password):
            user = self.db.query(UserModel).filter(UserModel.email == email).first()
            if user:
                if user.password == password:
                    return user
                else:
                    raise HTTPException(status_code=401, detail="Contraseña incorrecta")
            else:
                raise HTTPException(status_code=401, detail="Correo incorrecto")
        
"""     def create_user(self, user: User):
        new_user = UserModel(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        return """
