#!/usr/bin/env python3

from flask import request
from flask_restful import Resource

from config import app, db, api
from models import Sport


# Example of the flask_restful library in action:

class ExampleRoutes(Resource):

    def get(self):
        return { 'message': 'This is an example' }, 200


api.add_resource(ExampleRoutes, '/examples')



# TODO: Change the routes below to use the flask_restful syntax

@app.get('/sports')
def all_sports():
    return [ sport.to_dict() for sport in Sport.query.all() ], 200


@app.post('/sports')
def post_sports():

    try:
        new_sport = Sport(
            name=request.json['name'], 
            representative=request.json['representative']
        )

        db.session.add( new_sport )
        db.session.commit()

        return new_sport.to_dict(), 201
    
    except Exception as e:
        return { 'error': str(e) }, 400
    


if __name__ == '__main__':
    app.run(port=5555, debug=True)