# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример

from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self) -> list[Movie]:
        return self.movie_dao.get_all_movies()

    def get_movie_by(self, id=None, director_id=None, genre_id=None, year=None):

        if director_id and genre_id and year:
            return self.movie_dao.get_movies_by_many_filters(director_id=director_id, genre_id=genre_id, year=year)

        if director_id:
            return self.movie_dao.get_movie_by_director_id(director_id)

        elif genre_id:
            return self.movie_dao.get_movie_by_genre_id(genre_id)

        elif year:
            return self.movie_dao.get_movie_by_year(year)

        elif id:
            return self.movie_dao.get_movie_by_id(id)

        else:
            return []

    def add_film(self, data) -> None:
        self.movie_dao.create(**data)

    def update_film(self, data: dict) -> None:
        self.movie_dao.update(data)

    def delete_film(self, id) -> None:
        self.movie_dao.delete(id)
