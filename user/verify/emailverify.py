from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

def get_my_item(key,value = None):
    rv = cache.get(key)
    if rv is None and value is not None:
        cache.set(key, value, timeout=60)
        return rv
    if rv is not None:
        return rv






