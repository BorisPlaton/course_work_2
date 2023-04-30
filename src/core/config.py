from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Project's configuration. Doesn't accept any `.env*` files. Reads
    only from the environment variables.
    """
    BASE_DIR: Path = Path(__file__).parent.parent
    DEBUG: bool = True

    PORT: int = 8888
    HOST: str = 'localhost'

    class Config:
        env_file_encoding = 'utf-8'


settings = Settings()
