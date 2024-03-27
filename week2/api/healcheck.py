import flask
import requests
from flask import Flask, jsonify, Blueprint

app = flask.Blueprint("api_healcheck", __name__)


# app.register_blueprint(api_healcheck)
@app.route('/healcheck', methods=['GET'])
def healcheck():
    is_connect = False
    try:
        response = requests.get('http://127.0.0.1:8000/api2').status_code
        if response == 200:
            return jsonify({
                'status': 'success'
            }, 200)
        else:
            return jsonify({
                'status': 'fail'
            }, 500)
    except Exception as e:
        return jsonify({
            'status': 'Bad request'
        }, 400)

# if __name__ == '__main__':
#     app.run(debug=True)
