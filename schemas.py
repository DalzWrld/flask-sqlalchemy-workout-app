from marshmallow import (
    Schema,
    ValidationError,
    fields,
    post_load,
    validate,
    validates,
)

from models import Exercise, Workout, WorkoutExercise


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)
    created_at = fields.DateTime(dump_only=True)

    # workouts = fields.Nested("WorkoutSchema", excludes=("workouts"))

    @validates("category")
    def validate_category(self, value):
        valid_categories = [
            "Strength",
            "Cardio",
            "Flexibility",
            "Balance",
            "Mobility",
        ]

        if value not in valid_categories:
            raise ValidationError(
                f"Category must be one of {valid_categories}"
            )

    @post_load
    def make_exercise(self, data, **kwargs):
        return Exercise(**data)


class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=1))
    notes = fields.Str()
    created_at = fields.DateTime(dump_only=True)

    exercises = fields.Nested("ExerciseSchema", excludes=("exercises"), many=True, dump_only=True)
    workout_exercises = fields.Nested("WorkoutExerciseSchema", excludes=("exercises"), many=True, dump_only=True)

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    sets = fields.Int(required=True)
    reps = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)