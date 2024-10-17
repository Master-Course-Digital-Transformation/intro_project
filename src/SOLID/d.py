class Database:
    def save(self, student):
        pass

class StudentService:
    def save_student(self, student):
        db = Database()  # High-level module depends on a low-level module
        db.save(student)

# Dependency Inversion Principle Violated: High-level modules should not depend on low-level modules. Both should depend on abstractions.