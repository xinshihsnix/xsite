# coding: utf-8
from django.contrib import admin

from models import Story


class StoryAdmin(admin.ModelAdmin):
    fields = ('title', 'content')


admin.site.register(Story, StoryAdmin)