class Student:
    def __init__(self, name: str, course: str):
        self.name = name
        self.course = course

    def get_details(self) -> str:
        return f"Student: {self.name} | Course: {self.course}"


student = Student("Mansi Pareek", "B.Tech CSE")

print(student.get_details())