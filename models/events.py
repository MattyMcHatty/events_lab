from models.event import *

event_1 = Event(datetime.date(2022,10,24), 'Anime Conference', 20, 'North Hall', 'A big convention full of weebs')
event_2 = Event(datetime.date(2022,11,3), 'Football Fun Day', 50, 'South Field', 'A fun day out playing football')
event_3 = Event(datetime.date(2023,1,17), 'New Year, New You', 10, 'West Quadrangle', 'A Self help seminar')

events = [event_1, event_2, event_3]

def add_new_event(event):
    events.append(event)