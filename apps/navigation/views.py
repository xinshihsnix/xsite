# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import Domain

def domain_get(request):
    domains = Domain.objects.all()
    return render_to_response('../templates/navigation.html', {'domains': domains})