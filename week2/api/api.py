import flask
from flask import Flask, Blueprint, request
from week2.handler import bootstrap
import week2.bootstrap

app = flask.Blueprint("api_app", __name__)

# app.register_blueprint(app)
@app.route('/data/profile', methods = ['POST'])
def get_name():
    name = request.form['name']
    data = week2.bootstrap.get_data_profile(name = name)
    return data

