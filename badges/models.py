from django.db import models

from django.contib.auth.models import User


class Badge(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class BadgeRule(models.Model):
	name = models.CharField(max_length=100)
	rule = models.TextField()
	badge = models.ForeignKey(Badge, related_name="rules")

	def __str__(self):
		return self.name

class BadgeAward(models.Model):
	team = models.ForeignKey(MonitoringTeam, related_name="badges")
	badge = models.ForeignKey(Badge, related_name="users")
	date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s - %s" % (self.team, self.badge, )