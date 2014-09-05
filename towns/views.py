from django.shortcuts import render

# Create your views here.

from django.template import RequestContext
from django.shortcuts import render_to_response

def town_map(request):
	context = RequestContext(request)
	return render_to_response(
			'towns/town_map.html',
			context)