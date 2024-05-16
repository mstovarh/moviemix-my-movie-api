from pydantic import BaseModel

#Definicion del esquema para User
class User(BaseModel):
    email:str
    password:str