import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Definición de archivo de la base de datos: nombre y ubicación
sqlite_file_name = "../database.sqlite"

#Obtención de directorio actual mediante ruta del archivo actual
base_dir = os.path.dirname(os.path.realpath(__file__))

#Contrucción de la URL de la base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#Creación de una instancia para la interacción con la base de datos en SQLAlchemy (Util para la depuración)
engine = create_engine(database_url, echo=True)

#Uso de fabrica para instancias de sesión que se utilizarán para todas las interacciones con la base de datos 
Session = sessionmaker(bind=engine)

#Creación una clase base para todas las clases de modelo de SQLAlchemy (Superclase padre de clases de modelos).
Base = declarative_base()