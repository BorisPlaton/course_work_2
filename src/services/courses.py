from typing import Any

from fastapi import HTTPException, status
from pymysql import cursors, IntegrityError
from pymysql.connections import Connection

import services


class CoursesServices:

    def __init__(
        self,
        *,
        conn: Connection
    ):
        self.conn = conn

    def get_all_courses(self) -> tuple[dict[str, Any]]:
        """
        Returns all courses from the database.

        @return:
            The tuple with all courses. It may be empty.
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute(
                """
                SELECT course_id, title, price, description
                FROM courses
                ORDER BY course_id;
                """
            )
            return cur.fetchall()

    def get_course(
        self,
        *,
        course_id: int
    ) -> dict[str, Any]:
        """
        Returns information about specific course.

        @param course_id:
            The course information with provided id will be returned.
        @raise HTTPException:
            If the course with provided id doesn't exist, raises an exception.
        @return:
            The dictionary with course information.
        """
        with self.conn.cursor() as cur:
            cur: cursors.DictCursor
            cur.execute("""
                SELECT course_id, title, price, description
                FROM courses
                WHERE course_id = %s;
            """, (course_id,))
            course = cur.fetchone()
            if not course:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Course with id '%s' doesn't exist."
                )
            cur.execute("""
                SELECT
                    users.user_id,
                    teachers.salary,
                    users.first_name,
                    users.second_name, 
                    users.last_name
                FROM teachers
                    JOIN users USING (user_id)
                WHERE course_id = %s
                ORDER BY users.user_id;
            """, (course['course_id'],))
            teachers = cur.fetchall()
            cur.execute("""
                SELECT
                    users.user_id,
                    users.first_name,
                    users.second_name, 
                    users.last_name
                FROM students
                    JOIN users USING (user_id)
                WHERE course_id = %s
                ORDER BY users.user_id;
            """, (course['course_id'],))
            students = cur.fetchall()
            course.update({
                'students': students,
                'teachers': teachers
            })
            return course

    def add_student_to_course(
        self,
        *,
        user_id: int,
        course_id: int
    ) -> dict:
        """
        Adds a user to the course students group.

        @param user_id:
            Which user must be added.
        @param course_id:
            To what course a user must be added.
        @raise HTTPException:
            If user is already enrolled for course, raises an HTTP exception
            with 409 status code.
        @return:
            The dictionary with values that are added to the 'students' table.
        """
        with self.conn.cursor() as cur:
            self.check_course_exists(course_id=course_id)
            services.UserServices(conn=self.conn).check_user_exists(user_id=user_id)
            try:
                cur.execute("""
                INSERT INTO students (user_id, course_id, has_paid, progress)
                VALUES
                    (%s, %s, 0, 0);
                """, (user_id, course_id))
                self.conn.commit()
            except IntegrityError:
                cur.connection.rollback()
                raise HTTPException(
                    detail="User with id '%s' is already enrolled for course with id '%s'." % (user_id, course_id),
                    status_code=status.HTTP_409_CONFLICT,
                )
            return {
                'user_id': user_id,
                'course_id': course_id,
                'has_paid': False,
                'progress': 0,
            }

    def add_teacher_to_course(
        self,
        *,
        user_id: int,
        course_id: int,
        salary: int | None,
    ) -> dict:
        """
        Adds a user to the course teachers group.

        @param user_id:
            Which user must be added.
        @param course_id:
            To what course a user must be added.
        @param salary:
            The teacher's salary.
        @raise HTTPException:
            If user is already a teacher for the course, raises an HTTP exception
            with 409 status code.
        @return:
            The dictionary with values that are added to the 'teachers' table.
        """
        with self.conn.cursor() as cur:
            self.check_course_exists(course_id=course_id)
            services.UserServices(conn=self.conn).check_user_exists(user_id=user_id)
            try:
                cur.execute("""
                INSERT INTO teachers (user_id, course_id, salary)
                VALUES
                    (%s, %s, %s);
                """, (user_id, course_id, salary))
                self.conn.commit()
            except IntegrityError:
                cur.connection.rollback()
                raise HTTPException(
                    detail="User with id '%s' is already a teacher for course with id '%s'." % (user_id, course_id),
                    status_code=status.HTTP_409_CONFLICT,
                )
            return {
                'user_id': user_id,
                'course_id': course_id,
                'salary': salary,
            }

    def remove_student_from_course(
        self,
        *,
        user_id: int,
        course_id: int,
    ):
        """
        Deletes a student from the course.

        @param user_id:
            Which user must be removed.
        @param course_id:
            From what course student must be removed.
        """
        with self.conn.cursor() as cur:
            self.check_course_exists(course_id=course_id)
            services.UserServices(conn=self.conn).check_user_exists(user_id=user_id)
            cur.execute("""
            DELETE FROM students
            WHERE user_id = %s and course_id = %s;
            """, (user_id, course_id))
            self.conn.commit()

    def remove_teacher_from_course(
        self,
        *,
        user_id: int,
        course_id: int,
    ):
        """
        Deletes a teacher from the course.

        @param user_id:
            Which teacher must be removed.
        @param course_id:
            From what course teacher must be removed.
        """
        with self.conn.cursor() as cur:
            self.check_course_exists(course_id=course_id)
            services.UserServices(conn=self.conn).check_user_exists(user_id=user_id)
            cur.execute("""
            DELETE FROM teachers
            WHERE user_id = %s and course_id = %s;
            """, (user_id, course_id))
            self.conn.commit()

    def increase_student_progress(
        self,
        *,
        user_id: int,
        course_id: int,
        points_amount: float,
    ):
        """
        Increases a student progress in some course and sets a certificate date
        if he has enough progress points.

        @param user_id:
            Which user's progress to increase.
        @param course_id:
            Progress in what course to look up.
        @param points_amount:
            How many points to add for current progress.
        """
        with self.conn.cursor() as cur:
            self.check_course_exists(course_id=course_id)
            services.UserServices(conn=self.conn).check_user_exists(user_id=user_id)
            cur.execute("""
            UPDATE students
            SET progress = IF(
                %(progress)s + progress > 100,
                100,
                progress + %(progress)s
            )
            WHERE user_id = %(user_id)s and course_id = %(course_id)s;
            """, {'progress': points_amount, 'user_id': user_id, 'course_id': course_id})
            cur.execute("""
            UPDATE students
            SET certificate_date = IF(
                students.progress > (
                    SELECT certificate.progress_pass
                    FROM certificate
                    WHERE certificate.course_id = %(course_id)s
                ),
                CURDATE(),
                NULL
            )
            WHERE user_id = %(user_id)s AND course_id = %(course_id)s;
            """, {'user_id': user_id, 'course_id': course_id})
            self.conn.commit()

    def check_course_exists(
        self,
        *,
        course_id: int
    ) -> bool:
        """
        Checks whether the course exists or not.

        @param course_id:
            Which course should be checked.
        @raise HTTPException:
            If the course with provided id doesn't exist, raises an exception
            with 404 status code.
        @return:
            True if course exists.
        """
        with self.conn.cursor() as cur:
            cur.execute("""
            SELECT course_id
            FROM courses
            WHERE course_id = %s;
            """, (course_id,))
            if not cur.fetchone():
                raise HTTPException(
                    detail="Course with id '%s' doesn't exist." % course_id,
                    status_code=status.HTTP_404_NOT_FOUND,
                )
            return True
