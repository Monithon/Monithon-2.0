from django.db import models

from reports.models import * 
from projects.models import *
from customforms.models import *
from django.contrib.auth.models import *

# Create your models here.
class Campaign(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	mission = models.TextField()

	icon = models.ImageField(null=True, blank=True)

	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def to_json(self, list=False):
		r = {}
		r["name"] = self.name
		r["description"] = self.description
		r["id"] = self.id
		r["mission"] = self.mission
		r["active"] = self.active

		r["projects"] = ["/api/projects/%s" % p.project.id for p in self.projects.all()] if not list else self.projects.count()
		r["reports"] = ["/api/reports/%s" %p.report.id for p in self.reports.all()] if not list else self.reports.count()
		return r


class CampaignProject(models.Model):
	campaign = models.ForeignKey(Campaign, related_name="projects")
	project = models.ForeignKey(Monitorable, related_name="campaigns")

class CampaignReport(models.Model):
	campaign = models.ForeignKey(Campaign, related_name="reports")
	report = models.ForeignKey(Report, related_name="campaigns")

class CampaignForm(models.Model):
	campaign = models.ForeignKey(Campaign)
	form = models.ForeignKey(Form, related_name="campaigns")	

class CampaignUser(models.Model):
	campaign = models.ForeignKey(Campaign, related_name="users")
	user = models.ForeignKey(User)
