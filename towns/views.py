from django.shortcuts import get_object_or_404, render, render_to_response
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.views.generic import TemplateView, ListView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

# Create your views here.

from django.contrib.auth.models import User
from .models import *
from maps.models import Slot

def town_map(request, town_slug):

	town = get_object_or_404(Town, slug=town_slug)
	# Look for the town which corresponds to the town_slug that was passed through my URL

	try:
		player = Player.objects.filter(user=request.user, left=None).latest('joined') # finds the current player
	except ObjectDoesNotExist:
		player = 'not_in_game' # for new players or people who just finished a game

	list_of_town_slots = list(TownSlot.objects.filter(town=town))
	slot_details = [{} for town_slot in range(len(list_of_town_slots))]
	count = 0
	for town_slot in list_of_town_slots:
		margin_left = town_slot.slot.longitude / 32
		margin_top = town_slot.slot.latitude / 16
		# Here, i used the longitude and latitude and divide them by the map size (3200*1600) to get percentage margins that will be responsive
		slot_details[count] = {
		# From Features
			'name' : town_slot.feature.name,
			'description' : town_slot.feature.description,
		# From Slots
			'number' : town_slot.slot.number,
			'longitude' : town_slot.slot.longitude,
			'latitude' : town_slot.slot.latitude,
		# From my calculations
			'margin_left' : margin_left,
			'margin_top' : margin_top,
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
		# From Dunno
#			'forsale' : False,
			}
		count += 1
		if count == len(list_of_town_slots): # if we've gone through all the slots, let's stop
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



def joinable_towns (request):
	joinable_towns = Town.objects.all().annotate(population=Count('player'))
	return render_to_response('towns/town_join.html', {'joinable_towns': joinable_towns,}, context_instance=RequestContext(request))



### Slot Views

def get_town_slot (town_slug, slot_number):
	# Reusable function for fetching a TownSlot
	master_slot = Slot.objects.get(number=int(slot_number))
	town = Town.objects.get(slug=town_slug)
	town_slot = TownSlot.objects.get(slot=master_slot, town=town)
	return town_slot

def slot_info(request, town_slug, slot_number):
	if request.POST.get('bid'): purchase(request, town_slug, slot_number)
#	if request.POST.get('bid') : messages.success(request, 'You placed a bid of %s !' % (request.POST.get('bid')))
	return render_to_response(
		'towns/slot_info.html',
		{'town_slot': get_town_slot(town_slug, slot_number),},
		context_instance=RequestContext(request)
		)

def slot_purchase(request, town_slug, slot_number):
	return render_to_response(
		'towns/slot_purchase.html',
		{'town_slot': get_town_slot(town_slug, slot_number),},
		context_instance=RequestContext(request)
		)

def purchase(request, town_slug, slot_number):
	bid = request.POST.get('bid') # Set 'bid' to whatever was posted in the form
	try: bid.isdigit() # Is the bid made of digits, meaning, is it valid ?
	except ValueError: messages.error(request, 'It looks like your "%s" bid was invalid ! A bid should contain only numbers.' % (bid))
	messages.success(request, 'You placed a bid of %s !' % (bid))


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