from fastapi import APIRouter, Body
from typing import Annotated
import db.scores

router = APIRouter(prefix="/scores")


@router.post("/{movie_id}", response_model=None, tags=["scores"])
async def set_movie_score(movie_id: int, score: Annotated[int, Body()]):
    current_score = db.scores.get_movie_score_db(movie_id)

    if current_score is None:
        db.scores.insert_score(movie_id, score)
    else:
        db.scores.update_score(movie_id, score)
