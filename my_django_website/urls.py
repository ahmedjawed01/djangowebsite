
from django.conf.urls import *  
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
from myapp.views import * 

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)), 
    url(r'^$', home), 
    url('^(?P<page_slug>.*)/$', article),
    url('^notfound/$', home),
    url(r'^sitemap\.xml$',generate_sitemap),
)


# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns  # NOQA
#If you have any question about Django visit www.djangotutsme.com
