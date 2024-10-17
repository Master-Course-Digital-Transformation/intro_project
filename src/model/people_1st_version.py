
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


if __name__ == "__main__":
    # Create different types of users using the factory
    people = [
        Student("Alice"),
        Teacher("Mr. Smith"),
        Admin("Principal Johnson")
    ]

    # Output the roles of the users
    for person in people:
        print(person)
