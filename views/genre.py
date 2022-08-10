from flask_restx import Resource, Namespace

from dao.model.schema import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genre')
genre_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        Получение всех жанров
        :return:
        """
        return genre_schema.dump(genre_service.get_genres()), 200


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id: int):
        """
        Получение жанра по ID
        :return:
        """
        return genre_schema.dump([genre_service.get_genre_by(genre_id)]), 200
