# Student Management System

---

## 🌐 Live Demo

**Frontend:** https://student-management-system-psi-blue.vercel.app

**Backend API:** https://student-management-system-bmey.onrender.com

---

![Python](https://img.shields.io/badge/Python-3-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Pytest](https://img.shields.io/badge/Tests-pytest-green)
![REST API](https://img.shields.io/badge/API-REST-blueviolet)
![React](https://img.shields.io/badge/React-19-61DAFB)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-4.x-38BDF8)
![Axios](https://img.shields.io/badge/Axios-HTTP%20Client-5A29E4)
![Tests](https://img.shields.io/badge/47%20Tests-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

This project began as a command-line application and gradually evolved into a complete full-stack web application. It showcases the progression from object-oriented programming and relational database management to REST API development and a modern React frontend.

The application allows users to manage student records through a responsive React frontend while exposing a fully tested REST API backed by SQLite. It demonstrates how a traditional Python CLI application can evolve into a complete full-stack software project.

---

## Highlights

- Modern React frontend with Tailwind CSS
- RESTful Flask API with 10 endpoints
- Command-line application with complete CRUD functionality
- SQLite relational database integration
- 47 automated tests using pytest
- CSV export functionality
- Modular object-oriented architecture
- Robust input validation and exception handling
- Interactive dashboard with live statistics
- Responsive React user interface

---

## Tech Stack

### Frontend:
- React
- Tailwind CSS
- Axios

### Backend:
- Flask
- SQLite

### Testing:
- Pytest

---

## ✨ Features

### 🌐 Web Application
* Modern responsive React interface
* Responsive navigation
* Dashboard with live database statistics

* Add new students
* View all students
* Search by Student ID
* Search by student name
* Update student information
* Delete students with confirmation
* Sort students by GPA
* Export student records to CSV

* Loading and error handling
* CSV download through browser
* Clean responsive UI

### 📊 Dashboard

* Total Students
* Average GPA
* Highest GPA
* Lowest GPA
* Number of Unique Majors
* Quick Actions
  * Add Student
  * View Students
  * Export CSV

### Command-Line Application

* Add new students to a SQLite database
* View all students
* Search students by **Student ID** or **Name**
* Update any student field through a dynamic SQL update system
* Delete students with confirmation prompts
* View students sorted by GPA using SQL `ORDER BY`

  * Ascending
  * Descending
* View a **Database Statistics Dashboard**, including:

  * Total students
  * Total unique majors
  * Average GPA
  * Highest GPA
  * Lowest GPA
  * Student distribution by major
* Export all student records to a CSV file

### REST API

* Retrieve all students
* Retrieve a student by Student ID
* Search students by name
* Retrieve students sorted by GPA (ascending or descending)
* Retrieve database statistics
* Export student records to CSV
* Create new students
* Update existing student records
* Delete student records
* JSON request and response handling
* Proper error responses
* CSV file download
* Proper HTTP status codes
* Robust request validation
* Duplicate Student ID protection

### Validation & Software Design

* Email validation using Regular Expressions (Regex)
* GPA validation (0.0–4.0)
* Graduation year validation
* Student name validation
* Prevent duplicate Student IDs
* Object-oriented design using a `Student` class
* Modular project architecture with reusable utility functions
* Frontend form validation
* Server-side validation

### Testing

The backend includes a comprehensive automated test suite built with pytest.

The frontend was manually tested throughout development to verify functionality, responsiveness, and user interactions.

#### Database Tests
* CRUD operations
* Student search
* GPA sorting
* Database statistics
* Duplicate ID prevention
* CSV export
* Empty database handling
#### API Tests
* All REST endpoints
* Success responses
* Error responses
* Request validation
* HTTP status codes
* JSON responses
* CSV download endpoint

#### Total Tests

✅ 47 Passing Tests

---

## Technologies Used

### Frontend

- React
- React Router
- Axios
- Tailwind CSS
- JavaScript

### Backend

- Python
- Flask
- SQLite
- SQL

### Testing

- Pytest
- Flask Test Client

### Development Tools

- Git
- GitHub
- VS Code
- Thunder Client
- Vite

---

## Project Structure

```text
Student-Management-System/
│
├── frontend/
│   ├── public/
│   │   ├── favicon.svg
│   │   └── icons.svg
│   │
│   ├── src/
│   │   ├── components/
|   |   |   |──dashboard/
|   |   |   └──navbar/
|   |   |
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
│   ├── eslint.config.js
│   └── .gitignore
│
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   └── test_database.py
│
├── app.py                  # Flask REST API
├── database.py             # Database operations and SQL queries
├── student.py              # Student model
├── utils.py                # Validation helper functions
├── menu.py                 # Command-line interface
├── main.py                 # CLI entry point
│
├── requirements.txt
├── pytest.ini
├── students.db             # SQLite database (generated at runtime)
├── students.csv            # Exported CSV (generated on demand)
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## REST API Endpoints

| Method | Endpoint                       | Description                           |
| ------ | ------------------------------ | ------------------------------------- |
| GET    | `/`                            | API status                            |
| GET    | `/students`                    | Retrieve all students                 |
| GET    | `/students/<student_id>`       | Retrieve a student by Student ID      |
| GET    | `/students/search?name=<name>` | Search students by first or last name |
| GET    | `/students/sorted?order=asc`   | Retrieve students sorted by GPA       |
| GET    | `/students/statistics`         | Retrieve database statistics          |
| GET    | `/students/export`             | Export all students to CSV            |
| POST   | `/students`                    | Create a new student                  |
| PUT    | `/students/<student_id>`       | Update an existing student            |
| DELETE | `/students/<student_id>`       | Delete a student                      |

---

## Architecture

The project follows a modular full-stack architecture with a clear separation between the frontend, backend, and database layers.

### Frontend

- React
- React Router
- Axios
- Tailwind CSS
- Component-based architecture

### Backend

- Flask REST API
- SQLite database
- Object-oriented Student model
- Input validation utilities

### Testing

- Pytest
- Flask Test Client
- Automated API and database testing

---

## Project Evolution

* ✅ Command-Line Application
* ✅ SQLite Database
* ✅ CRUD Operations
* ✅ Statistics Dashboard
* ✅ CSV Export
* ✅ REST API
* ✅ Automated Testing
* ✅ React Frontend
* ✅ Tailwind CSS UI
* ✅ Full-Stack Integration
* ⬜ Authentication
* ⬜ Deployment

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/aryalankit121/Student-Management-System.git
```

### 2. Navigate into the project

```bash
cd Student-Management-System
```

### 3. Install dependencies

```bash
pip install flask pytest
```

---

### Run the Command-Line Application

```bash
python main.py
```

---

### Backend

```bash
pip install -r requirements.txt

python app.py
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

The SQLite database will automatically be created the first time the application is run if it does not already exist.

---

## Running the Backend Test Suite

Execute the automated tests with:

```bash
pytest -v
```

The automated test suite covers both the database layer and the REST API.

### Database Tests

- CRUD operations
- Student lookup
- Student search
- GPA sorting
- Database statistics
- CSV export
- Duplicate ID protection
- Empty database export handling

### REST API Tests

- All GET endpoints
- POST endpoint
- PUT endpoint
- DELETE endpoint
- Request validation
- Error handling
- HTTP status codes
- JSON request/response handling
- CSV export endpoint

---

## Skills Demonstrated

This project provided hands-on experience with:

* Object-Oriented Programming (OOP)
* Full-Stack Web Development
* SQL and relational databases
* SQLite integration with Python
* CRUD application development
* REST API development
* Flask
* JSON serialization
* HTTP request handling
* HTTP methods (GET, POST, PUT, DELETE)
* Query parameter handling
* Modular software architecture
* Input validation
* Regular Expressions (Regex)
* CSV file handling
* Exception handling
* Automated testing with **pytest**
* Flask testing
* Flask test client
* RESTful API Design
* REST API testing
* Test-driven validation
* Manual API testing using Thunder Client
* Frontend-Backend Integration
* React
* Tailwind CSS
* Axios
* Responsive Design
* Component-Based Architecture
* React Hooks
* State Management
* Git version control
* GitHub workflow

---

## Planned Improvements

* Authentication and user login
* Advanced search filters
  * Major
  * Graduation Year
  * GPA range
* Pagination for API responses
* Docker containerization
* API documentation with Swagger/OpenAPI

---

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

View live database statistics and access common actions.

---

### Student Records

![Students](screenshots/students-page.png)

Browse, search, edit, delete, sort, and export student records.

---

### Add Student

![Add Student](screenshots/add-student.png)

Validated form for creating new student records.

---

### Edit Student

![Edit Student](screenshots/edit-student.png)

Update student information with real-time validation.

---

### Search & Student Management

![Search](screenshots/search.png)

Search students instantly by Student ID or name.

---

## Author

**Ankit Aryal**

Computer Science Student  
Catawba College

GitHub: https://github.com/aryalankit121

---

## License

This project is licensed under the MIT License. See the **LICENSE** file for details.
