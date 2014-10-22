from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.http import HttpResponse

from customforms.models import FormFieldOption
from reports.models import *
from projects.models import Monitorable
from monitor.models import MonitoringTeam
from django.views.decorators.csrf import csrf_exempt

import json

from reports.models import *


@login_required
def new_report(request):
	p = {"forms":["standard"]}
	if request.REQUEST.get("project"):
		p["project"] = Monitorable.objects.get(id=request.REQUEST.get("project"))
	return render(request, "new_report.html", p)



@csrf_exempt 
@login_required
def push_report(request):
	data = request.REQUEST.get("data", "{}")
	data = json.loads(data)

	r = Report()
	r.author = MonitoringTeam.objects.get(id=request.REQUEST.get("team"))
	r.project = Monitorable.objects.get(id=request.REQUEST.get("project"))
	r.save()

	for area in data["report"]:
		rf = ReportForm()
		rf.form = CustomForm.objects.get(id=area["origin"])
		rf.report = r
		rf.save()

		for field in area["data"]:
			rff =ReportFormField()
			rff.report_form = rf
			rff.field = FormFieldOption.objects.get(id=field["name"])
			rff.value = field["value"]

			rff.save()

	return HttpResponse(json.dumps({"message":"result", "type":"OK", "id":r.id}))

def list_reports(request):

	page = int(request.REQUEST.get('p', "1"))-1

	count = Report.objects.filter(finalized=True).count()
	pages = int(count / 10)

	reports = Report.objects.filter(finalized=True)[page*10:(page+1)*10]

	return render(request, "reports.html", {"count":count, "page":page+1, "pages":pages, "reports":reports, "prev":page, "next":page+2})

def show_report(request, id):
	report = Report.objects.get(id=id)
	
	return render(request, "report.html", {"report":report})

def reports_json(request):
	ret = {
		"type":"FeatureCollection",
		"features":[{
			"type":"Feature",
			"geometry":json.loads(r.position.json),
			"properties":{
				"title":r.title,
				"id":r.id
			}
		} for r in Report.objects.filter(finalized=True)]
	}

	return HttpResponse(json.dumps(ret))