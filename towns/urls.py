from django.conf.urls import patterns, url

from towns import views

urlpatterns = patterns('',
	url(r'^$', views.town_map, name='town_map'),
#	url(r'^(?i)(?P<username>\w+)/', views.ProfileView.as_view(), name='profile'),
)
