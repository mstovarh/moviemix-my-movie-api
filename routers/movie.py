from fastapi import APIRouter, HTTPException
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No se ha encontrado la pelicula"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_Category_o_Year(category: str = Query(None, min_length=5, max_length=15), year: int = Query(None, gt=0)) -> List[Movie]:
    db = Session()
    movie_service = MovieService(db)

    if category and year:
        result = movie_service.get_movies_by_category_and_year(category, year)
    elif category:
        result = movie_service.get_movies_by_category(category)
    elif year:
        result = movie_service.get_movies_by_year(year)
    else:
        raise HTTPException(status_code=400, detail="Debe proporcionar al menos un parámetro de filtro (category o year)")

    db.close()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post( "/", tags=["movies"], response_model=dict, dependencies=[Depends(JWTBearer())])
def create_movie(movie: Movie) -> dict:
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la pelicula"})

@movie_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def update_movie(id: int, movie: Movie)-> dict:
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    MovieService(db).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})

@movie_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int)-> dict:
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la pelicula"})