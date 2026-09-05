from sqlalchemy.orm import Session

from . import models, schemas


def create_department(
    db: Session,
    data: schemas.DepartmentCreate
):
    department = models.Department(
        name=data.name
    )

    db.add(department)
    db.commit()
    db.refresh(department)

    return department


def get_departments(db: Session):
    return (
        db.query(models.Department)
        .order_by(models.Department.id)
        .all()
    )


def create_student(
    db: Session,
    data: schemas.StudentCreate
):
    student = models.Student(
        student_code=data.student_code,
        full_name=data.full_name,
        email=data.email,
        major=data.major
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student


def get_students(db: Session):
    return (
        db.query(models.Student)
        .order_by(models.Student.id)
        .all()
    )


def create_course(
    db: Session,
    data: schemas.CourseCreate
):
    course = models.Course(
        course_code=data.course_code,
        course_name=data.course_name,
        credits=data.credits,
        department_id=data.department_id
    )

    db.add(course)
    db.commit()
    db.refresh(course)

    return course


def get_courses(db: Session):
    return (
        db.query(models.Course)
        .order_by(models.Course.id)
        .all()
    )


def create_enrollment(
    db: Session,
    data: schemas.EnrollmentCreate
):
    enrollment = models.Enrollment(
        student_id=data.student_id,
        course_id=data.course_id,
        semester=data.semester
    )

    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return enrollment


def get_enrollments(db: Session):
    return (
        db.query(models.Enrollment)
        .order_by(models.Enrollment.id)
        .all()
    )


def calculate_letter_grade(
    score: float
):
    if score >= 8.5:
        return "A"

    if score >= 7.0:
        return "B"

    if score >= 5.5:
        return "C"

    if score >= 4.0:
        return "D"

    return "F"


def create_grade(
    db: Session,
    data: schemas.GradeCreate
):
    letter_grade = calculate_letter_grade(
        data.score
    )

    grade = models.Grade(
        enrollment_id=data.enrollment_id,
        score=data.score,
        letter_grade=letter_grade
    )

    db.add(grade)
    db.commit()
    db.refresh(grade)

    return grade


def get_grades(db: Session):
    return (
        db.query(models.Grade)
        .order_by(models.Grade.id)
        .all()
    )