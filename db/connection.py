import sqlite3
from fastapi import Depends
from typing import Annotated


class MoviesDBConnection:
    def __init__(self):
        self.con = sqlite3.connect("movies.db")
        self.cur = self.con.cursor()

    def __enter__(self):
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.commit()
        self.con.close()
