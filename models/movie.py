from config.database import Base
from sqlalchemy import Column, Integer, String, Float

#Clase hija de Base y representativa de la tabla movies en la base de datos
class Movie(Base):
    #Nombre de la tabla de la base de datos
    __tablename__ = "movies"

    #Definición de columnas de la base de datos
    id = Column(Integer, primary_key = True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)