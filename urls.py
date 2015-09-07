# coding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.views import *
from apps import navigation, note, views_for_bash

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),    # django富文本

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', index),
    url(r'^welcome/', welcome),
    url(r'^navigation/', include(navigation.urls)),
    url(r'^note/', include(note.urls)),

    url(r'^bash/', include(views_for_bash.urls)),
)