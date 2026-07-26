from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api

from models import Exercise, Workout, WorkoutExercise, db
from schemas import exercise_schema, exercises_schema, workout_schema, workouts_schema

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app=app)
migrate = Migrate(app=app, db=db)

# Workouts
@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return jsonify(workouts_schema.dump(workouts)), 200

@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    workout = Workout.query.get_or_404(id)

    return jsonify(workout_schema.dump(workout)), 200

@app.route("/workouts", methods=["POST"])
def create_workout():
    try:
        workout = workout_schema.load(request.json)

        db.session.add(workout)
        db.session.commit()

        return jsonify(workout_schema.dump(workout)), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.get_or_404(id)

    db.session.delete(workout)
    db.session.commit()

    return jsonify({
        "message": "Workout deleted successfully."
    }), 200

# Exercises
@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()

    return jsonify(exercises_schema.dump(exercises)), 200

@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    return jsonify(exercise_schema.dump(exercise)), 200

@app.route("/exercises", methods=["POST"])
def create_exercise():
    try:
        exercise = exercise_schema.load(request.json)

        db.session.add(exercise)
        db.session.commit()

        return jsonify(exercise_schema.dump(exercise)), 201

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "error": str(e)
        }), 400

@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.get_or_404(id)

    db.session.delete(exercise)
    db.session.commit()

    return jsonify({
        "message": "Exercise deleted successfully."
    }), 200


api = Api(app=app)

if __name__ == '__main__':
    app.run(debug=True)