# coding: utf-8
from django.contrib import admin

from models import Domain


class DomainAdmin(admin.ModelAdmin):
    fields = ('url', 'title', 'description')


    def save_model(self, request, obj, form, change):
        if change:  # 更改的时候
            pass
        else:   # 新增的时候
            pass

        obj.save()


admin.site.register(Domain, DomainAdmin)