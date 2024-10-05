from fastapi import APIRouter, Body
from db.connection import MoviesDBConnection
from pydantic import BaseModel
from typing import Annotated

router = APIRouter(prefix="/scores")


def get_movie_score_db(movie_id: int):
    with MoviesDBConnection() as cursor:
        query = cursor.execute(
            """
            SELECT score
            FROM scores
            WHERE movie_id = ?
            """,
            (movie_id,),
        )
        result = query.fetchone()
        return result[0] if result else None


@router.get("/{movie_id}", response_model=int | None, tags=["scores"])
async def get_movie_score(movie_id: int):
    return get_movie_score_db(movie_id)


@router.post("/{movie_id}", response_model=None, tags=["scores"])
async def set_movie_score(movie_id: int, score: Annotated[int, Body()]):
    current_score = get_movie_score_db(movie_id)

    print(current_score, score)

    with MoviesDBConnection() as cursor:
        if current_score is None:
            cursor.execute(
                """
                INSERT INTO scores (movie_id, score)
                VALUES (?, ?)
                """,
                (movie_id, score),
            )
        else:
            cursor.execute(
                """
                UPDATE scores
                SET score = ?
                WHERE movie_id = ?
                """,
                (score, movie_id),
            )
