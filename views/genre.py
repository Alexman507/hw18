from flask_restx import Resource, Namespace

genre_ns = Namespace('genre')


@genre_ns.route('/')
@genre_ns.param("director_id")
@genre_ns.param("genre_id")
@genre_ns.param("year")
class GenresView(Resource):
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


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
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
