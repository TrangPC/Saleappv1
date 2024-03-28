from flask import Flask
from api.service import app as api_service
from api.healcheck import app as api_healthcheck
from api.api import app as api_app
from api_dto.api_exception import handle_exception
from flask_redis import FlaskRedis
from repo.minio_manager import app as minio_manager

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://localhost:6379/0"
redis_store = FlaskRedis(app)

app.register_error_handler(Exception, handle_exception)
app.register_blueprint(api_service, url_prefix="/api1")
app.register_blueprint(api_healthcheck, url_prefix="/api1")
app.register_blueprint(api_app, url_prefix="/api3")
app.register_blueprint(minio_manager, url_prefix = '/minio')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
