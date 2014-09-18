from django.shortcuts import get_object_or_404, render, render_to_response
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.views.generic import TemplateView, ListView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

from django.contrib.auth.models import User
from .models import *


def town_map(request, town_slug):

	town = get_object_or_404(Town, slug=town_slug)

	try:
		player = Player.objects.filter(user=request.user, left=None).latest('joined') # finds the current player
	except ObjectDoesNotExist:
		player = 'not_in_game' # for new players or people who just finished a game

	list_of_town_slots = list(TownSlot.objects.filter(town=town))
	slot_details = [{} for town_slot in range(len(list_of_town_slots))]
	count = 0
	for town_slot in list_of_town_slots:
		slot_details[count] = {
		# From Features
			'name' : town_slot.feature.name,
			'description' : town_slot.feature.description,
		# From Slots
			'number' : town_slot.slot.number,
			'longitude' : town_slot.slot.longitude,
			'latitude' : town_slot.slot.latitude,
		# From TownSlots
			'owner' : town_slot.owner,
#			'stored_items' : 0,
		# From Illustrations
#			'file_name' : 'placeholder.png',
#			'shape' : '30,0,61,15,31,31,0,16',
#			'vertical-offset' : 0,
#			'horizontal-offset' : 0,
		# From Upgrades / Features
#			'buttons' : '<a href="build"></a>',
			}
		count += 1
		if count == len(list_of_town_slots):
			break

	return render_to_response('towns/town_map.html', {
		'town': town,
		'player': player,
		'slot_details': slot_details
		})

	town = models.ForeignKey(Town)
	slot = models.ForeignKey(Slot) # Finds the coordinates and starting feature of this Slot
	owner = models.ForeignKey(Player, null=True, default=None)
	feature = models.ForeignKey(Feature)
	stored_items = models.ManyToManyField(Item, through='StoredItems')



class JoinTownView(ListView):
	model = Town
	context_object_name = "open_towns"
	queryset = Town.objects.all().annotate(population=Count('player'))



### Make user join town by creating a 'player' within that town

def create_player(request):

	context = RequestContext(request)

	if request.method == 'POST': # check if post data has been sent through the join town page
		town_slug = request.POST.get('town_to_join')
		town = Town.objects.get(slug=town_slug)
		user = request.user
		new_player = Player(town=town, user=user)
		new_player.save()
		return HttpResponseRedirect('/town/')

def current_town(request):
	try:
		player = Player.objects.filter(user=request.user, left=None).latest('joined') # finds the current player
		return HttpResponseRedirect('/town/%s' % player.town.slug)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/town/join')


import datetime

def leave_town(request):
	player = Player.objects.filter(user=request.user, left=None).latest('joined')
	player.left = datetime.datetime.now()
	player.save()
	return HttpResponseRedirect('/u/myprofile/')