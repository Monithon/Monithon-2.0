from django.shortcuts import render
from django.utils.html import conditional_escape
from projects.models import Monitorable

from django.http import HttpResponse

import json
import urllib

def get_project(request,cup):

	value = request.build_absolute_uri()

	qr = conditional_escape("http://chart.apis.google.com/chart?%s" % \
            urllib.urlencode({'chs':'150x150', 'cht':'qr', 'chl':value, 'choe':'UTF-8'}))

	return render(request, "project.html", {"project":Monitorable.objects.get(id=cup), "qr":qr})


def list_projects(request):

	category = request.REQUEST.get("category")

	f = {}
	if category is not None:
		f["category__id"] = int(category)

	count = Monitorable.objects.filter(**f).count()
	page = int(request.REQUEST.get("p", "1"))-1
	prjs = Monitorable.objects.filter(**f)[(page)*10:(page+1)*10]
	return render(request, "projects.html", {"projects":prjs, "page":page+1, "count":count, "prev":page, "next":page+2, "category":category})

def search(request):
	return HttpResponse(json.dumps([{"name":x.description, "id":x.id} for x in Monitorable.objects.filter(description__icontains=request.REQUEST.get("q"))[:10]]))