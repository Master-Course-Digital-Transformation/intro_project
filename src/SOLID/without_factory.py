class UndergraduateStudent:
    def __init__(self, name, student_id, courses):
        self.name = name
        self.student_id = student_id
        self.courses = courses

class GraduateStudent:
    def __init__(self, name, student_id, thesis_topic):
        self.name = name
        self.student_id = student_id
        self.thesis_topic = thesis_topic

# Usage
student1 = UndergraduateStudent("Alice", 123, ["Math", "History"])
student2 = GraduateStudent("Bob", 456, "Artificial Intelligence")
