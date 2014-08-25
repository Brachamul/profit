from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'signups.views.home', name='home'),
	url(r'^u/', include('profiles.urls'), name='profiles'),
	url(r'^admin/', include(admin.site.urls)),
#	url(r'^blog/', include('blog.urls'), name='blog'),
#	url(r'^$', RedirectView.as_view(permanent=False, url='/blog/')),
)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
						  document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
						  document_root=settings.MEDIA_ROOT)