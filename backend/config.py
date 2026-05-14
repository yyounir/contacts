from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)   # Initislize Flask App
CORS(app)               # Able to send cross origin req

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# Specify the location of the sqllite database on our machine
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# Create a database instance for our app

