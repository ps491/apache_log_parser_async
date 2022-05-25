from environs import Env

DEBUG = True

if DEBUG:
    env = Env()
    env.read_env(".env.dev", recurse=True)
else:
    env = Env()
    env.read_env()

POSTGRES_HOST = env.str("POSTGRES_HOST")

POSTGRES_PORT = env.str("POSTGRES_PORT")
USER = env.str("USER")
PASSWORD = env.str("PASSWORD")
DB_NAME = env.str("DB_NAME")

