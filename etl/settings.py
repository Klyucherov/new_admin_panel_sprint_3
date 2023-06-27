import os
from dataclasses import dataclass
from typing import Callable

from core.indices import movies_index
from core.queries import query_film_work
from models.models import Film

dsl = {
    'dbname': os.getenv('DB_NAME', 'movies_database'),
    'user': os.getenv('DB_USER', 'app'),
    'password': os.getenv('DB_PASSWORD', '123qwe'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'options': '-c search_path=content'
}

ELASTIC_HOST = os.getenv('ELASTIC_HOST', 'localhost')
ELASTIC_PORT = int(os.getenv('ELASTIC_PORT', 9200))

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))

SLEEP_TIME_SECONDS = int(os.getenv('SLEEP_TIME', 60))

DB_FILM_LIMIT = 20000
DB_GENRE_LIMIT = 20000
DB_PERSON_LIMIT = 20000


@dataclass
class ETLConfig:
    """Класс описывающий параметры ETL для отдельной сущности."""
    query: str
    index_schema: dict
    state_key: str
    elastic_index_name: str
    related_model: Callable
    batch_size: int = 100
    limit_size: int = 5000


ETL_CONFIGS = [
    ETLConfig(query_film_work, movies_index, 'film_last_modified_date', 'movies', Film, limit_size=DB_FILM_LIMIT)
]
