from flask import make_response, request
from flask_restful import Resource
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from extensions import log
from models import Exercise, Workout, WorkoutExercise, db
from schemas import workout_exercise_schema


class WorkoutExercises(Resource):
    def post(self, workout_id, exercise_id):

        workout = Workout.query.filter_by(workout_id=workout_id)
        exercise = Exercise.query.filter_by(exercise_id=exercise_id)

        try:
            data = workout_exercise_schema.load(request.get_json())

            workout_exercise = WorkoutExercise(
                workout=workout,
                exercise=exercise,
                sets=data["sets"],
                reps=data["reps"],
                duration_seconds=data.get("duration_seconds")
            )

            db.session.add(workout_exercise)
            db.session.commit()

            return make_response(workout_exercise_schema.dump(workout_exercise), 201)

        except ValidationError as err:
            log.error("validation_error", errors=err.messages)
                        
            response = {
                "status": 400,
                "message": "Validation error(s) occurred",
                "errors": {**err.messages},
            }
                        
            return make_response(response, 400)

        except IntegrityError as ie:
            log.error(
                "integrity_error", error=str(ie)
            )
            response = {
                "status": 409,
                "message": "That exercise is already part of this workout",
            }

            return make_response(response, 409)

        except ValueError as ve:
            db.session.rollback()
            
            log.error("value_error", error=str(ve))
            
            response = {
                "status": 400,
                "message": "Wrong value(s) entered.",
            }
            
            return make_response(response, 400)