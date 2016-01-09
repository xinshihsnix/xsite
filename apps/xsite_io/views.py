# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from ..common.services import CrawlService


def save_imgs_from_url(request):
    url = request.GET.get('url')
    img_format = request.GET.get('img_format', 'jpg')

    img_list = CrawlService.get_img_list_from_url(url, img_format)
    for _url in img_list:
        CrawlService.save_img_from_url_to_db(_url)
    return render_to_response('note/category.html', {'img_list': img_list})
