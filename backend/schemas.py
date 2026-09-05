from pydantic import BaseModel, ConfigDict, Field


class DepartmentCreate(BaseModel):
    name: str


class DepartmentResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class TeacherCreate(BaseModel):
    full_name: str
    email: str
    department_id: int


class TeacherResponse(BaseModel):
    id: int
    full_name: str
    email: str
    department_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class StudentCreate(BaseModel):
    student_code: str
    full_name: str
    email: str
    major: str


class StudentResponse(BaseModel):
    id: int
    student_code: str
    full_name: str
    email: str
    major: str

    model_config = ConfigDict(
        from_attributes=True
    )


class CourseCreate(BaseModel):
    course_code: str
    course_name: str
    credits: int = Field(
        ge=1,
        le=10
    )
    department_id: int


class CourseResponse(BaseModel):
    id: int
    course_code: str
    course_name: str
    credits: int
    department_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class EnrollmentCreate(BaseModel):
    student_id: int
    course_id: int
    semester: str


class EnrollmentResponse(BaseModel):
    id: int
    student_id: int
    course_id: int
    semester: str

    model_config = ConfigDict(
        from_attributes=True
    )


class GradeCreate(BaseModel):
    enrollment_id: int
    score: float = Field(
        ge=0,
        le=10
    )


class GradeResponse(BaseModel):
    id: int
    enrollment_id: int
    score: float
    letter_grade: str

    model_config = ConfigDict(
        from_attributes=True
    )