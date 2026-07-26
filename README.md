# FLASK-SQLALCHEMY WORKOUT TRACKER APP

A backend API for a workout tracking application used by personal trainers.
Trainers can create reusable exercises, build workouts, and attach exercises
to a workout with the reps, sets, or duration performed.

## Project Description

- **Exercise** — a reusable movement (name, category, whether it needs equipment).
- **Workout** — a single training session (date, duration, notes).
- **WorkoutExercise** — the join between the two, storing the reps/sets/duration
  performed for a given exercise within a given workout.

A workout has many exercises through workout_exercises, and an exercise can
belong to many workouts, so the same exercise can be reused across sessions.

## Installation

1. Clone the repo and move into it:
   ```
   git clone <your-repo-url>
   cd workout-tracker-api
   ```
2. Install dependencies:
   ```
   pipenv install
   pipenv shell
   ```
3. Move into the `server/` directory (all commands below assume you're here):
   ```
   cd server
   ```
4. Initialize, migrate, and upgrade the database:
   ```
   export FLASK_APP=app.py
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade head
   ```
5. Seed the database:
   ```
   python seed.py
   ```

## Running the App

```
python app.py
```

The API runs at `http://localhost:5555`.

## Endpoints

| Method | Route | Description |
|---|---|---|
| `GET` | `/workouts` | List all workouts |
| `GET` | `/workouts/<id>` | Show a workout, including its workout_exercises (reps/sets/duration + exercise details) |
| `POST` | `/workouts` | Create a workout — body: `date`, `duration_minutes`, `notes` |
| `DELETE` | `/workouts/<id>` | Delete a workout and its associated workout_exercises |
| `GET` | `/exercises` | List all exercises |
| `GET` | `/exercises/<id>` | Show an exercise, including the workouts it's used in |
| `POST` | `/exercises` | Create an exercise — body: `name`, `category`, `equipment_needed` |
| `DELETE` | `/exercises/<id>` | Delete an exercise and its associated workout_exercises |
| `POST` | `/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` | Add an exercise to a workout — body: `reps`, `sets`, and/or `duration_seconds` |

### Validation

Requests that fail validation return a `400` with an `errors` key describing
the problem. Validation is enforced at three levels:

- **Table constraints**: unique exercise names, non-blank categories, positive
  workout duration, and positive reps/sets/duration_seconds.
- **Model validations**: name/category/duration checks run before anything
  hits the database.
- **Schema validations**: request payloads are checked for required fields,
  allowed categories, and that at least one of reps/sets/duration_seconds is
  present when adding an exercise to a workout.

## Allowed Exercise Categories

`strength`, `cardio`, `flexibility`, `balance`, `plyometric`