class Student:
    def __init__(self,first_name,last_name,student_id,major,year,gpa,email):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.major = major
        self.year = year
        self.gpa = gpa
        self.email = email

    def display(self):
        print("----------------------------------")
        print(f"Student ID: {self.student_id}")
        print(f"Name      : {self.first_name} {self.last_name}")
        print(f"Major     : {self.major}")
        print(f"Year      : {self.year}")
        print(f"GPA       : {self.gpa}")
        print(f"Email     : {self.email}")
        print("----------------------------------")

    def to_dict(self):
        """Converts object instances into JSON-serializable dictionaries."""
        return {
            "student_id": self.student_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "major": self.major,
            "year": self.year,
            "gpa": self.gpa,
            "email": self.email
        }