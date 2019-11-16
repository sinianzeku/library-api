from werkzeug.contrib.cache import SimpleCache

cache = SimpleCache()


def get_my_item(key, value=None, time=60):
    rv = cache.get(key)
    if rv is None and value is not None:
        cache.set(key, value, timeout=time)
        return rv
    if rv is not None:
        return rv
