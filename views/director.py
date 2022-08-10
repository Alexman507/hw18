from flask_restx import Resource, Namespace

director_ns = Namespace('director')


@director_ns.route('/')
@director_ns.param("director_id")
@director_ns.param("director_id")
@director_ns.param("year")
class DirectorsView(Resource):
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


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    def get(self, director_id: int):
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
