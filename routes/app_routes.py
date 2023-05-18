from fastapi.responses import RedirectResponse
from fastapi import APIRouter, Path, Query
from functions.utils import Category
from db.movies_db import movies_list
from schemas.movie import Movie

home = APIRouter()


@home.get("/")
def index():
    return RedirectResponse(url="/docs")


@home.get("/movies", tags=["Movies"])
def get_movies():
    return movies_list


@home.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int = Path(ge=0, le=1000)):
    return [movie for movie in movies_list if movie["id"] == id]


@home.get("/movies/category/{category}", tags=["Movies"])
def get_by_category(category: Category):
    return [movie for movie in movies_list if movie["category"] == category]


@home.get("/movies/", tags=["Movies"])
def get_by_name(title: str = Query(min_length=5, max_length=25)):
    return [movie for movie in movies_list if movie["name"] == title]


@home.post("/movies", tags=["Movies"])
def create_movie(movie: Movie):
    return movie
