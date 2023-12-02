from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
from datetime import date

def test_find_with_students(db_connection):
    db_connection.seed("seeds/student_directory_2.sql")
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    
    assert cohort == Cohort(1, 'A1', date(2020, 1, 1), students=[
        Student(4, "Andy Notha-Test", 1),
        Student(5, "Yetta Notha-Test", 1),
    ])