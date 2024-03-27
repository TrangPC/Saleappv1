import flask
from flask import Flask, jsonify, request, Blueprint

app = flask.Blueprint('request', __name__)


class Request:
    def __init__(self, name):
        self.name = name

    @app.route('/request_name', methods=['POST'])
    def get_name(self):
        name = request.json.get('name')
        name_request = Request(name=name)
        return jsonify('Name requested is: ', name_request)
