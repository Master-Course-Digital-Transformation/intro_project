import model.people
import control.BookingService
import pysqlite3

class BackendService:
    def __init__(self):
        self.booking_service = control.BookingService.BookingService()
        self.connection = pysqlite3.connect("data.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, type TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS rooms (id INTEGER, name TEXT, capacity INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS resources (name TEXT, quantity INTEGER)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS bookings (person TEXT, room INTEGER, start_time TEXT, end_time TEXT)")
        self.connection.commit()

    def add_person(self, person):
        self.booking_service.add_person(person)
        self.cursor.execute("INSERT INTO people (name, type) VALUES (?, ?)", (person.name, type(person).__name__))
        self.connection.commit()

    def add_room(self, room):
        self.booking_service.add_room(room)
        self.cursor.execute("INSERT INTO rooms (id, name, capacity) VALUES (?, ?, ?)", (room.id, room.name, room.capacity))
        self.connection.commit()

    def add_resource(self, resource):
        self.booking_service.add_resource(resource)
        self.cursor.execute("INSERT INTO resources (name, quantity) VALUES (?, ?)", (resource.name, resource.quantity))
        self.connection.commit()

    def book(self, person, room, start_time, end_time):
        self.booking_service.book(person, room, start_time, end_time)
        self.cursor.execute("INSERT INTO bookings (person, room, start_time, end_time) VALUES (?, ?, ?, ?)", (person.name, room.id, start_time, end_time))
        self.connection.commit()

    def get_bookings(self):
        return self.booking_service.get_bookings()

    def get_people(self):
        return self.booking_service.get_people()

    def get_rooms(self):
        return self.booking_service.get_rooms()

    def get_resources(self):
        return self.booking_service.get_resources()

    def close(self):
        self.connection.close()