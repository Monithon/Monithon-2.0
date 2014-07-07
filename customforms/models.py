from django.db import models

class Form(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class FormField(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class FormFieldOption(models.Model):
	form = models.ForeignKey(Form, related_name="fields")
	
	label = models.CharField(max_length=100)
	hint = models.TextField()
	form_field = models.ForeignKey(FormField)
	list_field = models.BooleanField(default = False)
	obligatory = models.BooleanField(default = True)

	options = models.TextField(blank=True, null=True)


	def __str__(self):
		return self.form.name + " -> " + self.label
	
