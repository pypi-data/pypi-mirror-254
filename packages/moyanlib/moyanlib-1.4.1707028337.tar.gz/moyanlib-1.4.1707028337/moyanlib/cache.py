import os
import time
import json


class Cache:
    def __init__(self, cache_dir="cache"):
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def get(self, key):
        # 获取缓存
        path = self._get_path(key)

        if os.path.exists(path):
            with open(path, "r") as f:
                data = json.load(f)
                if self._is_expired(data):
                    return None
                else:
                    return data["value"]
        else:
            return None

    def set(self, key, value, ttl=None):
        # 设置缓冲
        path = self._get_path(key)
        data = {"value": value, "created_at": time.time(), "ttl": ttl}
        with open(path, "w") as f:
            json.dump(data, f)

    def get_all(self):
        # 获取所有缓存
        all_data = {}
        for filename in os.listdir(self.cache_dir):
            path = os.path.join(self.cache_dir, filename)
            if os.path.isfile(path) and filename.endswith(".json"):
                with open(path, "r") as f:
                    data = json.load(f)
                    if not self._is_expired(data):
                        all_data[filename[:-5]] = data["value"]
        return all_data

    def delete(self, key):
        # 删除指定缓存
        path = self._get_path(key)
        if os.path.exists(path):
            os.remove(path)

    def delete_all(self):
        # 删除所有缓存
        for filename in os.listdir(self.cache_dir):
            path = os.path.join(self.cache_dir, filename)
            if os.path.isfile(path) and filename.endswith(".json"):
                os.remove(path)

    def _get_path(self, key):
        filename = "{}.json".format(key)
        path = os.path.join(self.cache_dir, filename)
        return path

    def _is_expired(self, data):
        if data["ttl"] and time.time() - data["created_at"] > data["ttl"]:
            return True
        elif not data["ttl"] and time.time() - data["created_at"] > 60:
            return True
        else:
            return False
