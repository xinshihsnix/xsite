# coding: utf-8
import hashlib

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.conf import settings


def index(request):
    return render_to_response('index.html')


def welcome(request):
    return render_to_response('welcome.html')


@csrf_exempt
def search(request):
    query = request.POST.get('query')
    pwd = request.POST.get('pwd')
    if query and hashlib.md5(query).hexdigest() == settings.EYE_QUERY_MD5:
        return JsonResponse({'result': 'wake_up'})
    if pwd and hashlib.md5(pwd).hexdigest() == settings.EYE_PWD_MD5:
        return render_to_response('monkey/eyes.html')
