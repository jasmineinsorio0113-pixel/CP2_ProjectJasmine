# STacy Oliveros

students = []  # Array to store student records

# Display menu
def display_menu():
    print("===== Student Information System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

# Add student
def add_student():
    name = input("Enter student name: ").strip()
    studentid = input("Enter student ID: ").strip()
    age = input("Enter student age: ").strip()
    birthday = input("Enter student birthday (YYYY-MM-DD): ").strip()
    course = input("Enter student course: ").strip()

    # Input validation
    if not name or not studentid.isdigit() or not age.isdigit() or not course:
        print("Invalid input. Please try again.")
        return

    student = {
        "name": name,
        "studentid": int(studentid),
        "age": int(age),
        "birthday": birthday,
        "course": course
    }
    students.append(student)
    print(f"Student {name} added successfully!")

# View all students
def view_students():
    if not students:
        print("No student records found.")
        return
    print("--- Student Records ---")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, ID: {student['studentid']}, Age: {student['age']}, Birthday: {student['birthday']}, Course: {student['course']}")
