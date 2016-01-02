# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import Story


def index(request):
    storys = Story.objects.order_by('-create_time')
    return render_to_response('story/index.html', {'storys': storys})


def detail(request):
    story = Story.objects.get(id=int(request.GET.get('id')))
    return render_to_response('story/detail.html', {'story': story})
