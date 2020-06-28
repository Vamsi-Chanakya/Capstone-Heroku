import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor, Casting, db
from auth import AuthError, requires_auth

ITEMS_PER_PAGE = 10


def paginate_list(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE

    current_list = selection[start:end]

    return current_list


def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)
    setup_db(app)
    #CORS(app)
    CORS(app, resources={'/': {"origins": "*"}})  # Set up CORS. Allow '*' for origins.

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow_Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow_Methods', 'GET,POST,PATCH,DELETE,OPTIONS')
        return response

    # ROUTES

    '''default endpoint'''

    @app.route('/', methods=['POST', 'GET'])
    def health():
        return jsonify("Healthy"),200

    # MOVIES

    '''
    implement endpoint GET /movies
    retrieves list of all movies and display 10 movies per page
    returns status code 200 and json {"success": True, "movies": movies}
    where movies is the list of movies or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(jwt):
        selection = Movie.query.order_by(Movie.id).all()
        current_list = paginate_list(request, selection)

        if len(current_list) == 0:
            abort(404)

        paginated_movies = [movie.format() for movie in current_list]

        return jsonify({
            'success': True,
            'movies': paginated_movies,
            'total_movies': len(selection)
        }), 200

    '''
    implement endpoint POST /movies
    create a new row in the movies table
    require the 'post:movies' permission and
    returns status code 200 and json {"success": True, "new_movie": new_movie}
    where new_movie contains only the newly posted movie or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def create_movie(jwt):
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            title = data.get('title')
            release_date = data.get('release_date')

            new_movie = Movie(title=title, release_date=release_date)
            new_movie.insert()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'new_movie': new_movie.format()
            }), 200
            db.session.close()

    '''
    implement endpoint PATCH /movies/<id> where <id> is the existing movie id
    respond with a 404 error if <id> is not found
    update the corresponding row for <id>
    require the 'patch:movies' permission and
    returns status code 200 and json {"success": True, "updated_movie": updated_movie}
    where updated_movie contains only the updated movie or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def update_movie(jwt, movie_id):
        update_movie = Movie.query.get(movie_id)

        if update_movie is None:
            abort(404)

        data = request.get_json()
        title = data.get('title')
        release_date = data.get('release_date')

        try:
            update_movie.title = title
            update_movie.release_date = release_date
            update_movie.update()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'updated_movie': update_movie.format()
            }), 200
            db.session.close()

    '''
    implement endpoint DELETE /movies/<id> where <id> is the existing model id
    respond with a 404 error if <id> is not found
    delete the corresponding row for <id>
    require the 'delete:movies' permission
    returns status code 200 and json {"success": True, "deleted_movie": movie_id}
    where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    '''

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        delete_movie = Movie.query.get(movie_id)

        if delete_movie is None:
            abort(404)

        try:
            delete_movie.delete()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'deleted_movie': movie_id
            }), 200
            db.session.close()

    # ACTORS

    '''
    implement endpoint GET /actors
    retrieves list of all actors and display 10 actors per page
    returns status code 200 and json {"success": True, "actors": actors}
    where actors is the list of actors or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(jwt):
        selection = Actor.query.order_by(Actor.id).all()
        current_list = paginate_list(request, selection)

        if len(current_list) == 0:
            abort(404)

        paginated_actors = [actor.format() for actor in current_list]

        return jsonify({
            'success': True,
            'actors': paginated_actors,
            'total_actors': len(selection)
        }), 200

    '''
    implement endpoint POST /actors
    create a new row in the actors table
    require the 'post:actors' permission and
    returns status code 200 and json {"success": True, "new_actor": new_actor}
    where new_movie contains only the newly posted actor or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def create_actor(jwt):
        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            name = data.get('name')
            age = data.get('age')
            gender = data.get('gender')

            new_actor = Actor(name=name, age=age, gender=gender)
            new_actor.insert()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'new_actor': new_actor.format()
            }), 200
            db.session.close()

    '''
    implement endpoint PATCH /actors/<id> where <id> is the existing actor id
    respond with a 404 error if <id> is not found
    update the corresponding row for <id>
    require the 'patch:actors' permission and
    returns status code 200 and json {"success": True, "updated_actor": updated_actor}
    where updated_actor contains only the updated actor or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def update_actor(jwt, actor_id):
        updated_actor = Actor.query.get(actor_id)

        if updated_actor is None:
            abort(404)

        data = request.get_json()
        name = data.get('name')
        gender = data.get('gender')
        age = data.get('age')

        try:
            updated_actor.name = name
            updated_actor.gender = gender
            updated_actor.age = age
            updated_actor.update()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'updated_actor': updated_actor.format()
            }), 200
            db.session.close()

    '''
    implement endpoint DELETE /actors/<id> where <id> is the existing model id
    respond with a 404 error if <id> is not found
    delete the corresponding row for <id>
    require the 'delete:actors' permission
    returns status code 200 and json {"success": True, "deleted_movie": movie_id}
    where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    '''

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        deleted_actor = Actor.query.get(actor_id)

        if deleted_actor is None:
            abort(404, 'There is no such an actor.')

        try:
            deleted_actor.delete()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
              'success': True,
              'deleted_actor': actor_id
            }), 200
            db.session.close()

    '''
    implement endpoint GET /casting
    retrieves list of all casting info and display 
    returns status code 200 and json {"success": True, "casting": casting}
    where casting is the list of casting info or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/casting', methods=['GET'])
    @requires_auth('get:casting')
    def get_casting(jwt):
        casting = Casting.query.all()

        if len(casting) == 0:
            abort(404)

        casting_format = [cast.format() for cast in casting]

        return jsonify({
            'success': True,
            'casting': casting_format,
            'total_casting': len(casting_format)
        }), 200

    '''
    implement endpoint POST /actors
    create a new row in the actors table
    require the 'post:actors' permission and
    returns status code 200 and json {"success": True, "new_actor": new_actor}
    where new_movie contains only the newly posted actor or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/casting', methods=['POST'])
    @requires_auth('post:casting')
    def create_casting(jwt):

        try:
            if request.method != 'POST':
                abort(405)

            data = request.get_json()
            actor_id = data.get('actor_id')
            movie_id = data.get('movie_id')

            new_casting = Casting(actor_id=actor_id, movie_id=movie_id)
            new_casting.insert()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'new_casting': new_casting.format()
            }), 200
            db.session.close()

    '''
    implement endpoint PATCH /casting/<id> where <id> is the existing casting id
    respond with a 404 error if <id> is not found
    update the corresponding row for <id>
    require the 'patch:casting' permission and
    returns status code 200 and json {"success": True, "updated_casting": updated_casting}
    where updated_casting contains only the updated casting info or 
    appropriate status code indicating reason for failure
    '''

    @app.route('/casting/<int:casting_id>', methods=['PATCH'])
    @requires_auth('patch:casting')
    def update_casting(jwt, casting_id):
        updated_casting = Casting.query.get(casting_id)

        if updated_casting is None:
            abort(404)

        data = request.get_json()
        actor_id = data.get('actor_id')
        movie_id = data.get('movie_id')

        try:
            updated_casting.actor_id = actor_id
            updated_casting.movie_id = movie_id
            updated_casting.update()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'updated_casting': updated_casting.format()
            }), 200
            db.session.close()

    '''
    implement endpoint DELETE /casting/<id> where <id> is the existing model id
    respond with a 404 error if <id> is not found
    delete the corresponding row for <id>
    require the 'delete:casting' permission
    returns status code 200 and json {"success": True, "deleted_casting": casting_id}
    where id is the id of the deleted record
    or appropriate status code indicating reason for failure
    '''

    @app.route('/casting/<int:casting_id>', methods=['DELETE'])
    @requires_auth('delete:casting')
    def delete_casting(jwt, casting_id):
        delete_casting = Casting.query.get(casting_id)

        if delete_casting is None:
            abort(404)

        try:
            delete_casting.delete()
        except Exception:
            db.session.rollback()
            abort(422)
        finally:
            return jsonify({
                'success': True,
                'deleted_casting': casting_id
            }), 200
            db.session.close()

    # Error Handling

    '''
    Error Handling for bad request
    '''
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    '''
    Error handling for resource not found
    '''

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    '''
    Error handling for method not allowed'
    '''

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405

    '''
    Error handling for unprocessable entity
    '''

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    '''
    Error handling for internal server error
    '''

    @app.errorhandler(500)
    def internal_sever_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'internal server error'
        }), 500

    '''
    implement error handler for AuthError
    error handler should conform to general task above
    '''

    @app.errorhandler(AuthError)
    def auth_error_handler(error):
        response = jsonify(error.error)
        response.status_code = error.status_code
        return response

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
