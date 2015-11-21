# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from ..common.decorator import xinshi_only
from ..common.utils import time_now_str


@xinshi_only()
def read_eye(request):
    image_data = open('/var/pi_media/{0}.jpg'.format(time_now_str()))
    return HttpResponse(image_data,content_type="image/png")