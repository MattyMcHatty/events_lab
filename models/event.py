import datetime

class Event():

    def __init__(self, date, event_name, guests, room_location, description):
        self.date = date
        self.event_name = event_name
        self.guest = guests
        self.room_location = room_location
        self.description = description

    