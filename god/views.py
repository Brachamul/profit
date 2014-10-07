from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Count, Max

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
		for town_slot in list_of_onsale_townslots :
			if timezone.now() > town_slot.on_sale : # Checks if the auction's time is up
				list_of_bids = Bid.objects.filter(town_slot=town_slot)
				highest_bid = list_of_bids.aggregate(Max('amount'))
				for bid in list_of_bids :
					if bid == highest_bid :
						town_slot.owner = bid.player
						messages.success(request, "%s has successfully purchased %s for %d." % (bid.player, town_slot, bid.amount))
						# notify successful purchase
			#		else :
			#			refund
						# notify unsuccessful purchase and amount of successful purchase
				town_slot.on_sale = None
