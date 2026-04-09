def search_student():
    search_name = input("Enter student name to search: ").strip()
    found = False
    for student in students:
        if student["name"].lower() == search_name.lower():
            print(f"Found: Name: {student['name']}, ID: {student['studentid']}, Age: {student['age']}, Birthday: {student['birthday']}, Course: {student['course']}")
            found = True
            break
    if not found:
        print("Student not found.")


def delete_student():
    delete_name = input("Enter student name to delete: ").strip()
    for student in students:
        if student["name"].lower() == delete_name.lower():
            students.remove(student)
            print(f"Student {delete_name} deleted successfully!")
            return
    print("Student not found.")

