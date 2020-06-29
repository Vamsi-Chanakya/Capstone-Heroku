# Udacity FSND Capstone Project - Casting Agency 

## Motivation for project

Integrating my below skills through this capstone project. 

Coding in Python 3
Relational Database Architecture
Modeling Data Objects with SQLAlchemy
Internet Protocols and Communication
Developing a Flask API
Authentication and Access
Authentication with Auth0
Authentication in Flask
Role-Based Access Control (RBAC)
Testing Flask Applications
Deploying Applications

## Heroku Link
https://vamsi-capstone-heroku.herokuapp.com/

## Getting Started
### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. 
This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://docs.python-guide.org/dev/virtualenvs/)

#### PIP Dependencies

Once you have your virtual environment setup, install dependencies by running:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

First ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
export FLASK_ENV=debug;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Casting Agency Specification
The Casting Agency models a company which is responsible for creating movies and managing and assigning actors of those movies. 
We are creating a system to simplify and streamline your process.

### Data Models
- Movie with attributes title and release date
- Actor with attributes name, age and gender
- Casting with attributes actor_id and movie_id

## Authentication
Task for Setup Auth0
1. Create a new Auth0 Account 
2. Select a unique tenant domain 
3. Create a new, single page web application 
4. Create a new API
    * in API Settings:
        * Enable RBAC
        * Enable Add Permissions in the Access Token
5. Create new API permissions:
    "delete:actors",
    "delete:casting",
    "delete:movies",
    "get:actors",
    "get:casting",
    "get:movies",
    "patch:actors",
    "patch:casting",
    "patch:movies",
    "post:actors",
    "post:casting",
    "post:movies"
6. Create new roles for:
    * Casting Assistant - has following permissions for actions. 
        - `get:movies`, `get:actors`, `get:casting`
    * Casting Director - has following permissions for actions. 
        - `get:movies`, `get:actors`, `get:casting`
        - `post:actors`, `post:casting`
        - `patch:movies`, `patch:actors`, `patch:casting`
        - `delete:actors`, `delete:casting`
    * Executive Producer - has following permissions for actions. 
    - `get:movies`, `get:actors`, `get:casting`
    - `post:movies`, `post:actors`, `post:casting`
    - `patch:movies`, `patch:actors`, `patch:casting`
    - `delete:movies`, `delete:actors`, `delete:casting`
7. Endpoints
    - GET /actors, /movies and /casting
    - POST /actors, /movies and /casting
    - PATCH /actors, /movies/ and /casting
    - DELETE /actors, /movies/ and /casting


### Authentication (bearer tokens)

Casting Assistant
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpDblFvOGRUUHNoWjhPelFQM05XVSJ9.eyJpc3MiOiJodHRwczovL3ZhbXNpY2hhbmFreWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjdmN2U0ZTgyNGE1MDAxOTIwODhmYiIsImF1ZCI6IkNhc3RpbmdfQWdlbmN5IiwiaWF0IjoxNTkzMzI3MTkyLCJleHAiOjE1OTM0MTM1OTIsImF6cCI6IkllcEZBY002aExJRERkaXBSbHN4UjNYcUpCMWtKb0RrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0OmNhc3RpbmciLCJnZXQ6bW92aWVzIl19.ety0mr-8mRq_v5hO-6yJBGnh0tiJS5n9jQOrGN_nRu4SLBxfEmD2G3X-EPPb_SAtV5l_RUUSlLRF4X8djKwBmVrUOFCjoClz-4w_iZW4JL1-xI0CtPl9Jc2ENy00_kjp-IV9TiLB5MR5M_1tH0dntQKWS-T-9f6NUDpjQW17Q2mvnbY8egxvxYCCX4pshLG7Z6JQELD-nEikL5vGZHvXO1384db6LFOg5XrBWYtslKf4UTrez3IxcqQOzL5kfFbbwKaiYOWTIC9_dHd7EH5mHk1Ienc7yANa2Ynpu3MccacKKX7r8u8dyJDcWvxNLkU-TpgyQ2yVBjYDYXDPpGwQEQ
```
```
{
  "iss": "https://vamsichanakya.auth0.com/",
  "sub": "auth0|5ef7f7e4e824a500192088fb",
  "aud": "Casting_Agency",
  "iat": 1593327192,
  "exp": 1593413592,
  "azp": "IepFAcM6hLIDDdipRlsxR3XqJB1kJoDk",
  "scope": "",
  "permissions": [
    "get:actors",
    "get:casting",
    "get:movies"
  ]
}
```

Casting Director
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpDblFvOGRUUHNoWjhPelFQM05XVSJ9.eyJpc3MiOiJodHRwczovL3ZhbXNpY2hhbmFreWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjdmODEyZTgyNGE1MDAxOTIwODkxYyIsImF1ZCI6IkNhc3RpbmdfQWdlbmN5IiwiaWF0IjoxNTkzMzI3NDIzLCJleHAiOjE1OTM0MTM4MjMsImF6cCI6IkllcEZBY002aExJRERkaXBSbHN4UjNYcUpCMWtKb0RrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOmNhc3RpbmciLCJnZXQ6YWN0b3JzIiwiZ2V0OmNhc3RpbmciLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6Y2FzdGluZyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDpjYXN0aW5nIl19.oADQg0NgVF5V989VGOakiloHaPidEdC0roJ6Gpc70pbCLtv4hntssBS-CdAzVhympYqWdomlkWugoaInfW1J9RRcdyNiZuMHMEEAUB7904zdCb0ZiS3vChIOTfxpCeZG1mTLvgq7UbzU4xBa7ZKvkPmgsnMmomoPV1Lj8nQYhqPmL3Yz1oJLWlNEz7ooLS6jlES_ISRU0l5XuhpIMiRL3zTskVvx-QCLRQNuaredrIZfIvq13LYPAZv96D8hCBFsai4aeUhitQB8IApTOJTKV2LfMrbN-oIzg8HPd9VAK1OIJ0AlI5sUdvwbnrIh6Xhs2I_hMV0bJ6DHsSRTJH0fLg
```

```
{
  "iss": "https://vamsichanakya.auth0.com/",
  "sub": "auth0|5ef7f812e824a5001920891c",
  "aud": "Casting_Agency",
  "iat": 1593327423,
  "exp": 1593413823,
  "azp": "IepFAcM6hLIDDdipRlsxR3XqJB1kJoDk",
  "scope": "",
  "permissions": [
    "delete:actors",
    "delete:casting",
    "get:actors",
    "get:casting",
    "get:movies",
    "patch:actors",
    "patch:casting",
    "patch:movies",
    "post:actors",
    "post:casting"
  ]
}
```

Executive Producer
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlpDblFvOGRUUHNoWjhPelFQM05XVSJ9.eyJpc3MiOiJodHRwczovL3ZhbXNpY2hhbmFreWEuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZjdmOGFkMzUyZDhmMDAxM2MzNzM1YiIsImF1ZCI6IkNhc3RpbmdfQWdlbmN5IiwiaWF0IjoxNTkzMzI3NDk2LCJleHAiOjE1OTM0MTM4OTYsImF6cCI6IkllcEZBY002aExJRERkaXBSbHN4UjNYcUpCMWtKb0RrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOmNhc3RpbmciLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDpjYXN0aW5nIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOmNhc3RpbmciLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6Y2FzdGluZyIsInBvc3Q6bW92aWVzIl19.L62u6YX_fATBO-MUF-oJD-AHSlVseQfFXfT5z9WGSLv3BmFkECp8GyZP2nNMWUMtZn5ePe3fuUh540k22PYp2LocjkTnlAFC_H9zJJEXjeq-zJXPd4-MwdMXWcse4benAGeulmImwAqdVftxSgTjHnItC3r7nhX-n6kK-1fEHAkcUThYZK_xoj9XuSDHfhwmEaumSw1YhZS2p6Ap__ngO3qAe909UNMD3crtRp3yjmhQt4UGTd0dyU83H1Tym1-DL0rBV0o7kofjjcw3AjeUWAXz0GWS3lXe7tgAHv73g7e35FKHTbQC_vkUWWGPb4kCczXKKCKX_vOGEr-pXBR6yA
```

```
{
  "iss": "https://vamsichanakya.auth0.com/",
  "sub": "auth0|5ef7f8ad352d8f0013c3735b",
  "aud": "Casting_Agency",
  "iat": 1593327496,
  "exp": 1593413896,
  "azp": "IepFAcM6hLIDDdipRlsxR3XqJB1kJoDk",
  "scope": "",
  "permissions": [
    "delete:actors",
    "delete:casting",
    "delete:movies",
    "get:actors",
    "get:casting",
    "get:movies",
    "patch:actors",
    "patch:casting",
    "patch:movies",
    "post:actors",
    "post:casting",
    "post:movies"
  ]
}
```

## Test on local
- Database on local can be created by the following steps.
    - Run `CREATE DATABASE casting_agency_db;` to create a database for test.
    - Import data and database schema with `psql -U postgres casting_agency_db < createdb.sql`

- Database on local can be recreated by the following steps.
    - Execute `TRUNCATE "Casting";`, `TRUNCATE "Movie" CASCADE;`, and `TRUNCATE "Actor" CASCADE;`
    - Import data and database schema with `psql -U postgres casting_agency_db < data.sql`
    
- Test the endpoints by running `test_app.py`
    - Execute `source setup.sh`
    - Execute `python3 test_app.py`

## Test on heroku
- Test the endpoints with Postman. 
    - Import the postman collection `./vamsi-capstone-heroku.postman_collection.json`
    - Run the collection.

- Database on heroku can be recreated by the following steps.
    - Run `heroku pg:psql`
    - Execute `TRUNCATE "Casting";`, `TRUNCATE "Movies" CASCADE;`, and `TRUNCATE "Actor" CASCADE;`
    - Exit heroku psql
    - Import data with `heroku pg:psql --app vamsi-capstone-heroku postgresql-triangular-39700 < data.sql`


## Error Handling

Errors are returned as JSON objects in the following formats:

```
{
    'success': False,
    'error': 400,
    'message': "bad request"
}

or

{
    'code': 'unauthorized',
    'description': 'Permission not found.'
}
```

The API will return seven error types when requests fail:

- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 500: Internal Sever Error

## Endpoints

### GET /movies

- General: Retrieve all movies.
    - Permission: Casting Assistant, Casting Director, Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of movies.
    - Sample: `{{host}}/movies`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 29 Jan 2018 00:00:00 GMT",
            "title": "Black Panther"
        },
        {
            "id": 2,
            "release_date": "Wed, 28 Jun 2017 00:00:00 GMT",
            "title": "Spider-Man: Homecoming"
        },
        {
            "id": 3,
            "release_date": "Mon, 23 Apr 2018 00:00:00 GMT",
            "title": "Avengers: Infinity War"
        },
        {
            "id": 4,
            "release_date": "Wed, 27 Feb 2019 00:00:00 GMT",
            "title": "Captain Marvel"
        },
        {
            "id": 5,
            "release_date": "Sun, 14 Apr 2013 00:00:00 GMT",
            "title": "Iron Man 3"
        }
    ],
    "success": true
}
```

### GET /actors

- General: Retrieve all actors.
    - Permission: Casting Assistant, Casting Director, Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of actors.
    - Sample: `{{host}}/actors`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "actors": [
        {
            "age": 42,
            "gender": "male",
            "id": 1,
            "name": "Chadwick Boseman"
        },
        {
            "age": 23,
            "gender": "male",
            "id": 2,
            "name": "Tom Holland"
        },
        {
            "age": 55,
            "gender": "male",
            "id": 3,
            "name": "Robert Downey Jr."
        },
        {
            "age": 35,
            "gender": "female",
            "id": 4,
            "name": "Scarlett Johansson"
        },
        {
            "age": 30,
            "gender": "female",
            "id": 5,
            "name": "Brie Larson"
        },
        {
            "age": 47,
            "gender": "female",
            "id": 6,
            "name": "Gwyneth Paltrow"
        },
        {
            "age": 53,
            "gender": "male",
            "id": 7,
            "name": "Jon Favreau"
        }
    ],
    "success": true
}
```

### GET /casting

- General: Retrieve all casting.
    - Permission: Casting Assistant, Casting Director, Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of casting.
    - Sample: `{{host}}/casting`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "casting": [
        {
            "actor_id": 1,
            "id": 1,
            "movie_id": 1
        },
        {
            "actor_id": 2,
            "id": 2,
            "movie_id": 2
        },
        {
            "actor_id": 3,
            "id": 3,
            "movie_id": 3
        },
        {
            "actor_id": 4,
            "id": 4,
            "movie_id": 3
        },
        {
            "actor_id": 5,
            "id": 5,
            "movie_id": 4
        },
        {
            "actor_id": 6,
            "id": 6,
            "movie_id": 3
        },
        {
            "actor_id": 6,
            "id": 7,
            "movie_id": 5
        },
        {
            "actor_id": 7,
            "id": 8,
            "movie_id": 5
        }
    ],
    "success": true
}
```

### POST /movies

- General: Create a new movie.
    - Permission: Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of the created movie.
    - Sample: `{{host}}/movies`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "new_movie": {
        "id": 6,
        "release_date": null,
        "title": "The Incredible Hulk"
    },
    "success": true
}
```

### POST /actors

- General: Create a new actor.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of the created actor.
    - Sample: `{{host}}/actors`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "new_actor": {
        "age": 50,
        "gender": "male",
        "id": 8,
        "name": "Edward Norton"
    },
    "success": true
}
```

### POST /casting

- General: Create a new casting.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token.
    - Return: success value and a dictionary of the created casting.
    - Sample: `{{host}}/casting`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "new_casting": {
        "actor_id": 8,
        "id": 9,
        "movie_id": 1
    },
    "success": true
}
```

### PATCH /movies/{movie_id}

- General: Update a movie using a movie ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of a movie to update.
    - Return: success value and a dictionary of the updated movie.
    - Sample: `{{host}}/movies/5`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "success": true,
    "updated_movie": {
        "id": 5,
        "release_date": null,
        "title": "The Incredible Hulk2"
    }
}
```

### PATCH /actors/{actor_id}

- General: Update an actor using an actor ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of an actor to update.
    - Return: success value and a dictionary of the updated actor.
    - Sample: `{{host}}/actors/5`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "success": true,
    "updated_actor": {
        "age": 100,
        "gender": "male",
        "id": 5,
        "name": "Edward Norton"
    }
}
```

### PATCH /casting/{casting_id}

- General: Update a casting using a casting ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of a casting to update.
    - Return: success value and a dictionary of the updated casting.
    - Sample: `{{host}}/casting/5`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "success": true,
    "updated_casting": {
        "actor_id": 1,
        "id": 5,
        "movie_id": 2
    }
}
```

### DELETE /movies/{movie_id}

- General: Delete a movie using a movie ID.
    - Permission: Executive Producer
    - Request Arguments: JWT token and an ID of a movie to delete.
    - Return: success value and the ID of a deleted movie.
    - Sample: `{{host}}/movies/4`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "deleted_movie": 4,
    "success": true
}
```

### DELETE /actors/{actor_id}

- General: Delete an actor using an actor ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of an actor to delete.
    - Return: success value and the ID of a deleted actor.
    - Sample: `{{host}}/actors/4`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "deleted_actor": 4,
    "success": true
}
```

### DELETE /casting/{casting_id}

- General: Delete a casting using a casting ID.
    - Permission: Casting Director and Executive Producer
    - Request Arguments: JWT token and an ID of a casting to delete.
    - Return: success value and the ID of a deleted casting.
    - Sample: `{{host}}/casting/4`
    - Please use postman collection `./vamsi-capstone-heroku.postman_collection.json`
```
{
    "deleted_casting": 4,
    "success": true
}
```

##Deployment on Heroku 

 1. python manage.py db init
 2. python manage.py db migrate
 3. python manage.py db upgrade
 4. pip freeze > requirements.txt
 5. commit and push all your changes on github
 6. heroku create name_of_your_app
 7. git remote add heroku heroku_git_url
 8. heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application
 9. heroku config --app name_of_your_application
 10.Go to heroku dashboard and go to app > setting > Reveal Config Vars and configure all environment variables which are given in setup.sh
 11.git push heroku master
 12.heroku run python manage.py db upgrade --app name_of_your_application