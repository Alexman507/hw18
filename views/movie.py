from flask_restx import Resource, Namespace

movie_ns = Namespace('movie')


@movie_ns.route('/')
@movie_ns.param("director_id")
@movie_ns.param("genre_id")
@movie_ns.param("year")
class MoviesView(Resource):
    def get(self):
        """
        Получение всех фильмов
        :return:
        """
        return "", 200

    def post(self):
        """
        Добавление нового фильма
        :return:
        """
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """
        Получение всех фильмов по ID
        :return:
        """
        return "", 200

    def put(self):
        """
        Обновить фильм по id
        :return:
        """
        return "", 201

    def delete(self):
        """
        Удалить фильм по id
        :return:
        """
        return "", 201
