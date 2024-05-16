from config.database import Base
from sqlalchemy import Column, Integer, String

#Clase hija de Base y representativa de la tabla users en la base de datos
class User(Base):
    #Nombre de la tabla de la base de datos
    __tablename__ = "users"

    #Definición de columnas de la base de datos
    id = Column(Integer, primary_key = True)
    email = Column(String)
    password = Column(String)