import functools
import time
from my_lrucache import LRUCacheDict


# CACHE = {}


def cache_it(max_size=1024, expiration=60):
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result
        return inner
    return wrapper


@cache_it(max_size=10, expiration=3)
def query(sql):
    time.sleep(1)
    result = 'execute %s' % sql
    return result


if __name__ == '__main__':
    start = time.time()
    query('SELECT * FROM bog_post')
    print(time.time() - start)

    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)