from pydantic import BaseModel, Field
from typing import Optional

#Definicion del esquema para Movie
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=30)
    overview: str = Field(min_length=5, max_length=200)
    year: int = Field(le=2024)
    rating:float = Field(ge=1, le=10)
    category:str = Field(min_length=5, max_length=15)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "MiPelicula",
                    "overview": "MiDescripcion",
                    "year": 2024,
                    "rating": 9.8,
                    "category": "Suspenso"
                }
            ]
        }
    }