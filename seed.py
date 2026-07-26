from datetime import date

from app import app
from models import Exercise, Workout, WorkoutExercise, db


def seed_data():
    with app.app_context():
        db.session.query(WorkoutExercise).delete()
        db.session.query(Workout).delete()
        db.session.query(Exercise).delete()
        db.session.commit()

        exercises = [
            Exercise(name="Bench Press", category="Strength", equipment_needed=True),
            Exercise(name="Barbell Squat", category="Strength", equipment_needed=True),
            Exercise(name="Deadlift", category="Strength", equipment_needed=True),
            Exercise(name="Push-ups", category="Strength", equipment_needed=False),
            Exercise(name="Running", category="Cardio", equipment_needed=False),
            Exercise(name="Jumping Jacks", category="Cardio", equipment_needed=False),
            Exercise(name="Plank", category="Balance", equipment_needed=False),
            Exercise(name="Yoga Stretch", category="Flexibility", equipment_needed=False)
        ]
        db.session.add_all(exercises)
        db.session.commit()

        workouts = [
            Workout(date=date(2026, 7, 20), duration_minutes=45, notes="Morning strength session"),
            Workout(date=date(2026, 7, 22), duration_minutes=35, notes="Quick cardio and core"),
            Workout(date=date(2026, 7, 24), duration_minutes=60, notes="Full-body workout"),
        ]
        db.session.add_all(workouts)
        db.session.commit()

        workout_exercises = [
            WorkoutExercise(workouts=workouts[0], exercises=exercises[0], sets=3, reps=10),
            WorkoutExercise(workouts=workouts[0], exercises=exercises[1], sets=3, reps=8),
            WorkoutExercise(workouts=workouts[1], exercises=exercises[2], sets=4, reps=6),
            WorkoutExercise(workouts=workouts[1], exercises=exercises[4], sets=3, reps=30, duration_seconds=45),
            WorkoutExercise(workouts=workouts[2], exercises=exercises[3], sets=3, reps=12),
            WorkoutExercise(workouts=workouts[2], exercises=exercises[4], sets=3, reps=20),
        ]
        db.session.add_all(workout_exercises)
        db.session.commit()

        print("Seed data created successfully.")


if __name__ == "__main__":
    seed_data()