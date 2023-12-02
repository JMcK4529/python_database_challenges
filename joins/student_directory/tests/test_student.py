from lib.student import Student

def test_student_constructs():
    id, name, cohort_id = 1, "Jeff Test", 3
    student = Student(id, name, cohort_id)
    for attribute in zip([student.id, student.name, student.cohort_id],
                         [id, name, cohort_id]):
        assert attribute[0] == attribute[1]

def test_student_repr_magic_method():
    id, name, cohort_id = 1, "Jeff Test", 3
    student = Student(id, name, cohort_id)
    assert str(student) == "Student(1, Jeff Test, 3)"

def test_student_eq_magic_method():
    id, name, cohort_id = 1, "Jeff Test", 3
    student1 = Student(id, name, cohort_id)
    student2 = Student(id, name, cohort_id)
    assert student1 == student2