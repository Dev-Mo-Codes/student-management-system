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
    students.append(student)


def get_student_parameters():
    print("Add Student \n")
    name = input("What's Student's full name: ")
    name = name.strip().title()
    age = input("What's studen's age: ")
    age = get_valid_int(age)
    student_id = input("What's Student's ID: ")
    student_id = get_valid_student_id(student_id)
    student = {
        "name": name,
        "age": age,
        "student_id": student_id
    }
    add_student(student)


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


def search_student_by_id(student_temp_id):
    for student in students:
        if student_temp_id == student["student_id"]:
            print("Here is the student's information")
            display_student(student)
            return True
    return False


def search_student_by_name(student_temp_name):
    student_temp_name = student_temp_name.strip().title()
    for student in students:
        if student_temp_name == student["name"]:
            print("Here is the student's information")
            display_student(student)
            return True
    return False


def update_student(student_temp_id):
    student_temp_id = get_valid_int(student_temp_id)
    for student in students:
        if student_temp_id == student["student_id"]:
            print("Here is the student's information")
            print("Name:", student["name"])
            updated_student_name = input("New name (leave blank to keep) ")
            updated_student_name = updated_student_name.strip().title()
            if not updated_student_name:
                updated_student_name = student["name"]
            print("Age:", student["age"])
            updated_student_age = input("New age(leave blank to keep) ")
            if updated_student_age:
                updated_student_age = get_valid_int(updated_student_age)
            else:
                updated_student_age = student["age"]
            print("Student ID:", student["student_id"])
            updated_student_id = input("New ID(leave blank to keep) ")
            if updated_student_id:
                updated_student_id = get_valid_student_id(updated_student_id)
            else:
                updated_student_id = student["student_id"]
            student["name"] = updated_student_name
            student["age"] = updated_student_age
            student["student_id"] = updated_student_id

            save_students()
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
            output = int(input_data)
            return output
        except ValueError:
            print("That wasn't a number. ")
            input_data = input("please enter a valid number")


def get_valid_student_id(input_data):
    student_temp_id = get_valid_int(input_data)
    for student in students:
        if student_temp_id == student["student_id"]:
            print("ID is already taken please choose another ID")
            student_temp_id = input("What's Student's ID: ")
            student_temp_id = get_valid_student_id(student_temp_id)
            break
    return student_temp_id


students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Show All Students")
    print("5. Update Student")
    print("6. Exit")
    print("------------------------------")

    choice = input("Select an option: ")

    if choice == "1":
        get_student_parameters()
        save_students()
    elif choice == "2":
        print("Remove Student")
        print("------------------------------")
        if not students:
            print("List is empty")
            print("------------------------------")
        student_temp_id = input("Please enter Student ID ")
        student_temp_id = get_valid_int(student_temp_id)
        check_status = remove_student(student_temp_id)
        save_students()
        if not check_status:
            print("Student not Found")
            print("------------------------------")
        else:
            print("Student Removed")
            print("------------------------------")
    elif choice == "3":
        print("\n===== Search Student =====")
        print("1. Search Student By Name")
        print("2. Search Student By ID")
        print("------------------------------")
        choice = input("Select an option: ")

        if choice == "1":
            student_temp_name = input("Please enter Student name: ")
            student_temp_name = student_temp_name.strip().title()
            print("Searching for student By name ..... ")
            check_status = search_student_by_name(student_temp_name)
            if not check_status:
                print("Student Not Found")
                print("------------------------------")
            else:
                print("------------------------------")
        elif choice == "2":
            student_temp_id = input("Please enter Student ID: ")
            student_temp_id = get_valid_int(student_temp_id)
            print("Searching for student By ID ..... ")
            check_status = search_student_by_id(student_temp_id)
            if not check_status:
                print("Student Not Found")
                print("------------------------------")
            else:
                print("------------------------------")
    elif choice == "4":
        show_all_students()
    elif choice == "5":
        student_temp_id = input("Please enter Student ID to update: ")
        if update_student(student_temp_id):
            print("Student has been updated")
            print("------------------------------")
        else:
            print("Student doesn't exist")
            print("------------------------------")
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
