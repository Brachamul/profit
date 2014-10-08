from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Count, Max, Min
import logging

# Create your views here.

from towns.models import *

from django.contrib.admin.views.decorators import staff_member_required
@staff_member_required
def god_page(request):
	list_of_active_towns = Town.objects.filter(ended=None)
	advance_phase(request, list_of_active_towns) # If one of the time-goes-by buttons were pressed.
	complete_auctions(request) # Check if any auction has run its course. If so, process bids and assign new owner.
	return render_to_response(
		'god/god_page.html', {'list_of_active_towns': list_of_active_towns},
		context_instance=RequestContext(request)
		)

def advance_phase(request, list_of_active_towns) :
	if request.POST.get('time-goes-by-in') == "all" :
		logger.debug('Advancing all towns by one phase.')
		for town in list_of_active_towns :
			town.phase += 1
			town.save()
	elif request.POST.get('time-goes-by-in') :
		town_slug = request.POST.get('time-goes-by-in')
		town = Town.objects.get(slug=town_slug)
		town.phase += 1
		town.save()

from django.utils import timezone
def complete_auctions(request) :
	if request.POST.get('complete-auctions') == "all" :
		list_of_onsale_townslots = TownSlot.objects.exclude(on_sale=None)
		messages.debug(request, "Okay, we got a request to complete ALL auctions.")
		for town_slot in list_of_onsale_townslots :
			messages.debug(request, '%s, slot %s' % (town_slot.town.name, town_slot.slot.number))
			if timezone.now() > town_slot.on_sale : # Checks if the auction's time is up
				list_of_bids = Bid.objects.filter(town_slot=town_slot)
				highest_bid = Bid.objects.filter(town_slot=town_slot).aggregate(Max('amount'))
				highest_bid = highest_bid['amount__max']
				if highest_bid == None :
					# No bids have been placed, so far.
					messages.debug(request, 'No bids have been placed, so far.')
				else :
					bids_with_highest_amount = Bid.objects.filter(town_slot=town_slot, amount=highest_bid)
					messages.debug(request, 'Highest bid : %s' % (highest_bid))
					if bids_with_highest_amount.count() > 1 :
						messages.debug(request, 'Several players have bid the same amount.')
						oldest_player_join_date = timezone.now()
						for bid in bids_with_highest_amount :
							if bid.player.joined < oldest_player_join_date :
								oldest_player_join_date = bid.player.joined
								oldest_player = bid.player
						messages.debug(request, 'Oldest player seems to be %s.' % (oldest_player))
						winner = oldest_player
					elif bids_with_highest_amount.count() == 1 :
						for bid in bids_with_highest_amount :
							winner = bid.player
					for bid in list_of_bids :
						if bid.player == winner :
							town_slot.owner.cash += bid.amount
							town_slot.owner.save() # Transfer the bid money to the former owner
							town_slot.owner = bid.player
							town_slot.save() # Grant ownership to the purchaser
							# [todo] notify successful purchase
						else :
							bid.player.cash += bid.amount
							bid.player.save() # Refund player with unsuccessful bid money
							# [todo] notify unsuccessful purchase and amount of successful purchase
						bid.delete()
					messages.success(request, "%s has successfully purchased slot %s for %d." % (winner, town_slot.slot.number, highest_bid))
				town_slot.on_sale = None # End auction
				town_slot.save()
				messages.debug(request, "Auction for slot %s is now complete." % (town_slot))
			else :
				messages.info(request, 'Auction is still running.')