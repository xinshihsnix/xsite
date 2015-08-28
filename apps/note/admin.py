# coding: utf-8
from django.contrib import admin

from models import NoteCategory, Note


class NoteCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)


class NoteAdmin(admin.ModelAdmin):
    fields = ('category', 'title', 'content')

admin.site.register(NoteCategory, NoteCategoryAdmin)
admin.site.register(Note, NoteAdmin)