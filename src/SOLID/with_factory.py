class StudentFactory:
    @staticmethod
    def create_student(student_type, name, student_id, extra_info):
        if student_type == "undergraduate":
            return UndergraduateStudent(name, student_id, extra_info)
        elif student_type == "graduate":
            return GraduateStudent(name, student_id, extra_info)
        else:
            raise ValueError("Invalid student type")

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

# Usage with factory
factory = StudentFactory()
student1 = factory.create_student("undergraduate", "Alice", 123, ["Math", "History"])
student2 = factory.create_student("graduate", "Bob", 456, "Artificial Intelligence")

# Motivation for Factories:
# Simplifying Object Creation: When creating objects requires multiple steps, or when objects have dependencies, directly instantiating them in the code can make it harder to manage changes. A factory centralizes this logic and makes the creation process more manageable.

# Decoupling Object Instantiation: Using a factory allows you to decouple the creation of objects from their use, which enhances the flexibility of your system. This aligns with the Dependency Inversion Principle (DIP), where high-level components depend on abstractions, not on specific concrete implementations.

# Handling Multiple Object Types: Factories are excellent when your system deals with multiple types of related objects. For instance, if your student management system needs to create different types of students (e.g., undergraduate, graduate), a factory can handle this logic.

# Easier Testing: By using factories, you can easily mock the object creation in unit tests. You won't need to know the exact creation logic inside your tests, allowing for better isolation and easier testing.