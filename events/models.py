from django.db import models


from projects.models import *
from campaigns.models import *
from django.contrib.auth.models import *

class Event(models.Model):
	name = models.TextField()
	creator = models.ForeignKey(User, related_name="event_organized")
	
	date_start = models.DateTimeField()
	date_end = models.DateTimeField()

	class Meta:
		ordering=["-date_start"]

	def __str__(self):
		return self.name

class CampaginEvent(models.Model):
	element = models.ForeignKey(Campaign, related_name="events")
	event = models.ForeignKey(Event, related_name="campaigns")

class MonitorableEvent(models.Model):
	element = models.ForeignKey(Monitorable, related_name="events")
	event = models.ForeignKey(Event, related_name="Projects")

class EventJoin(models.Model):
	user = models.ForeignKey(User, related_name="events")
	event = models.ForeignKey(Event, related_name="joins")


