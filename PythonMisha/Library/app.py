from fastapi import FastAPI
from models.Author import Author

app = FastAPI()
authorService = AuthorService()

# get_author = app.get("/")(get_author)

@app.get('/authors')
def get_authors():
    return authorService.get_authors()

