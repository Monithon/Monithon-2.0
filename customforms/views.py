from django.shortcuts import render

from django.http import HttpResponse
from customforms.models import *

import json


def get_form_structure(name):
	form = {}
	data = Form.objects.get(name=name)

	form['name'] = data.name
	form['id'] = data.id
	form['fields'] = []

	for field in data.fields.all():
		if field.options is not None:
			form['fields'].append({'field':field.form_field.name, 'label':field.label, 'hint':field.hint, 'options':field.options.split("\n"), "list":field.list_field, "oblig":field.obligatory, "id":field.id})
		else:
			form['fields'].append({'field':field.form_field.name, 'label':field.label, 'hint':field.hint, 'options':[""], "list":field.list_field, "oblig":field.obligatory, "id":field.id})
	return form

def get_form(request, name):
	return HttpResponse(json.dumps(get_form_structure(name)))


def show_form(request, name):
	form = get_form_structure(name)
	for field in form['fields']:
		field["url"] = "fields/" + field['field'] + ".html"
	return render(request, "form.html", form)


def list_forms(request):
	ret = []
	for form in Form.objects.all():
		ret.append(form.name)
	return HttpResponse(json.dumps(ret))
