import json
from student import Student


class StudentManager:

    def __init__(self):
        self.students = []

    def load_studentss(self):
        try:
            with open("student.json", "r") as file:
                data = json.load(file)
                self.students = [
                    Student.from_dict(student) for student in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = []

    def save_students(self):
        with open("student.json", "w") as file:
            json.dump(
                [student.to_dict() for student in self.students],
                file,
                indent=4
            )

    def add_student(self, student):
        self.students.append(student)
        self.save_students()

    def get_student_parameters(self):
        print("Add Student \n")
        name = input("What's Student's full name: ").strip().title()
        age = input("What's student's age: ")
        age = self.get_valid_int(age)
        student_id = input("What's Student's ID: ")
        student_id = self.get_valid_student_id(student_id)
        student = Student(name, age, student_id)
        self.add_student(student)

    def remove_student(self, student_temp_id):
        for student in self.students:
            if student_temp_id == student.student_id:
                print("removing the student's information")
                student.display_student()
                confirmation = (
                    input(
                        "do you confirm?  (Y for Yes N for No) "
                    ).strip().upper()
                )
                if confirmation.upper() == "Y":
                    print("Student no longer on the list")
                    self.students.remove(student)
                    self.save_students()
                    return True
        return False

    def search_student_by_id(self, student_temp_id):
        for student in self.students:
            if student_temp_id == student.student_id:
                print("Here is the student's information")
                return student
        return None

    def search_student_by_name(self, student_temp_name):
        student_temp_name = student_temp_name.strip().title()
        for student in self.students:
            if student_temp_name == student.name:
                print("Here is the student's information")
                return student
        return None

    def update_student(self, student_temp_id):
        student_temp_id = self.get_valid_int(student_temp_id)
        for student in self.students:
            if student_temp_id == student.student_id:
                print("Here is the student's information")
                print("Name:", student.name)
                updated_student_name = (
                    input("New name (leave blank to keep) ").strip().title()
                )
                if not updated_student_name:
                    updated_student_name = student.name
                print("Age:", student.age)
                updated_student_age = input("New age(leave blank to keep) ")
                if updated_student_age:
                    updated_student_age = (
                        self.get_valid_int(updated_student_age)
                    )
                else:
                    updated_student_age = student.age
                print("Student ID:", student.student_id)
                updated_student_id = input("New ID(leave blank to keep) ")
                if updated_student_id:
                    updated_student_id = (
                        self.get_valid_student_id(updated_student_id)
                    )
                else:
                    updated_student_id = student.student_id
                student.name = updated_student_name
                student.age = updated_student_age
                student.student_id = updated_student_id

                self.save_students()
                return True
        return False

    def get_valid_int(self, input_data):
        while True:
            try:
                output = int(input_data)
                return output
            except ValueError:
                print("That wasn't a number. ")
                input_data = input("please enter a valid number")

    def get_valid_student_id(self, input_data):
        student_temp_id = self.get_valid_int(input_data)
        for student in self.students:
            if student_temp_id == student.student_id:
                print("ID is already taken please choose another ID")
                student_temp_id = input("What's Student's ID: ")
                student_temp_id = self.get_valid_student_id(student_temp_id)
                break
        return student_temp_id

    def sort_students_by_name(self, reverse):
        self.students.sort(key=lambda student: student.name, reverse=reverse)
        self.save_students()

    def sort_students_by_age(self, reverse):
        self.students.sort(key=lambda student: student.age, reverse=reverse)
        self.save_students()

    def sort_students_by_id(self, rev):
        self.students.sort(key=lambda student: student.student_id, reverse=rev)
        self.save_students()

    def select_sort_type(self):
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

    def oldest_student(self):
        return max(self.students, key=lambda student: student.age)

    def total_student_number(self):
        return len(self.students)

    def youngest_student(self):
        return min(self.students, key=lambda student: student.age)

    def average_student_age(self):
        sum_of_age = 0
        total_number_of_students = self.total_student_number()
        for student in self.students:
            sum_of_age += student.age
        return round(sum_of_age/total_number_of_students)

    def remove_all_students(self):
        print("ATTENTION : You are going to delete all students ......")
        print("ARE YOU SURE?")
        first_confirmation = input("Y for yes N for NO? ")
        if first_confirmation == "Y":
            print("After deleting there data will be gone forever")
            print("ARE YOU SURE?")
            second_confirmation = input("type CONFIRM to delete ")
            if second_confirmation == "CONFIRM":
                print("Deleting the student's information list ")
                self.students.clear()
                self.save_students()
                print("100% DONE!")
                print("------------------------------")
            else:
                return
        else:
            return

    def show_all_students(self):
        print("Here is a list of all students")
        print("------------------------------")
        if not self.students:
            print("List is empty")
        for student in self.students:
            Student.display_student(student)
            print("-----------------------------")
