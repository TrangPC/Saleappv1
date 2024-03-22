from flask import Flask
from api.service import app as api_service
from api.healcheck import app as api_healthcheck
from api.api import app as api_app
from api_dto.api_exception import errorhandler

app = Flask(__name__)
app.register_blueprint(Exception, errorhandler)
app.register_blueprint(api_service, url_prefix="/api1")
app.register_blueprint(api_healthcheck, url_prefix="/api1")
app.register_blueprint(api_app, url_prefix="/api3")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)