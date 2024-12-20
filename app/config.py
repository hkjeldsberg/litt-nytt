from starlette.config import Config

config = Config(".env")

APP_NAME = "LittNytt"
APP_VERSION = "0.1.0"
APP_PORT = config("PORT", default=8000)
APP_HOST = "127.0.0.1"
APP_TIMEOUT = 60
HF_TOKEN = config("HF_TOKEN", default=None)
DATABASE_URL = config("DATABASE_URL", default=None)
