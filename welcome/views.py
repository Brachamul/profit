from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

#	class WelcomeView(TemplateView):
#		template_name = 'welcome/welcome.html'


from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def welcome(request):
	if request.user.is_authenticated() :
		return HttpResponseRedirect('/u/myprofile')
	else :
		return render_to_response('welcome/welcome.html')