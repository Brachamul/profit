from django.conf.urls import patterns, url

from god import views

urlpatterns = patterns('',
    url(r'^$', views.god_page, name='god_page'),
)
