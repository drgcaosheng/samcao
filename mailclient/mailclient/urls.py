from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # ('^hello/$',hello),
    # Examples:
    # url(r'^$', 'mailclient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('mailclient.views',
    ('^hello/$','hello'),
)
