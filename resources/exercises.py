from flask import make_response, request
from flask_restful import Resource
from marshmallow import ValidationError

from extensions import log
from models import Exercise, db
from schemas import exercise_schema, exercises_schema


class Exercises(Resource):
    def get(self):
        exercises = Exercise.query.all()

        log.info("get_all_exercises", request_data=exercises_schema.dump(exercises))
        return make_response(exercises_schema.dump(exercises), 200)

    def post(self):
        try:
            data = exercise_schema.load(request.get_json())
            exercise = Exercise(**data)

            db.session.add(exercise)
            db.session.commit()

            return make_response(exercise_schema.dump(exercise), 201)

        except ValidationError as err:
            log.error("validation_error", errors=err.messages)

            response = {
                "status": 400,
                "message": "Validation error(s) occurred",
                "errors": {**err.messages},
            }

            return make_response(response, 400)

        except ValueError as ve:
            db.session.rollback()

            log.error("value_error", error=str(ve))

            response = {
                "status": 400,
                "message": "Wrong value(s) entered.",
            }

            return make_response(response, 400)


class ExerciseByID(Resource):
    def get(self, id):
        exercise = Exercise.query.filter_by(id=id).first()

        if exercise:
            return make_response(exercise_schema.dump(exercise), 200)
        else:
            response = {"status": 404, "message": "Exercise not found"}

            return make_response(response, 404)

    def delete(self, id):
        exercise = Exercise.query.filter_by(id=id).first()

        if exercise:
            db.session.delete(exercise)
            db.session.commit()

            response = {"message": "Exercise deleted successfully"}

            return make_response(response, 200)

        else:
            response = {"status": 404, "message": "Exercise not found"}

            return make_response(response, 404)