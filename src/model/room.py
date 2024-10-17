class Room:
    def __init__(self, room_id, name, capacity):
        self.room_id = room_id
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f"{self.room_id} {self.name} {self.capacity}"

