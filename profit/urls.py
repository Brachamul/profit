from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
#	url(r'^$', 'signups.views.home', name='home'),
	url(r'^u/', include('profiles.urls'), name='profiles'),
	url(r'^welcome/', include('welcome.urls'), name='welcome'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^town/', include('towns.urls')),
    url(r'^god/', include('god.urls')),
#	url(r'^blog/', include('blog.urls'), name='blog'),
	url(r'^$', RedirectView.as_view(permanent=False, url='/welcome/')),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)