import os
import redis
from typing import Optional

class RedisConfig:
    def __init__(self, host: str = 'localhost', port: int = 6379, db: int = 0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = None

    def connect(self):
        self.redis_client = redis.Redis(host=self.host, port=self.port, db=self.db)

    def get(self, key: str) -> Optional[str]:
        if self.redis_client:
            return self.redis_client.get(key)
        return None

    def set(self, key: str, value: str):
        if self.redis_client:
            self.redis_client.set(key, value)

    def close(self):
        if self.redis_client:
            self.redis_client.close()
            self.redis_client = None

def load_config() -> RedisConfig:
    host = os.environ.get('REDIS_HOST', 'localhost')
    port = int(os.environ.get('REDIS_PORT', '6379'))
    db = int(os.environ.get('REDIS_DB', '0'))
    return RedisConfig(host, port, db)

def main():
    config = load_config()
    config.connect()
    config.set('test_key', 'test_value')
    value = config.get('test_key')
    print(value)
    config.close()

if __name__ == '__main__':
    main()