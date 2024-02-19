from hyperfunc.core.mq import BaseRedisConn


class Cache(BaseRedisConn):
    def set(self, name, value, ex):
        self._conn.set(name=name, value=value, ex=ex)

    def get(self, name):
        self._conn.get(name=name)

    def delete(self, name):
        self._conn.delete(name)


cache = Cache()
