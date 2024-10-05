from fastapi import FastAPI, Request
import routers
import routers.movies
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import time

import routers.scores

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_delay(request: Request, call_next):
    time.sleep(0.5)
    return await call_next(request)


app.include_router(routers.movies.router)
app.include_router(routers.scores.router)


@app.get("/", response_model=str, tags=["root"])
async def root():
    return "The api docs can be found at /redoc"
