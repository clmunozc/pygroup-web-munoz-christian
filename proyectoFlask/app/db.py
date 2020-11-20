from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()

def create_all():
    db.create_all()

def drop_all():
    db.drop_all()

def remove_session():
    db.session.remove()

