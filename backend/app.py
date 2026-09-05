from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import Base, engine, get_db


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Academic Training Management API",
    version="1.0.0",
    description="REST API for academic training management."
)


@app.get("/")
def root():
    return {
        "message": "Academic Training Management API",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post(
    "/departments",
    response_model=schemas.DepartmentResponse
)
def create_department(
    data: schemas.DepartmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_department(
        db,
        data
    )


@app.get(
    "/departments",
    response_model=list[schemas.DepartmentResponse]
)
def list_departments(
    db: Session = Depends(get_db)
):
    return crud.get_departments(db)


@app.post(
    "/students",
    response_model=schemas.StudentResponse
)
def create_student(
    data: schemas.StudentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_student(
        db,
        data
    )


@app.get(
    "/students",
    response_model=list[schemas.StudentResponse]
)
def list_students(
    db: Session = Depends(get_db)
):
    return crud.get_students(db)


@app.post(
    "/courses",
    response_model=schemas.CourseResponse
)
def create_course(
    data: schemas.CourseCreate,
    db: Session = Depends(get_db)
):
    return crud.create_course(
        db,
        data
    )


@app.get(
    "/courses",
    response_model=list[schemas.CourseResponse]
)
def list_courses(
    db: Session = Depends(get_db)
):
    return crud.get_courses(db)


@app.post(
    "/enrollments",
    response_model=schemas.EnrollmentResponse
)
def create_enrollment(
    data: schemas.EnrollmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_enrollment(
        db,
        data
    )


@app.get(
    "/enrollments",
    response_model=list[schemas.EnrollmentResponse]
)
def list_enrollments(
    db: Session = Depends(get_db)
):
    return crud.get_enrollments(db)


@app.post(
    "/grades",
    response_model=schemas.GradeResponse
)
def create_grade(
    data: schemas.GradeCreate,
    db: Session = Depends(get_db)
):
    return crud.create_grade(
        db,
        data
    )


@app.get(
    "/grades",
    response_model=list[schemas.GradeResponse]
)
def list_grades(
    db: Session = Depends(get_db)
):
    return crud.get_grades(db)