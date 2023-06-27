from typing import List, Optional

from pydantic import BaseModel


class Genre(BaseModel):
    id: Optional[str]
    name: str


class Person(BaseModel):
    id: str
    name: str


class Film(BaseModel):
    id: str
    imdb_rating: Optional[float]
    genre: List[str]
    title: str
    description: Optional[str]
    director: List[str]
    actors_names: List[str]
    writers_names: List[str]
    actors: List[Person]
    writers: List[Person]
