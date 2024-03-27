from flask import Flask
class CacheManager:
    def __init__(self, redis_store):
        self.redis_store = redis_store
    def get_cache_data(self, key):
        cached_data = self.redis_store.get(key)
        if cached_data:
            return cached_data
        else:
            return None

    def store_data_in_cache(self, key, data):
        self.redis_store.setex(key, data)
