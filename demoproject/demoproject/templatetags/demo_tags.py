#from django import template
from django.template.defaultfilters import register


@register.filter
def demo(value):
    return value + 'demo'
