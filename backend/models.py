from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False,
        unique=True
    )

    teachers = relationship(
        "Teacher",
        back_populates="department"
    )

    courses = relationship(
        "Course",
        back_populates="department"
    )


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(120),
        unique=True,
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="teachers"
    )


class Student(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_code = Column(
        String(30),
        unique=True,
        nullable=False,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(120),
        unique=True,
        nullable=False
    )

    major = Column(
        String(100),
        nullable=False
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="student"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    course_code = Column(
        String(30),
        unique=True,
        nullable=False,
        index=True
    )

    course_name = Column(
        String(150),
        nullable=False
    )

    credits = Column(
        Integer,
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="courses"
    )

    enrollments = relationship(
        "Enrollment",
        back_populates="course"
    )


class Enrollment(Base):
    __tablename__ = "enrollments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        nullable=False
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False
    )

    semester = Column(
        String(30),
        nullable=False
    )

    student = relationship(
        "Student",
        back_populates="enrollments"
    )

    course = relationship(
        "Course",
        back_populates="enrollments"
    )

    grade = relationship(
        "Grade",
        back_populates="enrollment",
        uselist=False,
        cascade="all, delete-orphan"
    )


class Grade(Base):
    __tablename__ = "grades"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    enrollment_id = Column(
        Integer,
        ForeignKey("enrollments.id"),
        unique=True,
        nullable=False
    )

    score = Column(
        Float,
        nullable=False
    )

    letter_grade = Column(
        String(5),
        nullable=False
    )

    enrollment = relationship(
        "Enrollment",
        back_populates="grade"
    )