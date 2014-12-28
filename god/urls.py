from django.conf.urls import patterns, url

from god import views

urlpatterns = patterns('',
	url(r'^$', views.god_home, name='god_home'),
	url(r'^(?P<town_slug>[-\w]+)/', views.god_town_info, name='god_town_info'),
)
