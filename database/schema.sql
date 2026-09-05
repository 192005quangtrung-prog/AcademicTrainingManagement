CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments(id)
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_code VARCHAR(30) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    major VARCHAR(100) NOT NULL
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code VARCHAR(30) NOT NULL UNIQUE,
    course_name VARCHAR(150) NOT NULL,
    credits INTEGER NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id)
        REFERENCES departments(id)
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    semester VARCHAR(30) NOT NULL,
    FOREIGN KEY (student_id)
        REFERENCES students(id),
    FOREIGN KEY (course_id)
        REFERENCES courses(id)
);

CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_id INTEGER NOT NULL UNIQUE,
    score REAL NOT NULL,
    letter_grade VARCHAR(5) NOT NULL,
    FOREIGN KEY (enrollment_id)
        REFERENCES enrollments(id)
);