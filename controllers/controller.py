from flask import render_template, request
from app import app
from models.events import events, add_new_event
from models.event import Event
import datetime


@app.route('/events')
def index():
    return render_template('index.html', title='Events Home', events=events)

@app.route('/events', methods=['POST'])
def add_event():
    eventDate = datetime.date(int(request.form['year']),int(request.form['month']),int(request.form['day']))
    eventName = request.form['event_name']
    eventGuests = request.form['guests']
    eventRoomLocation = request.form['room_location']
    eventDescription = request.form['description']
    newEvent= Event(date=eventDate, event_name=eventName, guests=eventGuests,room_location=eventRoomLocation, description=eventDescription)
    add_new_event(newEvent)

    return render_template('index.html', title='Events Home', events=events)

