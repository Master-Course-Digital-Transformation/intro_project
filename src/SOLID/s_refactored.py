class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

class GradeService:
    def get_grades(self, student):
        # Fetch grades for the student from the database
        pass

class FileService:
    def save_to_file(self, student):
        # Save student data to a file
        pass
