# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response



def sign_up(request):
    """ 注册 """
    return render_to_response('account/sign_up.html')


def login_in(request):
    pass
