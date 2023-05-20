import pymysql
from pymysql import Connection
from pymysql.cursors import DictCursor

from core.config import settings


def get_db_conn() -> Connection:
    """
    Returns a new connection to the MySQL database. Closes connection
    automatically.

    @return:
        A new instantiated connection to the database.
    """
    with pymysql.connect(
        host=settings.MYSQL_HOST,
        port=settings.MYSQL_PORT,
        user=settings.MYSQL_USER,
        password=settings.MYSQL_PASSWORD,
        database=settings.MYSQL_DB,
        charset='utf8mb4',
        cursorclass=DictCursor,
    ) as conn:
        yield conn
