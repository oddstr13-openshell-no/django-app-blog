#!/usr/bin/env python2
from django import template
from django.utils.safestring import mark_safe

from creole import parse

register = template.Library()

@register.filter(name='creole', is_safe=True)
def creoleparse(value):
    return mark_safe(parse(value))
