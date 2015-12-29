# coding: utf-8
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    url(r'^index/', index),
    url(r'^terminal/', terminal),
    url(r'^leavemessage/', leavemessage),
)