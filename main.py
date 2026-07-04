from student_manager import StudentManager

manager = StudentManager()
manager.load_students()

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
        manager.get_student_parameters()
    elif choice == "2":
        print("Remove Student")
        print("------------------------------")
        if manager.total_student_number() == 0:
            print("List is empty")
            print("------------------------------")
        student_temp_id = input("Please enter Student ID ")
        student_temp_id = manager.get_valid_int(student_temp_id)
        removed = manager.remove_student(student_temp_id)
        if not removed:
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
            student = (
                manager.search_student_by_name(student_temp_name)
            )
            if not student:
                print("Student Not Found")
                print("------------------------------")
            else:
                student.display_student()
                print("------------------------------")
        elif choice == "2":
            student_temp_id = input("Please enter Student ID: ")
            student_temp_id = manager.get_valid_int(student_temp_id)
            print("Searching for student By ID ..... ")
            student = (
                manager.search_student_by_id(student_temp_id)
            )
            if not student:
                print("Student Not Found")
                print("------------------------------")
            else:
                student.display_student()
                print("------------------------------")
    elif choice == "4":
        student_temp_id = input("Please enter Student ID to update: ")
        if manager.update_student(student_temp_id):
            print("Student has been updated")
            print("------------------------------")
        else:
            print("Student doesn't exist")
            print("------------------------------")
    elif choice == "5":
        manager.show_all_students()
    elif choice == "6":
        print("\n===== Sort Student List =====")
        print("1. Sort By Name")
        print("2. Sort By Age")
        print("3. Sort By ID")
        print("------------------------------")
        choice = input("Select an option: ")
        if choice == "1":
            sort_descending = manager.select_sort_type()
            manager.sort_students_by_name(sort_descending)
            manager.show_all_students()
        elif choice == "2":
            sort_descending = manager.select_sort_type()
            manager.sort_students_by_age(sort_descending)
            manager.show_all_students()
        elif choice == "3":
            sort_descending = manager.select_sort_type()
            manager.sort_students_by_id(sort_descending)
            manager.show_all_students()
        else:
            print("Invalid choice")
    elif choice == "7":
        print("\n=====Statistics =====")
        print("1. Total number of students: ")
        print(manager.total_student_number())
        print("\n------------------------------")
        if not manager.students:
            print("List is empty")
            print("\n------------------------------")
        else:
            print("2. Youngest student info: ")
            manager.youngest_student().display_student()
            print("\n------------------------------")
            print("3. Oldest student info: ")
            manager.oldest_student().display_student()
            print("\n------------------------------")
            print("4. Average of students age: ")
            print(manager.average_student_age())
            print("\n------------------------------")
    elif choice == "8":
        manager.remove_all_students()
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
