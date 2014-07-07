from django.db import models

from django.contib.auth.models import User


class Badge(models.Model):
	name = models.CharField(max_length=100)

class BadgeRule(models.Model):
	name = models.CharField(max_length=100)
	rule = models.TextField()
	badge = models.ForeignKey(Badge, related_name="rules")

class BadgeAward(models.Model):
	user = models.ForeignKey(User, related_name="badges")
	badge = models.ForeignKey(Badge, related_name="users")
	date = models.DateTimeField(auto_now=True)