import sqlite3
from student import Student
import csv

DB_NAME = "students.db"

def setup_database():
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    major TEXT,
    year INTEGER,
    gpa REAL,
    email TEXT
    )
    """)
    connection.commit()
    connection.close()

def add_student(student):
    connection = sqlite3.connect(DB_NAME)

    try:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students VALUES (?,?,?,?,?,?,?)",
            (
                student.student_id,
                student.first_name,
                student.last_name,
                student.major,
                student.year,
                student.gpa,
                student.email,
            ),
        )

        connection.commit()

    finally:
        connection.close()

def get_all_students():
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    rows = cursor.fetchall()
    connection.close()

    all_students = []

    for row in rows:
        student = Student(
            row[1],
            row[2],
            row[0],
            row[3],
            row[4],
            row[5],
            row[6]
            )
        all_students.append(student)


    return all_students


def get_student_by_id(student_id):
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",(student_id,)
    )
    
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    student = Student(
    row[1],
    row[2],
    row[0],
    row[3],
    row[4],
    row[5],
    row[6]
)

    return student

def get_students_by_name(search_term):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    query = "SELECT * FROM students WHERE first_name LIKE ? OR last_name LIKE ?"
    
    cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))

    rows = cursor.fetchall()
    connection.close()

    found_students = []

    for row in rows:
        student = Student(
            row[1],
            row[2],
            row[0],
            row[3],
            row[4],
            row[5],
            row[6]
        )
        found_students.append(student)
        
    return found_students

def update_student_field(student_id, column_name, new_value):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    query = f"UPDATE students SET {column_name} = ? WHERE student_id = ?"
    
    cursor.execute(query, (new_value, student_id))

    connection.commit()
    connection.close()
    
def delete_student(student_id):
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",(student_id,)
    )

    connection.commit()
    connection.close()

def get_database_statistics():
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total_students = cursor.fetchone()[0]

    if total_students == 0:
        connection.close()
        return None

    cursor.execute("SELECT AVG(gpa) FROM students")
    avg_gpa = round(cursor.fetchone()[0],2)

    cursor.execute("SELECT MAX(gpa) FROM students")
    max_gpa = round(cursor.fetchone()[0],2)

    cursor.execute("SELECT MIN(gpa) FROM students")
    min_gpa = round(cursor.fetchone()[0],2)

    cursor.execute("SELECT major, COUNT(*) FROM students GROUP BY major ORDER BY COUNT(*) DESC")
    major_counts = [
        {"major": major, "count": count}
        for major, count in cursor.fetchall()
    ]

    cursor.execute("SELECT COUNT(DISTINCT major) FROM students")
    total_majors = cursor.fetchone()[0]

    connection.close()

    return {
        "total_students": total_students,
        "avg_gpa": avg_gpa,
        "max_gpa": max_gpa,
        "min_gpa": min_gpa,
        "major_counts": major_counts,
        "total_majors": total_majors
    }

def get_students_sorted_by_gpa(descending = True):
    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    if descending:
        query = "SELECT * FROM students ORDER BY gpa DESC"
    else:
        query = "SELECT * FROM students ORDER BY gpa ASC"
    
    cursor.execute(query)
    rows = cursor.fetchall()
    connection.close()

    sorted_students = []

    for row in rows:
        student = Student(
            row[1],
            row[2],
            row[0],
            row[3],
            row[4],
            row[5],
            row[6]
        )
        sorted_students.append(student)
    
    return sorted_students

def does_student_exist(student_id):
    if (get_student_by_id(student_id) is None):
        return False
    else:
        return True
    
def export_students_to_csv():
    students = get_all_students()

    if len(students) == 0:
        return False

    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Student ID",
            "First Name",
            "Last Name",
            "Major",
            "Year",
            "GPA",
            "Email"
        ])

        for student in students:
            writer.writerow([
                student.student_id,
                student.first_name,
                student.last_name,
                student.major,
                student.year,
                student.gpa,
                student.email
            ])

    return True