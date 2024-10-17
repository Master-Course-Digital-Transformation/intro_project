class Resource:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.quantity}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Flipchart(Resource):
    def __init__(self, quantity):
        super().__init__("Flipchart", quantity)
    
class Projector(Resource):
    def __init__(self, quantity):
        super().__init__("Projector", quantity)

class ResourceFactory:
    def create(self, resource_type, quantity):
        if resource_type == "Flipchart":
            return Flipchart(quantity)
        elif resource_type == "Projector":
            return Projector(quantity)
        else:
            raise ValueError(f"Unknown resource type: {resource_type}")