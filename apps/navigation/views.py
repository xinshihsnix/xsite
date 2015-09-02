# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import Domain
from ..common.utils import section_list


def domains_get(request):
    domains = Domain.objects.all()
    domains_section = section_list(domains, 3)
    return render_to_response('navigation.html', {'domains_section': domains_section})
