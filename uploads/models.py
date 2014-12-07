from django.db import models

from django.conf import settings
from projects.models import *
from django.contrib.auth.models import User

class UploadType(models.Model):
	name = models.TextField()

	def __str__(self):
		return self.name

class Upload(models.Model):
	project = models.ForeignKey(Monitorable, null=True, blank=True, related_name="uploads")
	author = models.ForeignKey(User)
	creation = models.DateTimeField(auto_now=True)
	relative_to = models.DateField()
	filename = models.TextField()
	upload_type = models.TextField()
	data = models.FileField(upload_to=settings.UPLOAD_FILES)

	def __str__(self):
		return self.filename

class UploadPosition(models.Model):
	upload = models.ForeignKey(Upload, related_name="positions")
	lon = models.FloatField()
	lat = models.FloatField()

