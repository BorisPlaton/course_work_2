from typing import Any

from fastapi import HTTPException
from pymysql import Connection, cursors
from starlette import status


class UserServices:
    """
    Handles a business logic for the users (students, teachers etc).
    """

    def __init__(
        self,
        *,
        conn: Connection
    ):
        self.conn = conn

    def get_all_users(self) -> tuple[dict[str, Any]]:
        """
        Returns all users from the database.

        :return:
            The tuple with all users. It may be empty.
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute(
                """
                SELECT user_id, first_name, second_name, last_name
                FROM users
                ORDER BY user_id;
                """
            )
            return cur.fetchall()

    def get_user(
        self,
        *,
        user_id: int
    ) -> dict:
        """
        Returns information about specific user.

        :param user_id:
            The user's information with provided id will be returned.
        :raise HTTPException:
            If user with provided id doesn't exist, raises an exception.
        :return:
            The dictionary user's information.
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute(
                """
                SELECT user_id, first_name, second_name, last_name
                FROM users
                WHERE user_id = %s
                ORDER BY user_id;
                """, (user_id,)
            )
            user = cur.fetchone()
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User with id '%s' doesn't exist."
                )
            return user

    def get_user_courses(
        self,
        *,
        user_id: int
    ) -> tuple[dict[str, Any]]:
        """
        Returns all user's courses.

        :param user_id:
            Courses for user with such id will be looked up.
        :return:
            The tuple with all courses. It may be empty if none was found.
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute(
                """
                SELECT
                    courses.course_id,
                    courses.title,
                    courses.price,
                    courses.description,
                    students.progress,
                    students.has_paid,
                    students.certificate_date
                FROM users
                    JOIN students USING (user_id)
                    JOIN courses USING (course_id)
                WHERE user_id = %s
                ORDER BY courses.course_id;
                """, (user_id,)
            )
            courses = cur.fetchall()
            cur.execute(
                """
                SELECT
                    courses.course_id,
                    users.user_id,
                    users.first_name,
                    users.second_name,
                    users.last_name,
                    teachers.salary
                FROM users
                    JOIN teachers USING (user_id)
                    JOIN courses USING (course_id)
                WHERE courses.course_id IN (
                    SELECT courses.course_id
                    FROM courses
                        JOIN students USING (course_id)
                    WHERE user_id = %s
                )
                ORDER BY courses.course_id;
                """, (user_id,)
            )
            teachers = cur.fetchall()
            for course in courses:
                course['teachers'] = []
                for teacher in teachers:
                    if teacher['course_id'] == course['course_id']:
                        teacher_copy = teacher.copy()
                        teacher_copy.pop('course_id')
                        course['teachers'].append(teacher_copy)
            return courses

    def get_user_own_courses(
        self,
        *,
        user_id: int
    ) -> tuple[dict[str, Any]]:
        """
        Returns user's created courses, where he is a teacher.

        :param user_id:
            User's Courses with such id will be looked up.
        :return:
            The tuple with all courses. It may be empty
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute(
                """
                SELECT
                    courses.course_id,
                    courses.title,
                    courses.price,
                    courses.description
                FROM courses
                    JOIN teachers USING (course_id)
                WHERE teachers.user_id = %s
                ORDER BY courses.course_id;
                """, (user_id,)
            )
            return cur.fetchall()
