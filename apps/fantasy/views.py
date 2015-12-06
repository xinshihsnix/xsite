# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response


def nighter_index(request):
    try:
        from api.im_port.ip import get_address_from_ip
        print 'xxx'

        if request.META.has_key('HTTP_X_FORWARDED_FOR'):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']

        print ip
        address = get_address_from_ip(ip)
        print ip
        return render_to_response('fantasy/nighter/index.html', {'address': address })
    except Exception, e:
        print e