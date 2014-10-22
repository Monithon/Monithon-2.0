#from django.db import models as basemodels
from django.contrib.gis.db import models

from django.contrib.auth.models import User

class MonitoringTeam(models.Model):
	name = models.CharField(max_length=150)
	description = models.TextField(null=True, blank=True)
	location = models.PolygonField(null=True, blank=True)

	def __str__(self):
		return self.name

class Monitor(models.Model):
	user = models.ForeignKey(User, related_name="monitor_profile", unique=True)
	teams = models.ManyToManyField(MonitoringTeam,null=True, blank=True, related_name="members")
	location = models.PointField(null=True, blank=True)

	def __str__(self):
		return self.user.username


from django.db.models.signals import post_save

def create_monitor(sender, instance, created, **kwargs):
	if created:
		Monitor.objects.create(user=instance)

post_save.connect(create_monitor, sender=User, dispatch_uid="create_user_profile")
