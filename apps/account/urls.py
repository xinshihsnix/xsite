# coding: utf-8
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    url(r'^sign_up/', sign_up),
    url(r'^is_username_exists/', is_username_exists),
)