from django import template
from django.template.defaultfilters import register, \
    stringfilter
from django.utils.safestring import mark_safe
#from django.conf import settings
#from django.utils.translation import ugettext_lazy as _
import datetime
from nvd3 import pieChart

#Usage
#-----
#
# <head>
#     <!-- code to include the NVD3 and D3 libraries goes here -->
#     <!-- load_nvd3 filter takes a comma-separated list of id's where -->
#     <!-- the charts need to be rendered to                             -->
#     {% load nvd3 %}
#     {% load_chart "pieChart" chartdata "container" %}
# </head>
# <body>
#     <div id='container'> Chart will be rendered here </div>
# </body>


# @register.simple_tag(name='get_app_name')
# def get_app_name(app_label, model_name, object_id):
#     """To get app name from app_label, model_name & object_id
#     Usage: {% get_app_name app_label model_name object_id %}
#     """
#     try:
#         return get_model(app_label, model_name).objects.get(pk=object_id)
#     except:
#         return '-'


@register.simple_tag(name='load_chart')
def load_chart(chart_type, series, render_to=''):
    """Loads the ``Chart`` objects in the ``chart_list`` to the
    HTML elements with id's specified in ``render_to``.

    **Arguments**:

    - **render_to** - id where the chart needs to be rendered to.
    """
    chart = eval(chart_type)(name=chart_type, height=400, width=400)
    chart.set_containerheader("\n\n<h2>" + chart_type + "</h2>\n\n")
    xdata = series['x']
    ydata = series['y']

    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()


    html_string = chart.htmlheader + '\n' + chart.jschart + '\n' + chart.container
    return mark_safe(html_string)


# @register.filter(name='cut')
# def cut(value, arg):
#     """Removes all values of arg from the given string"""
#     return value.replace(arg, '')


@register.filter
@stringfilter
def superlower(value):
    return value.lower()


# Template usage
# {% get_current_time "%Y-%m-%d %I:%M %p" as the_time %}
# <p>The time is {{ the_time }}.</p>
@register.assignment_tag(name='get_current_time')
def get_current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

