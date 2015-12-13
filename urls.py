# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from apps.views import *
from apps import navigation, note, views_for_bash, pi, fantasy, account

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^ckeditor/', include('ckeditor.urls')),    # django富文本

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^welcome/', welcome),
    url(r'^search/', search),
    url(r'^upload_file/', upload_file),

    url(r'^pi/', include(pi.urls)),
    url(r'^navigation/', include(navigation.urls)),
    url(r'^note/', include(note.urls)),
    url(r'^bash/', include(views_for_bash.urls)),
    url(r'^fantasy/', include(fantasy.urls)),
    url(r'^account/', include(account.urls)),
)


if settings.DEBUG:
   urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
                            url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
                           )