from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from polls import views

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$',views.results, name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$',views.vote, name='vote'),
    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
