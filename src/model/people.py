
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
class Student(Person):
    def __init__(self, name, id = None):
        super().__init__(name)
        self.id = id

    def __str__(self):
        return f"{self.name} {'with immatriculation number' + self.id if self.id else ''} is a Student"

class Teacher(Person):
    def __str__(self):
        return f"{self.name} is a Teacher"

class Admin(Person):
    def __str__(self):
        return f"{self.name} is an Admin"

# Step 3: Create a Factory to generate different user types
class PersonFactory:
    @staticmethod
    def create_person(user_type, name):
        if user_type == "student":
            return Student(name)
        elif user_type == "teacher":
            return Teacher(name)
        elif user_type == "admin":
            return Admin(name)
        else:
            raise ValueError("Invalid user type")

# Step 4: Demonstration of the Factory
if __name__ == "__main__":
    # Create different types of users using the factory
    people = [
        PersonFactory.create_person("student", "Alice"),
        PersonFactory.create_person("teacher", "Mr. Smith"),
        PersonFactory.create_person("admin", "Principal Johnson")
    ]

    # Output the roles of the users
    for person in people:
        print(person)
