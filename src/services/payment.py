from fastapi import HTTPException, status
from pymysql import Connection, cursors

import services


class PaymentService:

    def __init__(
        self,
        *,
        conn: Connection
    ):
        self.conn = conn

    def get_payment_for_all_teachers(self) -> dict:
        """
        Returns a payment for the all teachers of existing
        courses.

        @return:
            The dictionary with sum of all teachers salaries.
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute("""
            SELECT SUM(salary) as payment
            FROM teachers;
            """)
            return cur.fetchone()

    def get_payment_for_teacher(
        self,
        *,
        user_id: int,
    ) -> dict:
        """
        Returns a payment for the specific teacher.

        @return:
            The dictionary with summary teacher's salary.
        """
        services.UserServices(conn=self.conn).check_user_is_teacher(user_id=user_id)
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute("""
            SELECT SUM(salary) as payment
            FROM teachers
            WHERE user_id = %s;
            """, (user_id,))
            return cur.fetchone()

    def set_new_salary(
        self,
        *,
        user_id: int,
        course_id: int,
        new_salary: int,
    ) -> bool:
        """
        Sets a new salary for the specific user.

        @param user_id:
            The teacher with this user id.
        @param course_id:
            At what course the teacher works.
        @param new_salary:
            The new salary to be set.
        @return:
            True if salary was updated.
        """
        services.UserServices(conn=self.conn).check_user_is_teacher(user_id=user_id)
        services.CoursesServices(conn=self.conn).check_course_exists(course_id=course_id)
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute("""
            UPDATE teachers
            SET salary = %s
            WHERE user_id = %s AND course_id = %s;
            """, (new_salary, user_id, course_id))
            self.conn.commit()
            return True

    def pay_for_course(
        self,
        *,
        user_id: int,
        course_id: int
    ) -> bool:
        """
        Returns True if user has successfully paid for the course.

        @param user_id:
            The user that makes a payment.
        @param course_id:
            For what course a payment is made.
        @raise HTTPException:
            If user has already paid for the course, raises an exception
            with 409 status code.
        @return:
            True if user has successfully paid.
        """
        services.UserServices(conn=self.conn).check_user_is_teacher(user_id=user_id)
        services.CoursesServices(conn=self.conn).check_course_exists(course_id=course_id)
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT has_paid
            FROM students
            WHERE user_id = %s AND course_id = %s;
            """, (user_id, course_id))
            has_paid: dict | None = cur.fetchone()
            if has_paid is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User with id '%s' isn't enrolled for the course with id '%s'." % (
                        user_id, course_id
                    )
                )
            elif has_paid['has_paid']:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="User with id '%s' has already paid for the course with id '%s'." % (
                        user_id, course_id
                    )
                )
            cur.execute("""
            UPDATE students
            SET has_paid = true
            WHERE user_id = %s and course_id = %s;
            """, (user_id, course_id))
            self.conn.commit()
            return True
