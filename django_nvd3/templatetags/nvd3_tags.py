from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
#from django.conf import settings
#from django.utils.translation import ugettext_lazy as _
#import datetime
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart
from nvd3.NVD3Chart import NVD3Chart


@register.simple_tag(name='load_chart')
def load_chart(chart_type, series, container, height=400, width=400, y_is_date=False, kwargs=None):
    """Loads the Chart objects in the container.


    **Arguments**:

    - **render_to** - id where the chart needs to be rendered to.
    """
    chart = eval(chart_type)(name=container, date=y_is_date, height=height, width=width)
    xdata = series['x']
    y_axis_list = [d for d in series.keys() if 'y' in d]
    for key in y_axis_list:
        ydata = series[key]
        if chart_type == 'linePlusBarChart' and kwargs and key == 'y1':
            chart.add_serie(y=ydata, x=xdata, **kwargs)
        else:
            chart.add_serie(y=ydata, x=xdata)

    chart.buildhtml()

    html_string = chart.jschart + '\n'
    return mark_safe(html_string)


@register.simple_tag(name='include_nvd3jscss')
def include_nvd3jscss():
    """
    Include the javascript and css for nvd3
    This include :
        * d3.v2.js
        * nv.d3.js
        * nv.d3.css
    """
    chart = NVD3Chart()
    chart.buildhtmlheader()
    return mark_safe(chart.htmlheader + '\n')


@register.simple_tag(name='include_container')
def include_container(include_container, height=400, width=600):
    """
    Include the html for the chart container and css for nvd3
    This will include something similar as :
        <div id="containername"><svg style="height:400px;width:600px;"></svg></div>
    """
    chart = NVD3Chart()
    chart.buildhtmlheader()
    return mark_safe(chart.htmlheader + '\n')


# Template usage
# {% get_current_time "%Y-%m-%d %I:%M %p" as the_time %}
# <p>The time is {{ the_time }}.</p>
# @register.assignment_tag(name='get_current_time')
# def get_current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)
