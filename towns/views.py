from django.shortcuts import get_object_or_404, render, render_to_response
from django.db.models import Count
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.views.generic import TemplateView, ListView
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

from django.contrib.auth.models import User
from .models import Town, Player


class TownMapView(TemplateView):

	template_name = 'towns/town_map.html'

	def get_context_data(self, **kwargs):

		context = super(TownMapView, self).get_context_data()

		town = get_object_or_404(Town, slug=self.kwargs['town_slug'])
		context['town'] = town

		try:
			player = Player.objects.filter(user=self.request.user, left=None).latest('joined') # finds the current player
			context['player'] = player
		except ObjectDoesNotExist:
			context['player'] = 'not_in_game' # for new players or people who just finished a game

		return context



class JoinTownView(ListView):

	model = Town

	context_object_name = "open_towns"

	queryset = Town.objects.all().annotate(population=Count('player'))