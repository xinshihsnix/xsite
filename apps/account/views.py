# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

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

def login_in(request):
    pass


def is_username_exists(request):
    username = request.GET.get('username')
    if User.objects.filter(username=username).exists():
        return HttpResponse('yes')
    else:
        return HttpResponse('no')