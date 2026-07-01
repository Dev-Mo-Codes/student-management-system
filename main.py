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
    age = input("What's student's age: ")
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


def remove_all_students():
    print("ATTENTION : You are going to delete all students ......")
    print("ARE YOU SURE?")
    first_confirmation = input("Y for yes N for NO? ")
    if first_confirmation == "Y":
        print("After deleting there data will be gone forever")
        print("ARE YOU SURE?")
        second_confirmation = input("type CONFIRM to delete ")
        if second_confirmation == "CONFIRM":
            print("Deleting the student's information list ")
            students.clear()
            save_students()
            print("100% DONE!")
            print("------------------------------")
        else:
            return
    else:
        return


def oldest_student():
    return max(students, key=lambda student: student["age"])


def total_student_number():
    return len(students)


def youngest_student():
    return min(students, key=lambda student: student["age"])


def average_student_age():
    sum_of_age = 0
    total_number_of_students = total_student_number()
    for student in students:
        sum_of_age += student["age"]
    return round(sum_of_age/total_number_of_students)


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


def sort_students_by_name(is_reverse):
    students.sort(key=lambda student: student["name"], reverse=is_reverse)
    save_students()


def sort_students_by_age(is_reverse):
    students.sort(key=lambda student: student["age"], reverse=is_reverse)
    save_students()


def sort_students_by_id(reverse):
    students.sort(key=lambda student: student["student_id"], reverse=reverse)
    save_students()


def select_sort_type():
    print("\n===== Sort List in =====")
    print("1. Ascending")
    print("2. Descending")
    print("------------------------------")
    choice = input("Select an option: ")
    if choice == "1":
        return False
    elif choice == "2":
        return True
    else:
        print("Invalid choice .... ")
        print("Ascending has been chosen by default ")
        return False


students = load_students()

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Show All Students")
    print("6. Sort Students List")
    print("7. Statistics")
    print("8. Delete All Data")
    print("9. Exit")
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
        student_temp_id = input("Please enter Student ID to update: ")
        if update_student(student_temp_id):
            print("Student has been updated")
            print("------------------------------")
        else:
            print("Student doesn't exist")
            print("------------------------------")
    elif choice == "5":
        show_all_students()
    elif choice == "6":
        print("\n===== Sort Student List =====")
        print("1. Sort By Name")
        print("2. Sort By Age")
        print("3. Sort By ID")
        print("------------------------------")
        choice = input("Select an option: ")
        if choice == "1":
            sort_descending = select_sort_type()
            sort_students_by_name(sort_descending)
        elif choice == "2":
            sort_descending = select_sort_type()
            sort_students_by_age(sort_descending)
        elif choice == "3":
            sort_descending = select_sort_type()
            sort_students_by_id(sort_descending)
        else:
            print("Invalid choice")
    elif choice == "7":
        print("\n=====Statistics =====")
        print("1. Total number of students: ")
        print(total_student_number())
        print("\n------------------------------")
        if not students:
            print("List is empty")
            print("\n------------------------------")
        else:
            print("2. Youngest student info: ")
            display_student(youngest_student())
            print("\n------------------------------")
            print("3. Oldest student info: ")
            display_student(oldest_student())
            print("\n------------------------------")
            print("4. Average of students age: ")
            print(average_student_age())
            print("\n------------------------------")
    elif choice == "8":
        remove_all_students()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
