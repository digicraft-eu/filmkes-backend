from fastapi import APIRouter
from util.tmdb import TMDBClientDI, Movie, MovieDetails
from pydantic import BaseModel
from datetime import date

router = APIRouter(prefix="/movies")


@router.get("/popular", response_model=list[Movie], tags=["movies"])
async def get_popular(tmdb_client: TMDBClientDI):
    movies = await tmdb_client.get_top_movies()
    return movies


@router.get("/{movie_id}", response_model=MovieDetails, tags=["movies"])
async def get_movie_details(movie_id: int, tmdb_client: TMDBClientDI):
    return await tmdb_client.get_movie_details(movie_id)
