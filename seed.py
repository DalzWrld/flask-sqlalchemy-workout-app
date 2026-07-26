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
            Exercise(name="Yoga Stretch", category="Flexibility", equipment_needed=False),
        ]
        db.session.add_all(exercises)
        db.session.commit()
        print(f"{len(exercises)} exercises seeded.")

        workouts = [
            Workout(date=date(2026, 7, 25), duration_minutes=60, notes="Upper body strength session"),
            Workout(date=date(2026, 7, 26), duration_minutes=45, notes="Morning cardio"),
            Workout(date=date(2026, 7, 27), duration_minutes=75, notes="Leg day"),
        ]
        db.session.add_all(workouts)
        db.session.commit()
        print(f"{len(workouts)} workouts seeded.")

        workout_exercises = [
            WorkoutExercise(workouts=workouts[0], exercises=exercises[0], sets=4, reps=10, duration_seconds=None),
            WorkoutExercise(workouts=workouts[0], exercises=exercises[3], sets=3, reps=20, duration_seconds=None),
            WorkoutExercise(workouts=workouts[1], exercises=exercises[4], sets=1, reps=1, duration_seconds=1800),
            WorkoutExercise(workouts=workouts[1], exercises=exercises[5], sets=3, reps=25, duration_seconds=45),
            WorkoutExercise(workouts=workouts[2], exercises=exercises[1], sets=5, reps=8, duration_seconds=None),
            WorkoutExercise(workouts=workouts[2], exercises=exercises[2], sets=4, reps=6, duration_seconds=None),
        ]
        db.session.add_all(workout_exercises)
        db.session.commit()
        print(f"{len(workout_exercises)} workout exercises seeded.")

        print("Seed data created successfully.")


if __name__ == "__main__":
    seed_data()