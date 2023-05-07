from typing import Annotated

from fastapi import APIRouter, Depends
from pymysql import Connection

from core.db import get_db_conn
from schemas.users import Teacher
from services.users import UserServices


router = APIRouter(
    prefix='/users',
    tags=['Users'],
)
