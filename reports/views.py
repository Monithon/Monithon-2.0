from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from reports.models import Report
from projects.models import Project
from django.views.decorators.csrf import csrf_exempt

import json


@login_required
def new_report(request):
	return render(request, "new_report.html", {"forms":["test"]})

@csrf_exempt 
@login_required
def push_report(request):
	data = request.REQUEST.get("data", "{}")
	data = json.loads(data)

	r = Report()
	r.author = request.user
	r.project = Project.objects.get(id=data["project"])
	r.save()

	for area in data["report"]:
		rf = ReportForm()
		rf.form = CustomForm.objects.get(id=area["origins"])
		rf.report = r
		rf.save()

		for field in area["data"]:
			rff =ReportFormField()
			rff.report_form = rf
			rff.field = FormField.objects.get(id=field["name"])
			rff.value = value

			rff.save()

	return HttpReponse("OK")

def list_reports(request):

	page = int(request.REQUEST.get('page', "1"))-1

	count = Report.objects.count()
	pages = int(count / 10)

	reports = Report.objects.all()[page*10:(page+1)*10]

	return render(request, "reports.html", {"count":count, "page":page+1, "pages":pages, "reports":reports, "next":page+1!=count})

def show_report(request, id):
	report = Report.objects.get(id=id)
	
	return render(request, "report.html", {"report":report})