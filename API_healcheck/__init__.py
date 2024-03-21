from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route('/healcheck', methods=['GET'])
def healcheck():
    is_connect = False

    response = requests.get('http://127.0.0.1:5001').status_code;
    if (response == 200):
        return jsonify({
            'status': 'success'
        }, 200)
    else:
        return jsonify({
            'status': 'faild'
        }, 500)



if __name__ == '__main__':
    app.run(debug=True)
