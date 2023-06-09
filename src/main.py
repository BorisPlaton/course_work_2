import uvicorn

from core.config import settings


if __name__ == '__main__':
    uvicorn.run(
        app='core.app:create_app',
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        factory=True,
    )
