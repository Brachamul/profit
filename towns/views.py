from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, ListView

# Create your views here.

from django.contrib.auth.models import User
from .models import *
from maps.models import *
from assets.models import *

@login_required
def town_map(request, town_slug):

	town = get_object_or_404(Town, slug=town_slug) # Look for the town which corresponds with the town_slug that was passed through my URL
	player = get_current_player(request)

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
			'town' : town_slot.town,
#			'stored_items' : 0,
		# From Illustrations
			'illustration' : town_slot.illustration,
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



### Slots !


def get_town_slot (town_slug, slot_number):
	# Reusable function for fetching a TownSlot
	town = Town.objects.get(slug=town_slug)
	master_slot = Slot.objects.get(map_layout=town.map_layout, number=int(slot_number))
	town_slot = TownSlot.objects.get(slot=master_slot, town=town)
	return town_slot


# main slot view
@login_required
def slot_info(request, town_slug, slot_number):
	
	town_slot = get_town_slot(town_slug, slot_number)
	player = get_current_player(request)

	# Purchasing and selling slots
	if request.POST.get('bid'): purchase(request, town_slot) # if a bid is placed, roll the purchasing code
	if request.POST.get('sell-slot') == "sell" : sell_slot(request, town_slot)
	bid = get_bid(town_slot, player)

	# Runs
	runs = get_runs(town_slot, player)
	
	return render_to_response(
		'towns/slot_info.html',	{
			'town_slot': town_slot,
			'player': player,
			'bid': bid,
			'runs': runs
			},
		context_instance=RequestContext(request)
		)



### Purchasing and selling slots


from django.utils import timezone
from datetime import timedelta
def sell_slot(request, town_slot):
	town_slot.on_sale = timezone.now() + timedelta(days=1)
	town_slot.save()
	messages.success(request, "Auction for the sale of this land has begun.")


def purchase(request, town_slot):
	bid = request.POST.get('bid') # Set 'bid' to whatever was posted in the form
	try: bid.isdigit() # Is the bid made of digits, meaning, is it valid ?
	except ValueError: messages.error(request, "It looks like your '%s' bid was invalid ! A bid should contain only numbers." % (bid))
	bid = int(bid)
	player = get_current_player(request)
	if player.cash >= bid : pass # does the player have enough cash for this bid ?
	else : messages.error(request, "You don't have the necessary funds to place a bid of <span class='cash'>%d</span> !" % (bid))
	if bid >= town_slot.feature.min_price  : pass # does the bid match the minimum purchase price ?
	else : messages.error(request, "The bid you placed was lower than the price set by the King." % (bid))
	if town_slot.on_sale != None : pass
	else : sell_slot(request, town_slot) 
	messages.success(request, "You placed a bid of %d !" % (bid))
	player.cash -= bid
	player.save()
	create_bid(bid, player, town_slot)


def create_bid(amount, player, town_slot):
	new_bid = Bid(amount=amount, player=player, town_slot=town_slot)
	new_bid.save()


def get_bid(town_slot, player):
	try: bid = Bid.objects.get(town_slot=town_slot, player=player) # finds the current player
	except ObjectDoesNotExist: bid = None # for new players or people who just finished a game
	return bid



### Joining and leaving a Town


def joinable_towns(request): # A page that lists towns available for joining
	joinable_towns = Town.objects.all().annotate(population=Count('player'))
	return render_to_response('towns/town_join.html', {'joinable_towns': joinable_towns,}, context_instance=RequestContext(request))


def create_player(request):
	context = RequestContext(request)
	if request.method == 'POST': # check if post data has been sent through the join town page
		town_slug = request.POST.get('town_to_join')
		town = Town.objects.get(slug=town_slug)
		user = request.user
		new_player = Player(town=town, user=user)
		new_player.save()
		return HttpResponseRedirect('/town/')


def get_current_player(request):
	# Get the current "player" instance based on the current logged-in user
	try: player = Player.objects.filter(user=request.user, left=None).latest('joined') # finds the current player
	except ObjectDoesNotExist: player = 'not_in_game' # for new players or people who just finished a game
	return player


def current_town(request):
	try:
		player = get_current_player(request)
		return HttpResponseRedirect('/town/%s' % player.town.slug)
	except ObjectDoesNotExist:
		return HttpResponseRedirect('/town/join')


import datetime
def leave_town(request):
	player = get_current_player(request)
	player.left = datetime.datetime.now()
	player.save()
	return HttpResponseRedirect('/u/myprofile/')



### Joining and leaving a Town


def get_runs(town_slot, player):

	# Collect development runs
	development_runs = list()
	for development_project in DevelopmentProject.objects.filter(was=town_slot.feature) :
		# insert techtree check here
		development_runs.append(development_project)

	# Collect upgrade runs
	upgrade_runs = list()
	for upgrade in Upgrade.objects.filter(feature=town_slot.feature) :
		# insert techtree check here
		upgrade_runs.append(upgrade)

	return {'development_runs': development_runs, 'upgrade_runs': upgrade_runs}

