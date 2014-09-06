from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views.generic.base import TemplateView

# Create your views here.

from .models import Town

#	def town_map(request):
#		context = RequestContext(request)
#		return render_to_response(
#				'towns/town_map.html',
#				context)


class TownMapView(TemplateView):
	template_name = 'towns/town_map.html'

	def get_context_data(self, **kwargs):
		context = super(TownMapView, self).get_context_data()
		town = get_object_or_404(Town, slug=self.kwargs['town_slug'])
		context['town_object'] = town
		return context
