from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///demo.db"

# Add flask-migrate
migrate = Migrate(app=app, db=db)

# Initialize our app to use flask sqlalchemy
db.init_app(app=app)

api = Api(app=app)