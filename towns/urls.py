from django.conf.urls import patterns, url

from towns import views

urlpatterns = patterns('',
    url(r'^join/$', views.JoinTownView.as_view(), name='join_a_new_town'),
	url(r'^(?i)(?P<town_slug>\w+)/', views.TownMapView.as_view(), name='town_map'),
)
