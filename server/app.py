#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Sport

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return { "stuff": "I am stuff" }, 404


@app.get('/sports')
def all_sports():
    return [ sport.to_dict() for sport in Sport.query.all() ], 200


@app.post('/sports')
def post_sports():

    new_sport = Sport(
        name=request.json['name'], 
        representative=request.json['representative']
    )

    db.session.add( new_sport )

    db.session.commit()

    return new_sport.to_dict(), 201


if __name__ == '__main__':
    app.run(port=5555, debug=True)
