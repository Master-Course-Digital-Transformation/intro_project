class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_grades(self):
        # Fetch grades from the database
        pass

    def save_to_file(self):
        # Save student data to a file
        pass

# single responsibility principle violated: A class should have only one reason to change. If a class has more than one responsibility, changes to one responsibility could cause issues with another.
