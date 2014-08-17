from django.shortcuts import render
from django.utils.html import conditional_escape
from projects.models import Project

import urllib

def get_project(request,cup):

	value = request.build_absolute_uri()

	qr = conditional_escape("http://chart.apis.google.com/chart?%s" % \
            urllib.urlencode({'chs':'150x150', 'cht':'qr', 'chl':value, 'choe':'UTF-8'}))

	return render(request, "project.html", {"project":Project.objects.get(id=cup), "qr":qr})


def list_projects(request):
	count = Project.objects.all().count()
	page = int(request.REQUEST.get("p", "1"))-1
	prjs = Project.objects.all()[(page)*10:(page+1)*10]
	return render(request, "projects.html", {"projects":prjs, "page":page+1, "count":count, "prev":page, "next":page+2})