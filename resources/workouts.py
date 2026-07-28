from flask import make_response, request
from flask_restful import Resource
from marshmallow import ValidationError

from extensions import log
from models import Workout, db
from schemas import workout_schema, workouts_schema


class Workouts(Resource):
    def get(self):
        workouts = Workout.query.all()

        log.info("get_all_users", request_data=workouts_schema.dump(workouts))
        return make_response(workouts_schema.dump(workouts), 200)

    def post(self):
        try:
            data = workout_schema.load(request.get_json())
            workout = Workout(**data)

            db.session.add(workout)
            db.session.commit()

            return make_response(workout_schema.dump(workout), 201)

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