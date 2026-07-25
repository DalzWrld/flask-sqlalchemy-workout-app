from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=naming_convention)

db = SQLAlchemy(metadata=metadata)

workout_exercises = db.Table(
    "workout_exercises",
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.id'), primary_key=True),
    db.Column('workout_id', db.Integer, db.ForeignKey('workouts.id'), primary_key=True),
    reps = db.Column(db.Integer, nullable=False),
    sets = db.Column(db.Integer, nullable=False),
    duration_seconds = db.Column(db.Integer, nullable=False)
)

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    equipment_needed = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text(250), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)