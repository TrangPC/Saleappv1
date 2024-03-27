import flask
from flask import Flask, Blueprint, request
from week2 import bootstrap
from week2.api_dto.api_exception import handle_exception

# import week2.bootstrap

app = flask.Blueprint("api_app", __name__)


# app.register_blueprint(app)
@app.route('/data/profile', methods=['POST'])
def get_name():
    try:
        name = request.form['name']
        data = bootstrap.get_data_profile(name=name)
        return data
    except KeyError:
        return handle_exception(ValueError('Invalid input!'))
    except Exception as e:
        return handle_exception(e)
