import json


def load_students():
    try:
        with open("student.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students():
    with open("student.json", "w") as file:
        json.dump(students, file, indent=4)


def add_student(student):
    student.append(student)


def display_student(student):
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("ID:", student["student_id"])


def remove_student(student_temp_id):
    for student in students:
        if student_temp_id == student["student_id"]:
            print("removing the student's information")
            display_student(student)
            confirmation = input("do you confirm?  (Y for Yes N for No) ")
            if confirmation.upper() == "Y":
                print("Student no longer on the list")
                students.remove(student)
            return True
    return False


def search_student(student_temp_id):
    for student in students:
        if student_temp_id == student["student_id"]:
            print("Here is the student's information")
            display_student(student)
            return True
    return False


def show_all_students():
    print("Here is a list of all students")
    print("------------------------------")
    if not students:
        print("List is empty")
    for student in students:
        display_student(student)
        print("-----------------------------")


def get_valid_int(input_data):
    while True:
        try:
            output = int(input(input_data))
            return output
        except ValueError:
            print("That wasn't a number. ")


students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Show All Students")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("Add Student \n")
        name = input("What's Student's full name: ")
        name = name.strip().title()
        age = get_valid_int("What's studen's age: ")
        student_id = get_valid_int("What's Student's number: ")
        student = {
            "name": name,
            "age": age,
            "student_id": student_id
        }
        add_student(student)
        save_students()
    elif choice == "2":
        print("Remove Student")
        if not students:
            print("List is empty")
        student_temp_id = int(input("Please enter Student ID "))
        check_status = remove_student(student_temp_id)
        save_students()
        if not check_status:
            print("Student not Found")
    elif choice == "3":
        print("Search student")
        student_temp_id = int(input("Please enter Student ID "))
        print("Searching for student ..... ")
        check_status = search_student(student_temp_id)
        if not check_status:
            print("Student Not Found")
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
