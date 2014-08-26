from django.conf.urls import patterns, url

from welcome import views

urlpatterns = patterns('',
	url(r'^$', views.welcome, name='welcome'),
#	url(r'^$', views.WelcomeView.as_view(), name='welcome'),
)
