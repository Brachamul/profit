from django.conf.urls import patterns, url

from towns import views

urlpatterns = patterns('',
	url(r'^leave/$', views.leave_town, name='leave_town'),
	url(r'^join/$', views.JoinTownView.as_view(), name='join_a_new_town'),
	url(r'^create_player/$', views.create_player, name='create_player'),
	url(r'^(?i)(?P<town_slug>[-\w]+)/$', views.TownMapView.as_view(), name='town_map'),
	url(r'^$', views.current_town, name='current_town'),
)
