from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import *

def campaigns(request, campaign_id=None):
	if campaign_id:
		c = Campaign.objects.get(id=campaign_id)
		return render(request, "campaign.html", {"campaign":c, "endorsed":not request.user.is_anonymous() if request.user.is_anonymous() else c.users.filter(user=request.user).count()>0})
	else:
		return render(request, "campaigns.html", {"campaigns":Campaign.objects.all()})

def api_campaings(request, campaign_id=None):
	if campaign_id:
		return HttpResponse(json.dumps(Campaign.objects.get(id=campaign_id).to_json(list=False)))
	else:
		return HttpResponse(json.dumps([c.to_json(list=True) for c in Campaign.objects.all()]))


@csrf_exempt
def add_project(request, campaign_id):
	if request.method == "GET":
		return render(request, "add_project.html", {"campaign":Campaign.objects.get(id=campaign_id)})
	else:
		project = request.POST.get("url")
		m = get_project(project)

		cp = CampaignProject()
		cp.campaign = Campaign.objects.get(id=campaign_id)
		cp.project = macostools
		cp.save()

		return HttpResponseRedirect("/campaigns/%s" % campaign_id)

def get_project(url):
	if "opencoesione" in url:
		m = project_from_OC(url)
	return m

def endorse(request, campaign_id):
	cu,c = CampaignUser.objects.get_or_create(user=request.user, campaign=Campaign.objects.get(id=campaign_id))
	return HttpResponseRedirect("/campaigns/%s"%campaign_id)

def unendorse(request, campaign_id):
	CampaignUser.objects.filter(user=request.user, campaign__id=campaign_id).delete()
	return HttpResponseRedirect("/campaigns/%s"%campaign_id)

def project_from_OC(url):
	"""origin: http://opencoesione.gov.it/progetti/1mise788/"""
	"""target: http://opencoesione.gov.it/api/progetti/1mise788?format=json"""
	print url
	url = url.replace("progetti", "api/progetti")[:-1]+"?format=json"
	print url
	
	data = requests.get(url).json()
	m = Monitorable()
	m.title = data.get("titolo_progetto")
	m.description = data.get("descrizione")
	#m.category = MonitorableCategory.objects.get()
	#m.cup = 
	#m.oc_slug = 
	#m.oc_url = 
	#m.total_amount = 
	#m.paid_amount = 
	#m.paid_percent = 
	#m.date_from = 
	#m.date_to = 
	m.save()
	#m.subjects = []
	#m.locations = []
	#m.tags = []
	#m.save_m2m()
	return m
