from flask_restx import Resource, Namespace
from flask import request
from dao.model.schema import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema(many=True)
movie_schema_one = MovieSchema()


@movie_ns.route('/')
# @movie_ns.param("director_id")
# @movie_ns.param("genre_id")
# @movie_ns.param("year")
class MoviesView(Resource):
    def get(self):
        """
        Получение всех фильмов
        :return:
        """
        if len(request.args) > 0:
            return movie_schema.dump(movie_service.get_movie_by(
                director_id=request.args.get("director_id"),
                genre_id=request.args.get("genre_id"),
                year=request.args.get("year"),
                id=request.args.get("id")
            )
            )
        if director_id := request.args.get("director_id"):
            return movie_schema.dump(movie_service.get_movie_by(director_id=director_id))
        elif genre_id := request.args.get("genre_id"):
            return movie_schema.dump(movie_service.get_genre_by(genre_id=genre_id))
        elif year := request.args.get("year"):
            return movie_schema.dump(movie_service.get_movie_by(year=year))
        else:
            return movie_schema.dump(movie_service.get_movies()), 200



    def post(self):
        """
        Добавление нового фильма
        :return:
        """
        movie_service.add_film(request.json)
        return "", 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    def get(self, movie_id: int):
        """
        Получение всех фильмов по ID
        :return:
        """
        return movie_schema.dump([movie_service.get_movie_by(id=movie_id)]), 200

    def put(self):
        """
        Обновить фильм по id
        :return:
        """
        movie_service.update_film(request.json)
        return "", 201

    def delete(self, movie_id: int):
        """
        Удалить фильм по id
        :return:
        """
        movie_service.delete_film(movie_id)
        return "", 201
