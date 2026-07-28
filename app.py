from dotenv import load_dotenv
from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api

from extensions import log
from models import db
from resources.exercises import ExerciseByID, Exercises
from resources.workout_exercises import WorkoutExercises
from resources.workouts import WorkoutByID, Workouts

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app=app)
migrate = Migrate(app=app, db=db)

api = Api(app=app)

@app.before_request
def log_request():
    log.info(
        "request",
        method=request.method,
        content_type=request.headers.get("Content-Type"),
    )


api.add_resource(Workouts, "/workouts")
api.add_resource(WorkoutByID, "/workouts/<int:id>")

api.add_resource(Exercises, "/exercises")
api.add_resource(ExerciseByID, "/exercises/<int:id>")

api.add_resource(
    WorkoutExercises,
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
)


if __name__ == '__main__':
    app.run(debug=True)