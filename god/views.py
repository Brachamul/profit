from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Count

# Create your views here.

from towns.models import Town

from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def god_page(request):
	list_of_active_towns = Town.objects.filter(ended=None)
	if request.POST.get('time-goes-by-in') == "all" :
		for town in list_of_active_towns :
			town.phase += 1
			town.save()
	elif request.POST.get('time-goes-by-in') :
		town_slug = request.POST.get('time-goes-by-in')
		town = Town.objects.get(slug=town_slug)
		town.phase += 1
		town.save()
	return render_to_response(
		'god/god_page.html', {'list_of_active_towns': list_of_active_towns},
		context_instance=RequestContext(request)
		)