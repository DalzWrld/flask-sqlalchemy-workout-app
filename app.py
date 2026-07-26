from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Api

from models import db, Workout, Exercise, WorkoutExercise
from schemas import workout_schema, workouts_schema, exercise_schema, exercises_schema

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app=app)
migrate = Migrate(app=app, db=db)

@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()

    return jsonify(workouts_schema.dump(workouts)), 200


api = Api(app=app)

if __name__ == '__main__':
    app.run(debug=True)