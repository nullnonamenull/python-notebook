class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        avg_grade = sum(self.marks) / len(self.marks)
        return avg_grade > 50
