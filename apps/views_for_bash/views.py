# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from ..note.models import Note, NoteCategory


def note_category_get_bash(request):
    categories = NoteCategory.objects.all()
    result = ''
    for c in categories:
        result += '  ' + c.name + '\n'
    result += '\n'

    result = 'pwd'
    return HttpResponse(result)