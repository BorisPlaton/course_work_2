from typing import Annotated

from fastapi import APIRouter, Depends
from pymysql import Connection

from core.db import get_db_conn
from services.users import UserServices


router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.get('/')
async def get_all_users(
    conn: Annotated[Connection, Depends(get_db_conn)]
):
    """
    Returns all users.
    """
    return UserServices(conn=conn).get_all_users()


@router.get('/{user_id}/')
async def get_user(
    user_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Returns information about specific user.
    """
    return UserServices(conn=conn).get_user(user_id=user_id)


@router.get('/{user_id}/courses/')
async def get_user_courses(
    user_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)]
):
    """
    Returns all user's courses that he is studying.
    """
    return UserServices(conn=conn).get_user_courses(user_id=user_id)


@router.get('/{user_id}/courses/own/')
async def get_user_own_courses(
    user_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)]
):
    """
    Returns all user's courses in which he is a teacher.
    """
    return UserServices(conn=conn).get_user_own_courses(user_id=user_id)


@router.get('/{user_id}/courses/{course_id:int}/')
async def get_user_course_statistics(
    user_id: int,
    course_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)]
):
    """
    Returns a user statistics about the specific course.
    """
    return UserServices(conn=conn).get_user_course_statistics(
        user_id=user_id,
        course_id=course_id
    )
