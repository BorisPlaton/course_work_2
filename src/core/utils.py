from fastapi import FastAPI

from core.config import settings


def create_app() -> FastAPI:
    """
    Setups, creates and returns a configured FastAPI application.

    :return: instance of the FastAPI class.
    """
    app = FastAPI(
        debug=settings.DEBUG,
        title='Центр Професійної Перепідготовки Спеціалістів',
        version='1.0.0',
    )
    return app
