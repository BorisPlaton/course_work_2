from pydantic import BaseModel


class User(BaseModel):
    """
    Represents user's basic information about.
    """
    user_id: int
    first_name: str
    second_name: str
    last_name: str | None


class Teacher(User):
    """
    Represents base information about the teacher.
    """
    salary: float | None

    class Config:
        schema_extra = {
            'example': {
                'user_id': 1,
                'first_name': 'Daniel',
                'second_name': 'Bush',
                'last_name': 'Sunday',
                'user_type': 'teacher',
                'salary': 25000,
            }
        }
