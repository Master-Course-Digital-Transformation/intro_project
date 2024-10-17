class Student:
    def get_grades(self):
        return "Grades"

class SpecialStudent(Student):
    def get_grades(self):
        raise Exception("Not allowed")

# Liskov Substitution Principle violated: SpecialStudent is not a valid substitute for Student