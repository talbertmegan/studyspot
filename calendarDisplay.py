from index import events
from data import Course

def filterEvents(course_names, events):
    user_events = []
    for course in course_names:
        for event in events:
            if course in event.summary:
                userEvents.append(event)
    return user_events
