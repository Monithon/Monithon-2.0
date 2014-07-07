from django.db import models

from django.contrib.auth.models import User
from projects.models import Project
from customforms.models import Form as CustomForm
from customforms.models import FormField

class Report(models.Model):
	author = models.ForeignKey(User)
	project = models.ForeignKey(Project)
	datetime = models.DateTimeField(auto_now=True)
	#finalized = models.BooleanField(default = False, editable=False)

class ReportForm(models.Model):
	report = models.ForeignKey(Report, related_name="forms")
	form = models.ForeignKey(CustomForm)


class ReportFormField(models.Model):
	report_form = models.ForeignKey(ReportForm, related_name ="fields")
	field = models.ForeignKey(FormField)
	value = models.TextField()