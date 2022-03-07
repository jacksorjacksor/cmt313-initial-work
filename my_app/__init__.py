from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = "spiderman"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "local_db.db"
)

db = SQLAlchemy(app)


from my_app import routes
