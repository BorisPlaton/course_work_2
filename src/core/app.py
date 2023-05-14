from fastapi import FastAPI

from core.config import settings
from api.users import router as users_router
from api.courses import router as courses_router
from api.payment import router as payment_router


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
    app.include_router(users_router)
    app.include_router(courses_router)
    app.include_router(payment_router)
    return app
