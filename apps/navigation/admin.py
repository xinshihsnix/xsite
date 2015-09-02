# coding: utf-8
import re
import urllib
from django.contrib import admin

from models import Domain


class DomainAdmin(admin.ModelAdmin):
    fields = ('type', 'url', 'title', 'description')

    def save_model(self, request, obj, form, change):
        # if change:  # 更改的时候
        #     pass
        # else:   # 新增的时候
        #     pass

        url = form.cleaned_data.get('url')
        if not url.startswith('http'):
            url = 'http://' + url
        if url.endswith('/'):
            url = url[:-1]      # http://xx.com/  --> http://xx.com

        # 获取网页标题
        html = urllib.urlopen(url).read()
        m = re.search(r'<title>(.*)</title>', html, flags=re.I)
        title = m.group(1)

        obj.url = url
        obj.title = title
        obj.save()


admin.site.register(Domain, DomainAdmin)