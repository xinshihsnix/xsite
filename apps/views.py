# coding: utf-8
import hashlib

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.http import JsonResponse
from django.conf import settings

from common.utils import TimeUtils

def index(request):
    return render_to_response('index.html')


def welcome(request):
    return render_to_response('welcome.html')


@csrf_exempt
def search(request):
    try:
        query = request.POST.get('query')
        pwd = request.POST.get('pwd')
        if query:
            if hashlib.md5(query).hexdigest() == settings.EYE_QUERY_MD5:
                request.session['xinshi_flag_A'] = True
                return JsonResponse({'result': 'wake_up'})
            else:
                request.session['xinshi_flag_A'] = False

        if pwd and hashlib.md5(pwd).hexdigest() == settings.EYE_PWD_MD5:
            if request.session['xinshi_flag_A']:
                request.session['whoareyou'] = 'i_am_xinshi'
            return render_to_response('monkey/eyes.html')
    except Exception, e:
        print 'eee:', e


@csrf_exempt
def upload_file(request):
    try:
        pi_img = request.FILES.get('pi_img')
        if pi_img:
            dest = '{0}/{1}.jpg'.format(settings.PI_IMG_STORE_PATH, TimeUtils.int_time_to_str_format())
            with open(dest, "wb+") as destination:
                for chunk in pi_img.chunks():
                    destination.write(chunk)
            return JsonResponse({'result': 'upload_success'})
    except Exception, e:
        print 'upload_file Exception:', e

