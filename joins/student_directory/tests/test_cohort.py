from lib.cohort import Cohort
from unittest.mock import MagicMock

def test_cohort_constructs():
    students_mock = [MagicMock() for _ in range(3)]
    for student_mock in students_mock:
        student_mock.__eq__.return_value = True

    id, name, starting_date, students = (1, "Test Cohort",
                                         "2023-12-01", students_mock)
    
    cohort = Cohort(id, name, starting_date, students_mock)
    for attribute in zip([cohort.id, cohort.name,
                          cohort.starting_date, cohort.students],
                         [id, name, starting_date, students]):
        assert attribute[0] == attribute[1]

def test_cohort_repr_magic_method():
    id, name, starting_date = 1, "Test Cohort", "2023-12-01"
    cohort = Cohort(id, name, starting_date)
    assert str(cohort) == "Cohort(1, Test Cohort, 2023-12-01, students=[])"

def test_cohort_eq_magic_method():
    students_mock = [MagicMock() for i in range(3)]
    for student_mock in students_mock:
        student_mock.__eq__.return_value = True
    id, name, starting_date, students = (1, "Test Cohort",
                                         "2023-12-01", students_mock)
    cohort1 = Cohort(id, name, starting_date, students)
    cohort2 = Cohort(id, name, starting_date, students)
    assert cohort1 == cohort2