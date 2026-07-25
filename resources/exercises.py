from flask import make_response
from flask_restful import Resource

from models import Exercise, db


class Exercises(Resource):
    def get(self):
        exercises = Exercise.query.all()
        return make_response([{"id": exercise.id, "name": exercise.name, "category": exercise.category} for exercise in exercises], 200)

class ExerciseByID(Resource):
    def get(self, id):
        exercise = Exercise.query.filter_by(id=id).first()
        
        if exercise:
            return make_response({"id": exercise.id, "name": exercise.name, "category": exercise.category}, 200)
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