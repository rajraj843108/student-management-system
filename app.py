from flask import Flask, request
from flask_cors import CORS
from flask import send_file
import database
from student import Student
import sqlite3
import utils
import os

app = Flask(__name__)
CORS(app)

database.setup_database()

ALLOWED_FIELDS = {
    "first_name",
    "last_name",
    "major",
    "year",
    "gpa",
    "email"
}

@app.route("/")
def home():
    return {
        "project": "Student Management System API",
        "status": "online",
        "version": "1.0.1",
        "author": "Ankit Aryal"
    }

@app.route("/students")
def get_students():
    students = database.get_all_students()

    return [student.to_dict() for student in students]

@app.route("/students/<int:student_id>")
def get_student_by_student_id(student_id):
    student = database.get_student_by_id(student_id)
    if student is None:
        return {"error": "Student not found"},404

    return student.to_dict()

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student_by_student_id(student_id):

    if not database.does_student_exist(student_id):
        return {"error": "Student not found"},404
    
    student = database.get_student_by_id(student_id)
    
    database.delete_student(student_id)

    return{
        "message": "Student successfully deleted",
        "student": student.to_dict()
        }, 200

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student_by_student_id(student_id):
    data = request.json

    if not data:
        return {"error": "Malformed or missing JSON payload"}, 400

    if not database.does_student_exist(student_id):
        return {"error": "Student not found"},404
    
    for column_name, new_value in data.items():
        if column_name not in ALLOWED_FIELDS:
            return {"error": f"Invalid field: {column_name}"}, 400
        
        if column_name == "first_name":
            if not utils.is_valid_name(new_value):
                return {"error": "Invalid First Name"}, 400
            
        if column_name == "last_name":
            if not utils.is_valid_name(new_value):
                return {"error": "Invalid Last Name"}, 400

        if column_name == "year":
            if not utils.is_valid_year(new_value):
                return {"error": "Invalid Year"}, 400

        if column_name == "gpa":
            if not utils.is_valid_gpa(new_value):
                return {"error": "Invalid GPA"}, 400

        if column_name == "email":
            if not utils.is_valid_email(new_value):
                return {"error": "Invalid email format"}, 400

        database.update_student_field(student_id, column_name, new_value)
    
    updated_student = database.get_student_by_id(student_id)

    return {
        "message": "Student updated successfully",
        "student": updated_student.to_dict()
    }, 200

@app.route("/students/statistics")
def get_students_statistics():
    statistics = database.get_database_statistics()

    if statistics is None:
        return{
            "error": "No Students in the database"
        }, 404
    
    return{
        "message": "Student statistics successfully loaded",
        "statistics": statistics
    }, 200

@app.route("/students/sorted")
def get_students_in_order():
    order = request.args.get("order")
    if order == "asc":
        students = database.get_students_sorted_by_gpa(descending=False)
        return [student.to_dict() for student in students]
    elif order == "desc":
        students = database.get_students_sorted_by_gpa(descending=True)
        return [student.to_dict() for student in students]
    else:
        return {
            "error": "Invalid order. Use 'asc' or 'desc'."
        },400
    
@app.route("/students/search")
def get_students_by_name():
    name = request.args.get("name")
    if not utils.is_valid_name(name):
        return{
            "error": "Invalid Name format"
        }, 400
    students = database.get_students_by_name(name)
    if not students:
        return{
            "error": "No students found"
        }, 404

    return [student.to_dict() for student in students]
    
@app.route("/students/export")
def export_to_csv():
    try:
        success = database.export_students_to_csv()

        if not success:
            return {"error": "No students available to export."}, 400

        return send_file(
            "students.csv",
            as_attachment=True,
            download_name="students.csv",
            mimetype="text/csv"
        )

    except PermissionError:
        return {
            "error": "Permission denied. Close students.csv and try again."
        }, 500

    except OSError as e:
        return {
            "error": f"File system error: {e}"
        }, 500

@app.route("/students", methods=["POST"])
def post_student():
    data = request.get_json(silent=True)

    if not data:
        return {"error": "Malformed or missing JSON payload"}, 400

    try:
        if not utils.is_valid_name(data["first_name"]):
            return {"error": "Invalid First Name"}, 400

        if not utils.is_valid_name(data["last_name"]):
            return {"error": "Invalid Last Name"}, 400

        if not utils.is_valid_year(data["year"]):
            return {"error": "Invalid Year"}, 400

        if not utils.is_valid_gpa(data["gpa"]):
            return {"error": "Invalid GPA"}, 400

        if not utils.is_valid_email(data["email"]):
            return {"error": "Invalid email format"}, 400

        student = Student(
            first_name=data["first_name"],
            last_name=data["last_name"],
            student_id=data["student_id"],
            major=data["major"],
            year=data["year"],
            gpa=data["gpa"],
            email=data["email"],
        )
        
        database.add_student(student)
        
        return {
            "message": "Student added successfully",
            "student": student.to_dict()
        }, 201
        
    except KeyError as e:
        return {
            "error": f"Missing required field: {e.args[0]}"
        }, 400
    
    except sqlite3.IntegrityError:
        return {
            "error": "Student ID already exists."
        }, 409

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )


