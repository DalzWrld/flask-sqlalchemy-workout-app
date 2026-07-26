from flask import make_response, request
from flask_restful import Resource

from models import Exercise, db
from schemas import exercise_schema, exercises_schema


class Exercises(Resource):
    def get(self):
        exercises = Exercise.query.all()
        return make_response(exercises_schema.dump(exercises), 200)

    def post(self):
        data = request.get_json()

class ExerciseByID(Resource):
    def get(self, id):
        exercise = Exercise.query.filter_by(id=id).first()
        
        if exercise:
            return make_response(exercise_schema.dump(exercise), 200)
        else:
            response = {
                "status": 404,
                "message": "Exercise not found"
            }
            return make_response(response, 404)

    def delete(self, id):
        self.exercise = Exercise.query.filter_by(id=id).first()

        if self.exercise:
            db.session.delete(self.exercise)
            db.session.commit()

            response = {
                "message": "Exercise deleted successfully"
            }

            return make_response(response, 200)
        else:
            response = {
                "status": 404,
                "message": "Exercise not found"
            }
            
            return make_response(response, 404)