from flask import make_response
from flask_restful import Resource

from models import Exercise, db


class Exercises(Resource):
    def get(self):
        exercises = Exercise.query.all()
        return make_response([{"id": exercise.id, "name": exercise.name, "category": exercise.category} for exercise in exercises], 200)