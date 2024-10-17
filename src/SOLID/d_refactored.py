class DatabaseInterface:
    def save(self, student):
        pass

class Database(DatabaseInterface):
    def save(self, student):
        pass

class StudentService:
    def __init__(self, db: DatabaseInterface):
        self.db = db

    def save_student(self, student):
        self.db.save(student)
