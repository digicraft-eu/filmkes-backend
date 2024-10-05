from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import date
import db.movies
import db.scores

router = APIRouter(prefix="/movies")


class MovieSnippet(BaseModel):
    id: int
    title: str
    poster_path: str


@router.get("", response_model=list[MovieSnippet], tags=["movies"])
async def get_popular():
    movies = db.movies.list_movies()

    return [
        MovieSnippet(id=id, title=title, poster_path=poster_path)
        for (id, title, poster_path) in movies
    ]


class MovieDetails(BaseModel):
    id: int
    title: str
    poster_path: str
    overview: str
    release_date: date
    score: int | None


@router.get("/{movie_id}", response_model=MovieDetails | None, tags=["movies"])
async def get_movie_details(movie_id: int):
    movie = db.movies.get_details(movie_id)

    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    score = db.scores.get_movie_score_db(movie_id)
    (id, title, poster_path, overview, release_date) = movie

    return MovieDetails(
        id=id,
        title=title,
        poster_path=poster_path,
        overview=overview,
        release_date=release_date,
        score=score,
    )
