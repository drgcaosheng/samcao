from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mailclient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('mailclient.views',
    (r'^$','hello'),
    (r'^hello/$','hello'),
    (r'^now/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'),
)
