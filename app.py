import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, db
from auth import AuthError, requires_auth
import simplejson as json


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={r'/': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-type,Authorization,true')
        response.headers.add('Access-Control-Allow-Headers',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/', methods=['GET'])
    def home():
        return jsonify({
            'success': True,
            'message': 'Welcome to Capstone'
        })

    @app.route('/movies')
    @requires_auth('get:movies')
    def get_all_movies(payload):
        try:
            movies = Movie.query.all()
            formatted_movies = [movie.format() for movie in movies]
            return jsonify({
                'success': True,
                'movies': formatted_movies
            })
        except Exception:
            abort(404)

    @app.route('/actors')
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.all()
            return jsonify({
                'success': True,
                'actors': [actor.format()for actor in actors]
            })
        except Exception:
            abort(404)

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movie')
    def create_new_movie(payload):
        body = request.get_json()
        try:
            title = body.get('title', None)
            release_date = body.get('release_date', None)
            movie = Movie(title=title, release_date=release_date)

            movie.insert()

            return jsonify({
                'success': True,
                'message': 'Movie Created'
            })

        except Exception:
            abort(422)

    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actor')
    def create_new_actor(payload):
        body = request.get_json()
        try:
            name = body.get('name', None)
            age = body.get('age', None)
            gender = body.get('gender', None)
            movie_id = body.get('movie_id', None)
            actor = Actor(name=name, age=age, gender=gender, movie_id=movie_id)

            actor.insert()

            return jsonify({
                'success': True,
                'message': 'Actor Created'
            })

        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(payload, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)

        body = request.get_json()

        actor.name = json.dumps(body.get('name', actor.name))
        actor.age = json.dumps(body.get('age', actor.age))
        actor.gender = json.dumps(body.get('gender', actor.gender))
        actor.movie_id = json.dumps(body.get('movie_id', actor.movie_id))

        actor.update()

        return jsonify({
            'success': True,
            'message': 'Actor updated'
        })

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        body = request.get_json()

        movie.title = json.dumps(body.get('title', movie.title))
        movie.release_date = json.dumps(body.get('release_date', movie.release_date))

        movie.update()

        return jsonify({
            'success': True,
            'message': 'Movie updated'
        })

    @app.route('/movies/delete/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        Movie.query.filter(Movie.id == movie_id).delete()
        db.session.commit()
        db.session.close()
        return jsonify({
            "success": True,
            "message": "Movie Deleted"
        })

    @app.route('/actors/delete/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        Actor.query.filter(Actor.id == actor_id).delete()
        db.session.close()
        return jsonify({
            "success": True,
            "message": "Actor Deleted"
        })

    '''
  Error handlers
  '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': "resource not found"
        }), 404

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        return jsonify({
            'success': False,
            'error': ex.status_code,
            'message': ex.error
        }), 401

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
