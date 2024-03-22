import flask
from flask import Flask, jsonify, request, Blueprint
app = flask.Blueprint('request', __name__)
@app.route('/data/profile', methods = ['POST'])
def get_name():
    name = request.form('name')
    # if()
    return name



