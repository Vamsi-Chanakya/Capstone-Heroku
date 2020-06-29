import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import json

database_name = "casting_agency_db"
database_path = os.environ.get('DATABASE_URL')

if not database_path:
    database_name = "casting_agency_db"
    database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres', 'localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    migrate = Migrate(app, db)
    db.app = app
    db.init_app(app)

'''
    db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''


# def db_drop_and_create_all():
#     db.drop_all()
#     db.create_all()

'''
Movie
a persistent Movie entity, extends the base SQLAlchemy Model
contains all movies in which casting agency is involved
there is a relation between Movie and Casting Tables
'''

class Movie(db.Model):
    __tablename__ = 'Movie'
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # String Movie Title
    title = db.Column(db.String(120), nullable=False)
    # Release Date of the Movie
    release_date = db.Column(db.Date, nullable=False)
    casting = db.relationship('Casting', backref=db.backref('Movie', lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

'''
Actor
a persistent Actor entity, extends the base SQLAlchemy Model
contains all actors information who belongs to casting agency 
there is a relation between Actor and Casting Tables
'''

class Actor(db.Model):
    __tablename__ = 'Actor'

    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    # String Name of the Actor
    name = db.Column(db.String(60), nullable=False)
    # Age of the Actor
    age = db.Column(db.Integer, nullable=False)
    # String Gender of the actor
    gender = db.Column(db.String(20), nullable=False)
    casting = db.relationship('Casting',
                              backref=db.backref('Actor', lazy=True,
                                                 cascade='all,delete'))

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

'''
Casting
a persistent Casting entity, extends the base SQLAlchemy Model
This Casting table is created for database normalization.
'''
class Casting(db.Model):
    __tablename__ = 'Casting'
    # Autoincrementing, unique primary key
    id = db.Column(db.Integer, primary_key=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id',
                                                   ondelete='CASCADE'))
    movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'))

    def __init__(self, actor_id, movie_id):
        self.actor_id = actor_id
        self.movie_id = movie_id

    def format(self):
        return {
            'id': self.id,
            'actor_id': self.actor_id,
            'movie_id': self.movie_id,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
