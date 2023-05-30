from typing import Annotated

from fastapi import APIRouter, Depends, Query
from pymysql.connections import Connection

from core.db import get_db_conn
from services.payment import PaymentService


router = APIRouter(
    prefix='/payment',
    tags=['Payment'],
)


@router.get('/teachers/')
async def get_payment_for_all_teachers(
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Returns a total amount of money needed to pay teachers.
    """
    return PaymentService(conn=conn).get_payment_for_all_teachers()


@router.get('/teachers/{user_id}/')
async def get_payment_for_teacher(
    user_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Returns a salary of the specific teacher.
    """
    return PaymentService(conn=conn).get_payment_for_teacher(user_id=user_id)


@router.patch('/teachers/{user_id}/')
async def set_teacher_salary(
    user_id: int,
    course_id: int,
    new_salary: Annotated[int, Query(gt=0)],
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Sets a new salary for the specific teacher on the course.
    """
    return PaymentService(conn=conn).set_new_salary(
        user_id=user_id,
        new_salary=new_salary,
        course_id=course_id
    )


@router.post('/users/{user_id}/{course_id}')
async def pay_for_course(
    user_id: int,
    course_id: int,
    conn: Annotated[Connection, Depends(get_db_conn)],
):
    """
    Pay for the user's course.
    """
    return PaymentService(conn=conn).pay_for_course(
        user_id=user_id,
        course_id=course_id
    )
