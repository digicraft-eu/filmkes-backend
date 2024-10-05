from db.connection import MoviesDBConnection


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


def insert_score(movie_id: int, score: int):
    with MoviesDBConnection() as cursor:
        cursor.execute(
            """
            INSERT INTO scores (movie_id, score)
            VALUES (?, ?)
            """,
            (movie_id, score),
        )


def update_score(movie_id: int, score: int):
    with MoviesDBConnection() as cursor:
        cursor.execute(
            """
                UPDATE scores
                SET score = ?
                WHERE movie_id = ?
                """,
            (score, movie_id),
        )
