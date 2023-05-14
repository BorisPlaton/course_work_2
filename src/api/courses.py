from fastapi import APIRouter


router = APIRouter(
    prefix='/courses',
    tags=['Courses'],
)


@router.get('/')
async def get_all_courses():
    """
    Returns all available courses.
    """


@router.get('/{course_id}/')
async def get_course(course_id: int):
    """
    Returns information about specific course.
    """


@router.post('/{course_id}/students/{user_id}/add/')
async def add_user_to_course(course_id: int, user_id: int):
    """
    Adds a user to the course.
    """


@router.post('/{course_id}/teachers/{user_id}/add/')
async def add_teacher_to_course(course_id: int, user_id: int):
    """
    Adds a teacher to the course.
    """


@router.post('/{course_id}/students/{user_id}/remove/')
async def remove_user_from_course(course_id: int, user_id: int):
    """
    Removes a user from the course.
    """


@router.post('/{course_id}/teachers/{user_id}/remove/')
async def remove_teacher_from_course(course_id: int, user_id: int):
    """
    Removes a teacher from the course.
    """


@router.patch('/{course_id}/students/{user_id}/progress/')
async def increase_user_progress(course_id: int, user_id: int):
    """
    Increases progress of the specific user in the course.
    """


@router.patch('/{course_id}/students/{user_id}/certificate/')
async def get_user_certificate(course_id: int, user_id: int):
    """
    Returns a user's certificate, if he has it.
    """
