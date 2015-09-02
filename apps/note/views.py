# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response

from models import Note, NoteCategory


def note_category_get(request):
    categories = NoteCategory.objects.all()
    return render_to_response('note/category.html', {'categories': categories})

def notes_get(request):
    category = NoteCategory.get_by_str_id(request.GET.get('cid'))

    notes = Note.objects.filter(category=category)
    return render_to_response('note/note.html', {'notes': notes})