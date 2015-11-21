# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response


def read_eye(request):
    image_data = open('/var/pi_media/qrcode_for_gh_fc95b1a44e37_1280.jpg')
    return HttpResponse(image_data,content_type="image/png")