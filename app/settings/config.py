from environs import Env

DEBUG = True

if DEBUG:
    env = Env()
    env.read_env(".env.dev", recurse=True)
else:
    env = Env()
    env.read_env()

TEST = env.str("TEST")
POSTGRES_HOST = env.str("POSTGRES_HOST")
POSTGRES_PORT = env.str("POSTGRES_PORT")
POSTGRES_USER = env.str("POSTGRES_USER")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD")
DB_NAME = env.str("DB_NAME")

