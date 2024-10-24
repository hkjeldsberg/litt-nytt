from starlette.config import Config

config = Config(".env")

ACCOUNT_URL = config("PREDICTION_SERVICE_BLOB_STORAGE_ACCOUNT_URL", default=None)

APP_NAME = "TinyNews"
APP_VERSION = "0.1.0"
APP_PORT = config("PORT", default=8000)
APP_HOST = "127.0.0.1"
APP_TIMEOUT = 60
