from django.shortcuts import render

from projects.models import Project

def get_project(request,cup):
	pass


def list_projects(request):
	count = Project.objects.all().count()
	page = int(request.REQUEST.get("p", "1"))-1
	prjs = Project.objects.all()[(page)*10:(page+1)*10]
	return render(request, "projects.html", {"projects":prjs, "page":page+1, "count":count})