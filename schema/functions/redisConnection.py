import redis


def instantiateRedis():
    cache = redis.Redis()
    return cache


def destroyRedis(redisServer):
    del redisServer
