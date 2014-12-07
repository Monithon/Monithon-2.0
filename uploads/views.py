from django.shortcuts import render

from projects.models import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
import datetime
from django.views.decorators.csrf import csrf_exempt
from uploads.models import *
from projects.models import *
import mimetypes

@csrf_exempt
def upload(request, project_id):
	if request.method=="GET":
		return render(request, "upload.html", {"project":Monitorable.objects.get(id=project_id)})
	else:
		try:

			f = request.FILES['file']
			relative_to = request.REQUEST.get("date")

			upload_type=request.REQUEST.get("filetype")

			u = Upload()
			u.data = f
			u.project = Monitorable.objects.get(id=project_id)
			print relative_to
			u.relative_to = datetime.datetime.strptime(relative_to, "%Y-%m-%d").date()
			u.filename = u.data.filename
			u.upload_type = upload_type

			if not request.user.is_anonymous():
				u.author = request.user
			u.save()
			if request.REQUEST.get("lat") and request.REQUEST.get("lon"):
				up = UploadPosition()
				up.upload = u
				up.lon = float(request.REQUEST.get("lon"))
				up.lat = float(request.REQUEST.get("lat"))
				up.save()

			return HttpResponseRedirect("/projects/%s" % project_id)
		except Exception as e:
			return HttpResponse(str(e))


def download(request, project_id, upload_id):
	try:
		u = Upload.objects.get(id=upload_id)
		response = HttpResponse(u.data.open("rb").read())

		type, encoding = mimetypes.guess_type(original_filename)
		if type is None:
			type = 'application/octet-stream'
		response['Content-Type'] = type
		response['Content-Length'] = str(os.stat(file_path).st_size)
		if encoding is not None:
			response['Content-Encoding'] = encoding

    	# To inspect details for the below code, see http://greenbytes.de/tech/tc2231/
		if u'WebKit' in request.META['HTTP_USER_AGENT']:
	        # Safari 3.0 and Chrome 2.0 accepts UTF-8 encoded string directly.
			filecmpname_header = 'filename=%s' % original_filename.encode('utf-8')
		elif u'MSIE' in request.META['HTTP_USER_AGENT']:
	        # IE does not support internationalized filename at all.
        # itertools can only recognize internationalized URL, so we do the trick via routing rules.
			filename_header = ''
		else:
        	# For others like Firefox, we follow RFC2231 (encoding extension in HTTP headers).
			filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(original_filename.encode('utf-8'))
		response['Content-Disposition'] = 'attachment; ' + filename_header
	except:
		response= HttpResponse("FileError")
	return response