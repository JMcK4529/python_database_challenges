from lib.cohort import Cohort
from lib.student import Student

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            """SELECT cohorts.id AS cohort_id, cohorts.name AS cohort_name,
            cohorts.starting_date, students.id AS student_id, students.name AS 
            student_name
            FROM cohorts JOIN students 
            ON cohorts.id = students.cohort_id
            WHERE cohorts.id = %s;""",
            [cohort_id]
            )
        # students = [Student(
        #                     row["student_id"], row["student_name"],
        #                     row["cohort_id"]
        #                     )
        #                      for row in rows]
        students = []
        for row in rows:
            students.append(Student(
                             row["student_id"], row["student_name"],
                             row["cohort_id"]
                             ))
        cohort = Cohort(rows[0]["cohort_id"], rows[0]["cohort_name"], 
                        rows[0]["starting_date"], students)
        print(type(rows[0]["starting_date"]))
        return cohort