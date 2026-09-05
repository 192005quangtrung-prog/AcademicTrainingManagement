# 🎓 Academic Training Management System

A web-based academic training management system for managing students, courses, enrollments, grades, and academic information.

The project demonstrates a complete application architecture using **REST API, SQL database, ORM, and interactive web dashboard**.

## 📌 Overview

The system is designed to support basic academic management operations:

```text
Students
    │
    ├── Enrollments ─── Courses
    │
    └── Grades

Departments
    │
    ├── Teachers
    └── Courses
```

The application follows a layered architecture:

```text
Streamlit Dashboard
        │
        │ HTTP Requests
        ▼
FastAPI REST API
        │
        ▼
SQLAlchemy ORM
        │
        ▼
SQLite Database
```

## ✨ Features

* Student management
* Department management
* Teacher management
* Course management
* Course enrollment management
* Grade management
* Automatic letter-grade classification
* Academic statistics dashboard
* RESTful API
* Interactive Swagger API documentation
* SQL database schema

## 🛠️ Technology Stack

| Category             | Technology        |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Backend              | FastAPI           |
| ORM                  | SQLAlchemy        |
| Database             | SQLite            |
| Data Validation      | Pydantic          |
| Frontend             | Streamlit         |
| HTTP Client          | Requests          |
| Data Processing      | Pandas            |
| API Documentation    | Swagger / OpenAPI |

## 📁 Project Structure

```text
Academic Training Management System/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
│
├── frontend/
│   └── app.py
│
├── database/
│   └── schema.sql
│
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

The SQLite database file is generated locally when the backend starts and is excluded from Git tracking.

## 🗄️ Database Design

The system contains the following main entities:

### Department

Stores academic department information.

### Teacher

Stores lecturer information and its relationship with departments.

### Student

Stores:

* Student code
* Full name
* Email
* Major

### Course

Stores:

* Course code
* Course name
* Credits
* Department

### Enrollment

Connects students with courses and stores semester information.

### Grade

Stores the score of an enrollment and its corresponding letter grade.

Relationship overview:

```text
Department
   │
   ├──────────────► Teacher
   │
   └──────────────► Course
                       │
                       ▼
                    Enrollment
                       ▲
                       │
                    Student
                       │
                       ▼
                     Grade
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/192005quangtrung-prog/AcademicTrainingManagement.git
cd AcademicTrainingManagement
```

### 2. Create virtual environment

Windows:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## ▶️ Run Backend

Start the FastAPI server:

```powershell
uvicorn backend.app:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

## 🖥️ Run Frontend

Open another terminal and activate the virtual environment.

Run:

```powershell
streamlit run frontend/app.py
```

Open:

```text
http://localhost:8501
```

## 🔌 REST API

Main endpoints:

```text
Departments
GET  /departments
POST /departments

Students
GET  /students
POST /students

Courses
GET  /courses
POST /courses

Enrollments
GET  /enrollments
POST /enrollments

Grades
GET  /grades
POST /grades
```

## 🧪 Example API Request

Create a student:

```json
{
  "student_code": "SV001",
  "full_name": "Nguyen Van A",
  "email": "sv001@example.com",
  "major": "Artificial Intelligence"
}
```

The request can be tested directly through the Swagger interface:

```text
http://127.0.0.1:8000/docs
```

## 📊 Dashboard

The Streamlit dashboard provides:

### Dashboard

Displays:

* Number of students
* Number of courses
* Number of enrollments
* Number of grades
* Grade distribution

### Students

Allows viewing and adding students.

### Courses

Allows viewing and adding courses.

### Enrollments

Allows creating course enrollments.

### Grades

Allows storing scores and displaying average scores.

## 🔄 Application Workflow

```text
User
 │
 ▼
Streamlit UI
 │
 │ HTTP POST / GET
 ▼
FastAPI
 │
 ▼
Pydantic Validation
 │
 ▼
CRUD Layer
 │
 ▼
SQLAlchemy ORM
 │
 ▼
SQLite Database
```

## 🎯 Learning Objectives

This project demonstrates practical knowledge of:

* Relational database design
* Primary keys and foreign keys
* Entity relationships
* CRUD operations
* SQLAlchemy ORM
* REST API development
* API request/response validation
* FastAPI
* Swagger/OpenAPI
* Streamlit dashboard development
* Backend/frontend integration

## 🔮 Future Improvements

* User authentication and authorization
* Role-based access control
* Advanced student search and filtering
* Course scheduling
* Attendance management
* GPA calculation
* Semester-based academic reports
* Pagination and database indexing
* PostgreSQL/MySQL deployment
* Automated unit and integration tests
* Docker deployment

## 👨‍💻 Author

**Nguyen Quang Trung**

GitHub:

https://github.com/192005quangtrung-prog

Repository:

https://github.com/192005quangtrung-prog/AcademicTrainingManagement

## 📄 License

This project is intended for educational and portfolio purposes.
