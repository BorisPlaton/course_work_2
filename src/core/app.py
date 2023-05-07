from fastapi import FastAPI

from core.config import settings
from api.users import router as workers_router


def create_app() -> FastAPI:
    """
    Sets up, creates and returns a configured FastAPI application.

    :return:
        an instance of the FastAPI application.
    """
    app = FastAPI(
        debug=settings.DEBUG,
        title='Center for Professional Retraining of Specialists',
        version='1.0.0',
    )
    app.include_router(workers_router)
    return app
