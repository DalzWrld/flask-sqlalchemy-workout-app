from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
)


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(required=True)
    created_at = fields.DateTime(dump_only=True)

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
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    sets = fields.Int(required=True, validate=validate.Range(min=1))
    reps = fields.Int(required=True, validate=validate.Range(min=1))
    duration_seconds = fields.Int(required=True, validate=validate.Range(min=0))

    created_at = fields.DateTime(dump_only=True)


exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)