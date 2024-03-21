import datetime
import os.path
import tempfile

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from datetime import datetime
import sqlite3

app = Flask(__name__)
app.secret_key = 'gjla14234&&o2824jfsj##$gjlajlaaqpri'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///labsaledb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

