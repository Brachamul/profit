from django.conf.urls import patterns, url

from towns import views

urlpatterns = patterns('',
#	url(r'^$', views.town_map, name='town_map'),
	url(r'^(?i)(?P<town_slug>\w+)/', views.TownMapView.as_view(), name='town_map'),
)
