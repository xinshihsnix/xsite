from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^read_eye/', read_eye),
)