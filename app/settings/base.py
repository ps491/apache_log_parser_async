from settings import config

PROJECT_NAME = config('PROJECT_NAME')

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT", cast=int, default=6379)

LOG_PATH = config("LOG_PATH")
LOG_CHUNK = config("LOG_CHUNK", cast=int,)

DATABASE = {
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT", cast=int),
        'CONN_MAX_AGE': config('CONN_MAX_AGE', cast=int, default=60),
    }
