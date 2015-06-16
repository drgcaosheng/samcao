from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mailclient.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^favicon\.ico$','django.views.generic.simple.redirect_to',{'url':'/static/images/favicon.ico'}),
)

urlpatterns += patterns('mailclient.views',
    (r'^$','webmail'),
    (r'^hello/$','hello'),
    (r'^now/$','current_datetime'),
    (r'^time/plus/(\d{1,2})/$','hours_ahead'),
)

urlpatterns += patterns('webmail.views',
    (r'^test/$','test'),
    (r'^display/','ua_display_good'),
    (r'^displayall/','display_meta'),
)