from django.conf.urls import patterns, include, url
from mysite.views import hello, my_homepage_view, current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       ('^$',my_homepage_view),
                       ('^hello/$', hello),
                       ('^time/$', current_datetime),
                       (r'^time/plus/(\d{1,2})/$',hours_ahead),
)
