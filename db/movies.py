from db.connection import MoviesDBConnection


def get_details(movie_id: int):
    with MoviesDBConnection() as cursor:
        query = cursor.execute(
            """
            SELECT id, title, poster_path, overview, release_date
            FROM movies
            WHERE id = ?
            """,
            (movie_id,),
        )
        return query.fetchone()


def list_movies():
    with MoviesDBConnection() as cursor:
        query = cursor.execute(
            """
            SELECT id, title, poster_path
            FROM movies
            """
        )
        return query.fetchall()
