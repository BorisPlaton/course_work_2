from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Project's configuration. Doesn't accept any `.env*` files. Reads
    only from the environment variables.
    """
    DEBUG: bool = True
    PORT: int = 8888
    HOST: str = 'localhost'

    MYSQL_HOST: str = 'localhost'
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = 'kirill_panchenko'
    MYSQL_PASSWORD: str = 'qwerty'
    MYSQL_DB: str = 'course_work'

    class Config:
        env_file_encoding = 'utf-8'


settings = Settings()
