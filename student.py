class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "student_id": self.student_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["age"],
            data["student_id"]
        )

    def display_student(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.student_id)
