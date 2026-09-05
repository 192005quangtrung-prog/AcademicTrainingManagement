import pandas as pd
import requests
import streamlit as st


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Academic Training Management",
    page_icon="🎓",
    layout="wide"
)


def get_data(endpoint):
    response = requests.get(
        f"{API_URL}{endpoint}",
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def post_data(endpoint, payload):
    response = requests.post(
        f"{API_URL}{endpoint}",
        json=payload,
        timeout=10
    )

    response.raise_for_status()

    return response.json()


def main():

    st.title(
        "🎓 Academic Training Management System"
    )

    st.write(
        "Academic management system using "
        "FastAPI, SQLAlchemy and SQLite."
    )

    st.divider()

    menu = st.sidebar.selectbox(
        "Navigation",
        [
            "Dashboard",
            "Students",
            "Courses",
            "Enrollments",
            "Grades"
        ]
    )

    # --------------------------------------------------
    # Dashboard
    # --------------------------------------------------

    if menu == "Dashboard":

        st.header("Dashboard")

        try:

            students = get_data(
                "/students"
            )

            courses = get_data(
                "/courses"
            )

            enrollments = get_data(
                "/enrollments"
            )

            grades = get_data(
                "/grades"
            )

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Students",
                len(students)
            )

            col2.metric(
                "Courses",
                len(courses)
            )

            col3.metric(
                "Enrollments",
                len(enrollments)
            )

            col4.metric(
                "Grades",
                len(grades)
            )

            if grades:

                grade_df = pd.DataFrame(
                    grades
                )

                st.subheader(
                    "Grade Distribution"
                )

                st.bar_chart(
                    grade_df[
                        "letter_grade"
                    ].value_counts()
                )

        except Exception as e:

            st.error(
                f"Cannot connect to API: {e}"
            )

            st.code(
                "uvicorn backend.app:app --reload"
            )

    # --------------------------------------------------
    # Students
    # --------------------------------------------------

    elif menu == "Students":

        st.header("Student Management")

        try:

            students = get_data(
                "/students"
            )

            if students:

                st.dataframe(
                    pd.DataFrame(students),
                    width="stretch",
                    hide_index=True
                )

        except Exception as e:

            st.error(str(e))

        st.subheader("Add Student")

        with st.form(
            "student_form"
        ):

            student_code = st.text_input(
                "Student Code"
            )

            full_name = st.text_input(
                "Full Name"
            )

            email = st.text_input(
                "Email"
            )

            major = st.text_input(
                "Major"
            )

            submitted = st.form_submit_button(
                "Create Student"
            )

            if submitted:

                try:

                    result = post_data(
                        "/students",
                        {
                            "student_code":
                                student_code,
                            "full_name":
                                full_name,
                            "email":
                                email,
                            "major":
                                major
                        }
                    )

                    st.success(
                        f"Created student ID {result['id']}"
                    )

                except Exception as e:

                    st.error(str(e))

    # --------------------------------------------------
    # Courses
    # --------------------------------------------------

    elif menu == "Courses":

        st.header("Course Management")

        try:

            courses = get_data(
                "/courses"
            )

            if courses:

                st.dataframe(
                    pd.DataFrame(courses),
                    width="stretch",
                    hide_index=True
                )

        except Exception as e:

            st.error(str(e))

        st.subheader("Add Course")

        with st.form(
            "course_form"
        ):

            course_code = st.text_input(
                "Course Code"
            )

            course_name = st.text_input(
                "Course Name"
            )

            credits = st.number_input(
                "Credits",
                min_value=1,
                max_value=10,
                value=3
            )

            department_id = st.number_input(
                "Department ID",
                min_value=1,
                value=1
            )

            submitted = st.form_submit_button(
                "Create Course"
            )

            if submitted:

                try:

                    result = post_data(
                        "/courses",
                        {
                            "course_code":
                                course_code,
                            "course_name":
                                course_name,
                            "credits":
                                credits,
                            "department_id":
                                department_id
                        }
                    )

                    st.success(
                        f"Created course ID {result['id']}"
                    )

                except Exception as e:

                    st.error(str(e))

    # --------------------------------------------------
    # Enrollments
    # --------------------------------------------------

    elif menu == "Enrollments":

        st.header("Enrollment Management")

        try:

            enrollments = get_data(
                "/enrollments"
            )

            if enrollments:

                st.dataframe(
                    pd.DataFrame(enrollments),
                    width="stretch",
                    hide_index=True
                )

        except Exception as e:

            st.error(str(e))

        st.subheader(
            "Create Enrollment"
        )

        with st.form(
            "enrollment_form"
        ):

            student_id = st.number_input(
                "Student ID",
                min_value=1,
                value=1
            )

            course_id = st.number_input(
                "Course ID",
                min_value=1,
                value=1
            )

            semester = st.text_input(
                "Semester",
                value="2026-1"
            )

            submitted = st.form_submit_button(
                "Enroll"
            )

            if submitted:

                try:

                    result = post_data(
                        "/enrollments",
                        {
                            "student_id":
                                student_id,
                            "course_id":
                                course_id,
                            "semester":
                                semester
                        }
                    )

                    st.success(
                        f"Enrollment created: {result['id']}"
                    )

                except Exception as e:

                    st.error(str(e))

    # --------------------------------------------------
    # Grades
    # --------------------------------------------------

    elif menu == "Grades":

        st.header("Grade Management")

        try:

            grades = get_data(
                "/grades"
            )

            if grades:

                grade_df = pd.DataFrame(
                    grades
                )

                st.dataframe(
                    grade_df,
                    width="stretch",
                    hide_index=True
                )

                st.metric(
                    "Average Score",
                    f"{grade_df['score'].mean():.2f}"
                )

        except Exception as e:

            st.error(str(e))

        st.subheader(
            "Add Grade"
        )

        with st.form(
            "grade_form"
        ):

            enrollment_id = st.number_input(
                "Enrollment ID",
                min_value=1,
                value=1
            )

            score = st.number_input(
                "Score",
                min_value=0.0,
                max_value=10.0,
                value=7.0,
                step=0.1
            )

            submitted = st.form_submit_button(
                "Save Grade"
            )

            if submitted:

                try:

                    result = post_data(
                        "/grades",
                        {
                            "enrollment_id":
                                enrollment_id,
                            "score":
                                score
                        }
                    )

                    st.success(
                        f"Grade saved: {result['letter_grade']}"
                    )

                except Exception as e:

                    st.error(str(e))


if __name__ == "__main__":
    main()