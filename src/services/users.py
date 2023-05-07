from pymysql import Connection


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

    def get_all_teachers(self) -> list[dict | None]:
        with self.conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT users.user_id,
                    users.first_name, 
                    users.second_name,
                    users.last_name,
                    teachers.salary
                FROM users JOIN teachers USING (user_id)
                ORDER BY user_id;                
                """
            )
            return cursor.fetchall()
