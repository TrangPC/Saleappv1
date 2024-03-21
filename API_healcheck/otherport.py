from flask import Flask, jsonify
import requests
app = Flask(__name__)
@app.route('/other', methods = ['GET'])
def run():
    ischeck = False
    response = requests.get('http://127.0.0.1:5000');
if __name__ == '__main__':
    app.run(debug=True)


