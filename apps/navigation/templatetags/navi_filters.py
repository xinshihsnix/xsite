# coding: utf-8
from django import template

register = template.Library()


@register.filter(name='string_cut')
def string_cut(s):
    return s[:55]