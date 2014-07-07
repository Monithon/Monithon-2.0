from django.db import models

from django.contib.auth.models import User

class MonitoringTeam(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField()
	location = models.PolygonField()

class Monitorer(models.Model):
	user = models.ForeignKey(User)
	teams = models.ManyToMany(MonitoringTeam)
	location = models.PointField()