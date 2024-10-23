import logging
import os

import uvicorn
from fastapi import FastAPI

from app.api.routes.router import router
from app.config import APP_VERSION, APP_NAME, APP_PORT, APP_HOST

logger = logging.getLogger(__name__)


def get_app() -> FastAPI:
    logger.debug("Starting TinyNews app")
    app = FastAPI(title=APP_NAME, version=APP_VERSION)
    app.include_router(router)

    return app


app = get_app()

if __name__ == "__main__":
    host = os.getenv("APP_HOST", APP_HOST)
    port = int(os.getenv("APP_PORT", APP_PORT))
    uvicorn.run(app, host=host, port=port)
