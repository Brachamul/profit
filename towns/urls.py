from django.conf.urls import patterns, include, url

from django.conf import settings

from django.views.generic.base import RedirectView

from towns import views

urlpatterns = patterns('',
	url(r'^leave/$', views.leave_town, name='leave_town'),
	url(r'^join/$', views.joinable_towns, name='joinable_towns'),
	url(r'^create_player/$', views.create_player, name='create_player'),
	url(r'^$', views.current_town, name='current_town'),
	url(r'^(?P<town_slug>[-\w]+)/', include(patterns('',
		# the dash means i accept dashes in the name, ie for slugs
		# the \w is here to say i accept words
		# the + sign says that i can accept several of these items
		# the (?i) should say that i'll ignore upper/lower case, but doesn't work
		# tried something like ([-\w]+)/i but didn't work either
		url(r'^$', views.town_map, name='town_map'),
		url(r'^slot/(?P<slot_number>[\d]+)/', include(patterns('',
			# the \d says to accept only digits
			# the + sign says there can be several of them
			url(r'^$', views.slot_info, name='slot_info'),
			url(r'^purchase/', views.slot_purchase, name='slot_purchase'),
			))),
		))),
	)
