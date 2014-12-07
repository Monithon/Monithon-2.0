
from django.contrib.gis.db import models
from monitor.models import MonitoringTeam
from projects.models import Monitorable
from customforms.models import Form as CustomForm, FormFieldOption
from customforms.models import FormField

import json

class Report(models.Model):
	author = models.ForeignKey(MonitoringTeam, related_name="reports", null=True, blank=True)
	author_text = models.CharField(max_length=1000, null=True, blank=True)
	project = models.ForeignKey(Monitorable, related_name="reports",null=True, blank=True)
	title = models.TextField(null=True, blank=True)
	datetime = models.DateTimeField(auto_now_add=True)
	finalized = models.BooleanField(default = False)
	validated = models.BooleanField(default = False)
	position = models.GeometryField(null=True, blank=True)

	class Meta:
		ordering = ["datetime"]

	def __str__(self):
		return self.title

	def geoj(self):
		return json.dumps(json.loads(self.position.json))

	def description(self):
		for form in self.forms.all():
			for field  in form.fields.all():
				if "Descr" in field.field.label:
					return field.value
		return ""

class ReportForm(models.Model):
	report = models.ForeignKey(Report, related_name="forms")
	form = models.ForeignKey(CustomForm)


class ReportFormField(models.Model):
	report_form = models.ForeignKey(ReportForm, related_name ="fields")
	field = models.ForeignKey(FormFieldOption)
	value = models.TextField()


class ReportImage(models.Model):
	report = models.ForeignKey(Report)
	image = models.ImageField(upload_to="uploads")

class ReportLink(models.Model):
	report = models.ForeignKey(Report, related_name="links")
	link = models.URLField(max_length=1000)

	def panel_body(self):
		try:
			if "youtu" in self.link:
				the_vid = self.link
				if ".be" in self.link:
					the_vid = the_vid.split("youtu.be/")[1]
				else:
					the_vid = the_vid.split("v=")[1]
				return """<div class='panel-body'><iframe class="col-lg-12" height="315" src="//www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe></div>""" % the_vid

			else:
				return ""
		except:
			return ""