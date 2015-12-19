# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login

from models import User


@csrf_exempt
def sign_up(request):
    """ 注册 """
    if request.method == 'GET':
        return render_to_response('account/sign_up.html')

    if request.method == 'POST':
        print request.POST
        user = User()
        user.username=request.POST.get('username')
        user.raw_password=request.POST.get('raw_password')
        user.set_password(request.POST.get('raw_password'))
        user.email=request.POST.get('email')
        user.save()
        # return HttpResponse('ok')
        return HttpResponseRedirect('/index')


@csrf_exempt
def sign_in(request):
    if request.method == 'GET':
        return render_to_response('account/sign_in.html')

    if request.method == 'POST':
        print request.POST
        username=request.POST.get('username')
        raw_password=request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            return JsonResponse({'is_success': True})
        else:
            return JsonResponse({'is_success': False})


def is_username_exists(request):
    username = request.GET.get('username')
    if User.objects.filter(username=username).exists():
        return HttpResponse('yes')
    else:
        return HttpResponse('no')