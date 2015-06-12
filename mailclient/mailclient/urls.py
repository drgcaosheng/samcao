from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mailclient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon\.ico$','django.views.generic.simple.redirect_to',{'url':'/static/images/favicon.ico'}),
)# + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

urlpatterns += patterns('mailclient.views',
    (r'^$','hello'),
    (r'^hello/$','hello'),
    (r'^now/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'),
)
