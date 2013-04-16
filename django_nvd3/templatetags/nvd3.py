from django import template
from django.template.defaultfilters import register, \
    stringfilter
from django.utils.safestring import mark_safe
#from django.conf import settings
#from django.utils.translation import ugettext_lazy as _
import datetime
from nvd3 import pieChart


# <head>
#     <!-- code to include the NVD3 and D3 libraries goes here -->
#     <!-- load_nvd3 filter takes a comma-separated list of id's where -->
#     <!-- the charts need to be rendered to                             -->
#     {% load nvd3_graph %}
#     {{ chartname|load_charts:"container" }}
# </head>
# <body>
#     <div id='container'> Chart will be rendered here </div>
# </body>


@register.assignment_tag(name='load_nvd3')
def load_nvd3(chart_type, series, render_to=''):
    """Loads the ``Chart`` objects in the ``chart_list`` to the
    HTML elements with id's specified in ``render_to``.

    **Arguments**:

    - **render_to** - id where the chart needs to be rendered to.
    """
    type = "pieChart"
    chart = pieChart(name=type, height=400, width=400)
    chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]

    chart.add_serie(y=ydata, x=xdata)
    chart.buildhtml()

    #jschart
    #container
    #htmlheader
    return mark_safe(chart.htmlcontent)


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
