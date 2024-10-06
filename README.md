# What is this?
This site lists out some movies that we have in a local sqlite database.  
We also keep track of the score that the user gave to a movie and whether or not the user has "favorited" the movie.  
For this exercise we'll assume we only have 1 user that uses the application.  
So you don't need to think of authentication and authorization.  


# Running locally

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
There's 3 tables in the sqlite database, these are their columns:

1. `movies`
   -  id: integer, primary key
   -  title: text
   -  poster_path: text
   -  overview: text
   -  release_date: text
2. `scores`
   - id: integer, primary key
   - movie_id: integer (references `movies.id`)
   - score: integer
3. `favorites`
   - id: integer, primary key
   - movie_id: integer (references `movies.id`)

`scores` keeps track of what score a user gave a certain movie. (No record means the user hasn't scored this movie yet)  
If there's a record in the `favorites` tables for a certain movie we'll assume the user has favorited the movie, if there's no record, the user hasn't 
favorited the movie.


# Assignment

## 1. Implement the favorites feature. 
We want the user to be able to keep track of their favorite movies.  
- When the user opens a movie's detail page they should be able to see if they've marked a movie as favorite or not
- On the movie detail page they should be able to add a movie to their favorites
- They should also be able to remove a movie from their favorites

## 2. Show the date next to the title
- The date should be formatted like this: 5 Oct, 2024
 
## 3. Create a favorites overview page
- The user should be able to get a quick overview of all the movies that they have favorited
- The movies should be ordened by the score the user gave to the movies.
  The highest rated movie should be first

# Tools
You're allowed to use the internet, install new npm modules, etc  
ChatGPT usage is allowed, but you're not allowed to copy or type any of the application's code to ChatGPT.  
This means you're allowed to use it for general questions like you would use Google.  
Remember, you're also allowed to ask us questions!
