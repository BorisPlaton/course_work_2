from fastapi import APIRouter


router = APIRouter(
    prefix='/payment',
    tags=['Payment'],
)


@router.get('/teachers/')
async def get_payment_for_all_teachers():
    """
    Returns a total amount of money needed to pay teachers.
    """


@router.get('/teachers/{user_id}/')
async def get_payment_for_teacher(user_id: int):
    """
    Returns a salary of the specific teacher.
    """


@router.patch('/teachers/{user_id}/')
async def increase_teacher_salary(user_id: int):
    """
    Increases a salary of the specific teacher.
    """


@router.get('/users/{user_id}/{course_id}')
async def payment_for_course(user_id: int, course_id: int):
    """
    Returns a true if user has paid for the course and price for this
    course.
    """


@router.post('/users/{user_id}/{course_id}')
async def pay_for_course(user_id: int, course_id: int):
    """
    Pay for the user's course.
    """
