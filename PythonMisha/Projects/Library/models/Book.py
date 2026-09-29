from pydantic import BaseModel
from Projects.Library.models.Author import Author


class BookPublic(BaseModel):
    name: str
    author: Author


class BookSchema(BaseModel):
    name: str
    author_id: int
