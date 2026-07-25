from marshmallow import Schema, fields


class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Boolean(required=True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Time(required=True)
    notes = fields.Str()

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    sets = fields.Int(required=True)
    reps = fields.Int(required=True)
    duration_seconds = fields.Int(required=True)