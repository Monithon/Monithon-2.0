
from projects.models import MonitorableCategory

def request(req):
	return {"categories":MonitorableCategory.objects.all()}