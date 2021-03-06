from django.db import models
from django.urls import reverse

from room_schedules.artifax_requests import get_todays_events_simple


class Venue(models.Model):
    name = models.CharField(max_length=100)
    artifax_id = models.IntegerField(unique=True)

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('event_schedule/venue', args=[str(self.id)])

    def update_events(self):
        from room_schedules.models import Room
        from room_schedules.models import Event
        events = get_todays_events_simple(self.artifax_id)
        events_that_should_exist = []
        new_events = 0
        for event in events:
            room, _ = Room.objects.update_or_create(artifax_id=event['room_id'], defaults={'name': event['room_name'],
                                                                                           'venue': self})
            event, new_event = Event.objects.update_or_create(artifax_id=event['event_id'],
                                                              defaults={'name': event['activity_detail'][:200],
                                                                        'organiser': event['organiser'][:200],
                                                                        'room': room,
                                                                        'start_time': event['time'],
                                                                        'end_time': event['finish_time'],
                                                                        'cancelled': event['cancelled']
                                                                        })
            events_that_should_exist.append(event.id)
            if new_event:
                new_events += 1
        Event.objects.filter(room__venue=self).exclude(pk__in=events_that_should_exist).delete()
        print("{} created {} events and updated {}".format(self.name,
                                                           new_events,
                                                           len(events_that_should_exist) - new_events))
