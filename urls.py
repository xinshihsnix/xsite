from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.views import *
from apps import navigation

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^navigation/', include(navigation.urls)),
)