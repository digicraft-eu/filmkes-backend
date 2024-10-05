from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from db.connection import MoviesDBConnection
from datetime import date

router = APIRouter(prefix="/movies")


class MovieSnippet(BaseModel):
    id: int
    title: str
    poster_path: str


@router.get("", response_model=list[MovieSnippet], tags=["movies"])
async def get_popular():
    with MoviesDBConnection() as cursor:
        query = cursor.execute(
            """
            SELECT id, title, poster_path
            FROM movies
            """
        )
        result = query.fetchall()

    return [
        MovieSnippet(id=id, title=title, poster_path=poster_path)
        for (id, title, poster_path) in result
    ]


class MovieDetails(BaseModel):
    id: int
    title: str
    poster_path: str
    overview: str
    release_date: date


@router.get("/{movie_id}", response_model=MovieDetails | None, tags=["movies"])
async def get_movie_details(movie_id: int):
    with MoviesDBConnection() as cursor:
        query = cursor.execute(
            """
            SELECT id, title, poster_path, overview, release_date
            FROM movies
            WHERE id = ?
            """,
            (movie_id,),
        )
        result = query.fetchone()

    if result is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    (id, title, poster_path, overview, release_date) = result
    return MovieDetails(
        id=id,
        title=title,
        poster_path=poster_path,
        overview=overview,
        release_date=release_date,
    )
