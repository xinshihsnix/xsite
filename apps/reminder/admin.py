# coding: utf-8
from django.contrib import admin

from models import Company, Reminder


class CompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'is_current')

    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('is_current'):
            obj.__class__.objects.update(is_current=False)      # is_current=True只能有一个
            obj.is_current = True
        obj.save()


class ReminderAdmin(admin.ModelAdmin):
    fields = ('company', 'title', 'content')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Reminder, ReminderAdmin)