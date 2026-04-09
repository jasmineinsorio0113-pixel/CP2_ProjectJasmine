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


   


def main():
    while True:
        display_menu()
        choice = input("Choose your option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program... Thanks for using the System!")
            break
        else:
            print("Invalid choice!")


if _name_ == "_main_":
    main()
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


def main():
    while True:
        display_menu()
        choice = input("Choose your option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program... Thanks for using the System!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
