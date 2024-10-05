from httpx import AsyncClient
import os
from fastapi import Depends
from typing import Annotated
from pydantic import BaseModel
from datetime import date


class Movie(BaseModel):
    id: int
    genre_ids: list[int]
    original_title: str
    overview: str
    poster_path: str
    release_date: date
    vote_average: float
    vote_count: int


class MovieGenre(BaseModel):
    id: int
    name: str


class MovieDetails(BaseModel):
    adult: bool
    backdrop_path: str
    budget: int
    genres: list[MovieGenre]
    homepage: str
    id: int
    imdb_id: str
    origin_country: list[str]
    original_language: str
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: date
    revenue: int
    runtime: int
    status: str
    tagline: str
    title: str
    video: bool
    vote_average: float
    vote_count: int


class TMDBClient:
    http_client: AsyncClient

    def __init__(self):
        tmdb_api_key = os.environ.get("TMDB_API_KEY")
        self.http_client = AsyncClient(
            base_url="https://api.themoviedb.org/3",
            headers={"Authorization": f"Bearer {tmdb_api_key}"},
        )

    async def get_top_movies(self) -> list[Movie]:
        params = {
            "primary_release_year": 2024,
            "sort_by": "popularity.desc",
            "vote_average.gte": 7.5,
        }
        response = await self.http_client.get("/discover/movie", params=params)
        json = response.json()
        return json.get("results", [])

    async def get_movie_details(self, movie_id: int) -> list[MovieDetails]:
        params = {
            "primary_release_year": 2024,
            "sort_by": "popularity.desc",
            "vote_average.gte": 7.5,
        }
        response = await self.http_client.get(f"/movie/{movie_id}", params=params)
        return response.json()


TMDBClientDI = Annotated[TMDBClient, Depends(TMDBClient)]
