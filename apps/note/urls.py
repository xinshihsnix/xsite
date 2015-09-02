# coding: utf-8
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^category/', note_category_get),
    url(r'^notes_title/', notes_get),
)