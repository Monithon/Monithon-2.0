from django.shortcuts import render

from events.model import *

def event(request, event_id=None):
	if event_id:
		return render(request,"event.html", {"event":Event.objects.get(id=event_id)})
	else:
		return render(request,"event.html", {"events":Event.objects.all()})
