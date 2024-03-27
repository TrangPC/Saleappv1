from flask import Flask, jsonify, request
from flask_redis import FlaskRedis
from flask import Blueprint
from week2.repo.repo_db import PostgreDatabase
from week2.repo.cache_manager import CacheManager

# from week2 import app
app = Blueprint('cache-redis', __name__)

cache_manager = CacheManager(redis_store=None)


@app.route('/cache-redis-data')
def get_profile():
    name = request.args.get('name')
    if not name:
        return jsonify('error'), 400
    cached_data = cache_manager.get_cache_data(name)
    if cached_data:
        return jsonify('data:' + cached_data)
    else:
        db = PostgreDatabase()
        data = db.get_profile(name)
        if data:
            cache_manager.store_data_in_cache(name, str(data), 1800)
            return jsonify({'data: ' + data})
        else:
            return jsonify('error: data not found')
