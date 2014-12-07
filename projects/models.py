import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from django.contrib.gis.db import models

class MonitorableCategory(models.Model):
	name = models.TextField()
	icon = models.TextField()

	def __str__(self):
		return self.name

class Monitorable(models.Model):
	#title = models.TextField(blank=True, null=True)
	description = models.TextField()
	subjects = models.ManyToManyField("Subject", blank=True, null=True)
	locations = models.ManyToManyField("Location", blank=True, null=True)
	tags = models.ManyToManyField("Tag", blank=True, null=True)
	category = models.ForeignKey(MonitorableCategory, blank=True, null=True)
	cup = models.CharField(max_length=100, null=True, blank=True)
	oc_slug = models.CharField(max_length=100, null=True, blank=True)
	oc_url = models.URLField(max_length=400,null=True, blank=True)
	total_amount = models.FloatField(null=True, blank=True)
	paid_amount = models.FloatField(null=True, blank=True)
	paid_percent = models.FloatField(null=True, blank=True)
	date_from = models.DateField(null=True, blank=True)
	date_to = models.DateField(null=True, blank=True)
	#original_data = models.TextField(blank=True, null=True)

	@property
	def concluded(self):
	    return self.date_to is not None
	
	@property
	def oc_page(self):
		if self.oc_url:
			return "http://www.opencoesione.gov.it/progetti/%s/" % self.oc_url.split("/")[-1].split(".")[0]

	def __str__(self):
		return self.description


class Location(models.Model):
	name = models.CharField(max_length=100)
	slug = models.CharField(max_length=100, unique=True)
	nat = models.ForeignKey('Geo', null=True, blank=True, related_name ="nat")
	reg = models.ForeignKey('Geo', null=True, blank=True, related_name ="reg")
	pro = models.ForeignKey('Geo', null=True, blank=True, related_name ="pro")
	mun = models.ForeignKey('Geo', null=True, blank=True, related_name ="mun")

	def __str__(self):
		return self.name

class Geo(models.Model):
	name = models.TextField()
	code = models.IntegerField()
	level = models.CharField(max_length=5)
	geometry = models.GeometryField()
	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.TextField()
	slug = models.TextField()
	url = models.URLField(max_length=400)
	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.TextField()
	description = models.TextField()
	slug = models.TextField(unique=True)
	tagtype = models.TextField()
	url = models.URLField(null=True, blank=True,max_length=400)
	def __str__(self):
		return self.name

class Layer(models.Model):
	name = models.CharField(max_length=500)
	icon = models.URLField()
	projects = models.ManyToManyField(Monitorable, related_name="layers")

	def __str__(self):
		return self.name