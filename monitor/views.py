from django.shortcuts import render
from monitor.models import *

def list_teams(request, id=None, op=None):

	if op:
		if op == "join":
			request.user.monitor_profile.all()[0].teams.add(MonitoringTeam.objects.get(id=id))
		elif op == "leave":
			request.user.monitor_profile.all()[0].teams.remove(MonitoringTeam.objects.get(id=id))

	if id is None:
		return render(request, "teams.html", {
			"teams":MonitoringTeam.objects.all()
		})
	else:
		memberfilter = {}
		if not request.user.is_anonymous():
			memberfilter["user"] = request.user
		
		return render(request, "team.html", {
			"team":MonitoringTeam.objects.get(id=id),
			"member":MonitoringTeam.objects.get(id=id).members.filter(**memberfilter)
		})

