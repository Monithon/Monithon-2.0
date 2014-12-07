
from campaigns.models import Campaign

def request(req):
	return {"campaigns":Campaign.objects.filter(active=True)}