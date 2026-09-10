from student import Student
import database
from utils import get_valid_integer, get_valid_float, get_valid_email

def print_menu():
    print()
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update a Student's data")
    print("5. Delete a Student")
    print("6. Export Students to CSV")
    print("7. View Students sorted based on GPA")
    print("8. View Database Statistics")
    print("9. Exit ")
    print()

def start():
    print("---------Welcome to the Student-Management-System---------")
    print()

    while True:
        #menu
        print()
        print("Here's the menu:")
        print_menu()

        choice = get_valid_integer(
            "Enter a number (1-9) that aligns with your choice: ",
            "Invalid choice! Please enter a number."
        )

        if choice == 1:
            while True:
                # We use the helper function just for the ID
                student_id = get_valid_integer(
                    "Enter the Student ID (example: 1111): ",
                    "Invalid ID! Please enter a number for ID, not text."
                )

                if database.does_student_exist(student_id):
                    print("\033[91m\nError: A student with this ID already exists!\033[0m")
                else:
                    break
            
            first_name = input("Enter the First name: ")
            last_name = input("Enter the Last name: ")
            major = input("Enter the Major: ")
            year = get_valid_integer("Enter the Year of Graduation: ", "Error: Year must be a number.")
            gpa = get_valid_float(
                "Enter the GPA: ",
                "Error: GPA must be a number with decimals.",
                min_value=0.0,
                max_value=4.0
            )
            email = get_valid_email(
                "Enter the email address: ",
                "Invalid email format!"
            )
            
            student = Student(first_name, last_name, student_id, major, year, gpa, email)
            database.add_student(student)
            
            print("\033[92m\nSuccess: Student Successfully Added!\033[0m")

        elif choice == 2:
            students = database.get_all_students()
            if len(students) == 0:
                print("\033[93m\nNo students in the database.\033[0m")
            else:
                print("\033[92m\nViewing all students in the database:\033[0m")
                for student in students:
                    student.display()
        
        elif choice == 3:
            print("\nHow would you like to search?")
            print("1. Search by Student ID")
            print("2. Search by Name")
        
            search_choice = get_valid_integer(
            "Choose an option (1-2): ",
            "Invalid choice! Please enter a number."
            )
        
            if search_choice == 1:
                student_id = get_valid_integer(
                    "What is the Student ID of the Student that you would like to search for (example: 1111): ",
                    "Invalid ID! Please enter a number for ID, not text."
                )
            
                student = database.get_student_by_id(student_id)

                if student is None:
                    print("\033[91m\nError: Student not found with that ID.\033[0m")
                else:
                    student.display()
                
            elif search_choice == 2:
                name_query = input("Enter the first or last name to search for: ").strip()
                results = database.get_students_by_name(name_query)
                
                if len(results) == 0:
                    print("\033[91m\nError: No students found matching that name.\033[0m")
                else:
                    print(f"\033[92m\nFound {len(results)} student(s):\033[0m")
                    for student in results:
                        student.display()
            else:
                print("\033[91m\nInvalid choice! Returning to menu...\033[0m")

        elif choice == 4:
            student_id = get_valid_integer(
            "What is the Student ID of the Student that you would like to Update (example: 1111): ",
            "Invalid ID! Please enter a number for ID, not text."
            )
            
            if (database.does_student_exist(student_id)):
                print("\nWhat would you like to update from the menu: ")
                print("1. First Name")
                print("2. Last Name")
                print("3. Major")
                print("4. Year")
                print("5. GPA")
                print("6. Email")
                
                update_choice = get_valid_integer(
                    "Choose the number (1-6) that aligns with your interest: ",
                    "Invalid choice! Please enter a number (1-6)."
                )

                if update_choice == 1:
                    new_first_name = input("What is the updated First Name: ")
                    database.update_student_field(student_id, "first_name", new_first_name)

                elif update_choice == 2:
                    new_last_name = input("What is the updated Last Name: ")
                    database.update_student_field(student_id, "last_name", new_last_name)
                
                elif update_choice == 3:
                    new_major = input("What is the updated Major: ")
                    database.update_student_field(student_id, "major", new_major)
                
                elif update_choice == 4:
                    new_year = get_valid_integer("What is the updated Year: ", "Error: Year must be a number.")
                    database.update_student_field(student_id, "year", new_year)

                elif update_choice == 5:
                    new_gpa = get_valid_float(
                        "Enter the updated GPA: ",
                        "Error: GPA must be a number with decimals.",
                        min_value=0.0,
                        max_value=4.0
                    )
                    database.update_student_field(student_id, "gpa", new_gpa)
    
                elif update_choice == 6:
                    new_email = get_valid_email(
                        "Enter the updated email: ",
                        "Invalid email format!"
                    )
                    database.update_student_field(student_id, "email", new_email)
                
                else:
                    print("\033[91m\nPlease enter a number (1-6) that aligns with the menu...\033[0m")
                    continue
                
                print("\033[92m\nSuccess: Student Successfully Updated!\033[0m")
                print("\nHere is the Student's updated data: ")
                student = database.get_student_by_id(student_id)
                student.display()
            else:
                print("\033[91m\nError: Student not found.\033[0m")

        elif choice == 5:
            student_id = get_valid_integer(
                "What is the Student ID of the Student that you would like to Delete (example: 1111): ",
                "Invalid ID! Please enter a number for ID, not text."
            )

            student = database.get_student_by_id(student_id)

            if student is None:
                print("\033[91m\nError: Student not found.\033[0m")
            else:
                student.display()
            
                confirm = input("\033[91mAre you sure you want to permanently delete this student? (y/n): \033[0m").strip().lower()
                
                if confirm in ("y", "yes"):
                    database.delete_student(student_id)
                    print("\033[92m\nSuccess: Student Successfully Deleted!\033[0m")
                else:
                    print("\nDeletion canceled. Returning to main menu.")
        
        elif choice == 6:
            print("\nExporting the student database to CSV...")

            try:
                result = database.export_students_to_csv()

                if result:
                    print("\033[92m\nSuccess: Data exported to 'students.csv'!\033[0m")

                else:
                    print("\033[93m\nNo students in the database to export.\033[0m")

            except PermissionError:
                print("\033[91m\nError: Permission denied. Please close 'students.csv' if it is open in another program and try again.\033[0m")

            except OSError as error:
                print(f"\033[91m\nAn unexpected file error occurred: {error}\033[0m")

        elif choice == 7:
            print("\nHow do you want the students to be sorted: ")
            print("1. From Highest to Lowest (Descending)")
            print("2. From Lowest to Highest (Ascending)")

            sort_choice = get_valid_integer(
            "Choose an option (1-2): ",
            "Invalid choice! Please enter a number."
            )
        
            if sort_choice == 1:
                students = database.get_students_sorted_by_gpa(descending = True)
            elif sort_choice == 2:
                students = database.get_students_sorted_by_gpa(descending = False)
            else:
                print("\033[91m\nInvalid choice! Returning to menu...\033[0m")
                continue
            
            if len(students) == 0:
                print("\033[93m\nNo students in the database.\033[0m")
            else:
                print(f"\033[92m\nShowing {len(students)} student(s) sorted by GPA:\033[0m")
                for student in students:
                    student.display()

        elif choice == 8:
            stats = database.get_database_statistics()
            if stats is None:
                print("\033[93m\nNo students in the database to analyze.\033[0m")
            else:
                print("\nCalculating Database Statistics...")
                print("\033[96m")
                print(" DATABASE STATISTICS ".center(40, "="))
                print(f"\n{'Total Students Enrolled:':30} {stats['total_students']}")
                print(f"{'Total Unique Majors:':30} {stats['total_majors']}")
                print(f"\n{'Overall Average GPA:':30} {stats['avg_gpa']}")
                print(f"{'Highest GPA:':30} {stats['max_gpa']}")
                print(f"{'Lowest GPA:':30} {stats['min_gpa']}")
                print("-" * 40)

                print("\nStudent Distribution by Major:")
                print("-" * 40)
                for major,count in stats['major_counts']:
                    print(f"  • {major:<20}: {count} student(s)")
                print()
                print("=" * 40)
                print("\033[0m")

        elif choice == 9:
            quit_confirmation = input("\033[91m\nAre you sure you want to quit? Press 1 if you want to quit; Press any other key to continue: \033[0m")
            
            if(quit_confirmation == '1'):
                print("You chose to quit the Program. Have a great day. Exiting....")
                break
            else:
                continue
        
        else:
            print("\033[91mInvalid choice! Please choose a number (1-9) from menu...\033[0m")