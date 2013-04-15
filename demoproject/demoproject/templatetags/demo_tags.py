from django import template
from django.template.defaultfilters import register, \
    stringfilter


@register.filter
@stringfilter
def demo(value):
    return value.lower()
