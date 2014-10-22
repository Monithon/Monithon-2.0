from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

def index(request):
	return render(request, "index.html")

def logins(request):
	return render(request, "logins.html", {
		"socials":[{
			"name":"GitHub", 
			"icon":"fa-github",
			"url":"github"
		},{
			"name":"Facebook", 
			"icon":"fa-facebook-square",
			"url":"facebook"
		},{
			"name":"Twitter", 
			"icon":"fa-twitter",
			"url":"twitter"
		},{
			"name":"A Scuola di Open Coesione", 
			"icon":"fa-circle",
			"url":"asoc"
		}]})

def profile(request, username=None):
	if username is None:
		return HttpResponseRedirect(reverse("monithon.views.profile", kwargs={"username":request.user.username}))

	own = request.user.username == username


	selected_user = User.objects.get(username=username)

	# import code for encoding urls and generating md5 hashes
	import urllib, hashlib
	 
	# Set your variables here
	email = selected_user.email
	size = 100
	 
	# construct the url
	gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	gravatar_url += urllib.urlencode({'s':str(size)})


	return render(request, "profile.html", {

		"is_own":request.user.username == username,
		"selected_user":selected_user,

		"profile":{
			"username":selected_user.username,
			"email":selected_user.email,
			"gravatar":gravatar_url,

		},
		"socials":[{
			"name":"GitHub", 
			"icon":"fa-github",
			"url":"github"
		},{
			"name":"Facebook", 
			"icon":"fa-facebook-square",
			"url":"facebook"
		},{
			"name":"Twitter", 
			"icon":"fa-twitter",
			"url":"twitter"
		},{
			"name":"A Scuola di Open Coesione", 
			"icon":"fa-circle",
			"url":"asoc"
		}]
	})


from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	return HttpResponseRedirect("/")
