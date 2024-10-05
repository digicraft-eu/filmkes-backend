# What is this?
This site lists out some movies from TMDB.  
The TMDB api is only used to GET info from the movies. We won't use the api to write data.  

We also have a local sqlite database that we'll use to keep track of the score that the user gave to a movie or whether or not the user has "favorited" the movie.  
For this exercise we'll assume we only have 1 user that uses the application.  
So you don't need to think of authentication and authorization. 


# Running locally
## Create a `.env` file.
- Copy `.env.sample`
- Enter a value for `TMDB_API_KEY`

You can get an api key by [creating an account at TMDB](https://www.themoviedb.org/login?to=read_me&redirect=%2Freference%2Fintro%2Fauthentication)

## Install `uv`
- Mac/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

(Or see docs here: https://docs.astral.sh/uv/getting-started/installation/)

## Install Python
`uv python install 3.12`

## Run project
`make dev`  
Or, if make isn't installed: `uv run fastapi dev --port 3000`
 


# Local database structure
There's 2 tables in the sqlite database, these are their columns:

1. `scores`
   - id: integer, primary key
   - movie_id: integer
   - score: integer
2. `favorites`
   - id: integer, primary key
   - movie_id: integer

`scores` keeps track of what score a user gave a certain movie. (No record means the user hasn't scored this movie yet)  
If there's a record in the `favorites` tables for a certain movie we'll assume the user has favorited the movie, if there's no record, the user hasn't 
favorited the movie.


# Assignment

## Implement the favorites feature. 
We want the user to be able to keep track of their favorite movies.  
- When the user opens a movie's detail page they should be able to see if they've marked a movie as favorite or not
- On the movie detail page they should be able to add a movie to their favorites
- They should also be able to remove a movie from their favorites 
 
## Create a favorites overview page
- The user should be able to get a quick overview of all the movies that they have favorited
- The movies should be ordened by the score the user gave to the movies.
  The highest rated movie should be first