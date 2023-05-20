from typing import Annotated

from fastapi import APIRouter, Depends, Query
from pymysql.connections import Connection

from core.db import get_db_conn
from services import CoursesServices


router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/')
async def get_all_courses(
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Returns all available courses.
    """
    return CoursesServices(conn=conn).get_all_courses()


@router.get('/{course_id}/')
async def get_course(
    course_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Returns information about specific course.
    """
    return CoursesServices(conn=conn).get_course(course_id=course_id)


@router.post('/{course_id}/students/{user_id}/add/')
async def add_student_to_course(
    conn: Annotated[Connection, Depends(get_db_conn)],
    course_id: int,
    user_id: int
):
    """
    Adds a user to the course.
    """
    return CoursesServices(conn=conn).add_student_to_course(user_id=user_id, course_id=course_id)


@router.post('/{course_id}/teachers/{user_id}/add/')
async def add_teacher_to_course(
    conn: Annotated[Connection, Depends(get_db_conn)],
    course_id: int,
    user_id: int,
    salary: int | None = None,
):
    """
    Adds a teacher to the course.
    """
    return CoursesServices(conn=conn).add_teacher_to_course(
        user_id=user_id,
        course_id=course_id,
        salary=salary,
    )


@router.post('/{course_id}/students/{user_id}/remove/')
async def remove_student_from_course(
    conn: Annotated[Connection, Depends(get_db_conn)],
    course_id: int,
    user_id: int
):
    """
    Removes a user from the course.
    """
    return CoursesServices(conn=conn).remove_student_from_course(
        course_id=course_id,
        user_id=user_id,
    )


@router.post('/{course_id}/teachers/{user_id}/remove/')
async def remove_teacher_from_course(
    conn: Annotated[Connection, Depends(get_db_conn)],
    course_id: int,
    user_id: int
):
    """
    Removes a teacher from the course.
    """
    return CoursesServices(conn=conn).remove_teacher_from_course(
        course_id=course_id,
        user_id=user_id,
    )


@router.patch('/{course_id}/students/{user_id}/progress/')
async def increase_student_progress(
    conn: Annotated[Connection, Depends(get_db_conn)],
    course_id: int,
    user_id: int,
    points_amount: Annotated[float, Query(ge=0, le=100)],
):
    """
    Increases progress of the specific user in the course.
    """
    return CoursesServices(conn=conn).increase_student_progress(
        user_id=user_id,
        course_id=course_id,
        points_amount=points_amount,
    )
