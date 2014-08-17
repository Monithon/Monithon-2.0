from django.contrib.gis.db import models

class Project(models.Model):
	cup = models.CharField(max_length=100, null=True, blank=True)
	oc_slug = models.CharField(max_length=100)
	description = models.TextField()
	oc_url = models.URLField(max_length=400)
	subjects = models.ManyToManyField("Subject")
	locations = models.ManyToManyField("Location")
	total_amount = models.FloatField(null=True, blank=True)
	paid_amount = models.FloatField(null=True, blank=True)
	paid_percent = models.FloatField(null=True, blank=True)
	date_from = models.DateField(null=True, blank=True)
	date_to = models.DateField(null=True, blank=True)

	@property
	def concluded(self):
	    return self.date_to is not None
	
	@property
	def oc_page(self):
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

class Tags(models.Model):
	name = models.TextField()
	description = models.TextField()
	slug = models.TextField(unique=True)
	tagtype = models.TextField()
	url = models.URLField(null=True, blank=True,max_length=400)
	def __str__(self):
		return self.name