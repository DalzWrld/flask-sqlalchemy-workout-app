from datetime import date

from app import app
from models import Workout, Exercise, WorkoutExercise, db

with app.app_context():
    db.session.query(Workout).delete()
    db.session.query(Exercise).delete()
    db.session.query(WorkoutExercise).delete()