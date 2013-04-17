from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from nvd3.NVD3Chart import NVD3Chart
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart


@register.simple_tag(name='load_chart')
def load_chart(chart_type, series, container, height=400, width=400, y_is_date=False):
    """Loads the Chart objects in the container.

    **usage**:

        {% load_chart "lineWithFocusChart" data_set "div_lineWithFocusChart" 400 400 %}

    **Arguments**:

        * ``chart_type`` - Give chart type name eg. lineWithFocusChart/pieChart
        * ``series`` - Data set which are going to be plotted in chart.
        * ``container`` - Chart holder in html page.
        * ``height`` - Chart height
        * ``width`` - Chart width
        * ``y_is_date`` - if x-axis is in date format
    """
    chart = eval(chart_type)(name=container, date=y_is_date, height=height, width=width)
    xdata = series['x']
    y_axis_list = [d for d in series.keys() if 'y' in d]

    for key in y_axis_list:
        ydata = series[key]
        if chart_type == 'linePlusBarChart':
            if key == 'y1':
                kwargs = series['kwargs1']
                chart.add_serie(y=ydata, x=xdata, **kwargs)
            else:
                chart.add_serie(y=ydata, x=xdata)
        elif chart_type == 'scatterChart':
            # get digit
            axis_no = key.split('y')[1]
            kwargs = series['kwargs' + axis_no]
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

    **usage**:

        {% include_container "lineWithFocusChart" 400 400 %}

    **Arguments**:

        * ``include_container`` - container_name
        * ``height`` - Chart height
        * ``width`` - Chart width
    """
    chart = NVD3Chart(include_container)
    chart.height = height
    chart.width = width
    chart.buildcontainer()

    return mark_safe(chart.container + '\n')
