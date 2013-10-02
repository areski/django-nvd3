from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from django.conf import settings
from nvd3.NVD3Chart import NVD3Chart
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart, linePlusBarWithFocusChart


@register.simple_tag(name='load_chart')
def load_chart(chart_type, series, container, x_is_date=False, x_axis_format="%d %b %Y", tag_script_js=True, color_category='category20', *args, **kwargs):
    """Loads the Chart objects in the container.

    **usage**:

        {% load_chart "lineWithFocusChart" data_set "div_lineWithFocusChart" %}

    **Arguments**:

        * ``chart_type`` - Give chart type name eg. lineWithFocusChart/pieChart
        * ``series`` - Data set which are going to be plotted in chart.
        * ``container`` - Chart holder in html page.
        * ``x_is_date`` - if x-axis is in date format
        * ``x_axis_format`` - display x-axis date in various format ie "%d %b %Y"
        * ``tag_script_js`` - if show the javascript tag <script>
        * ``color_category`` - Define color category (eg. category10, category20, category20c)
    """
    if not chart_type:
        return False
    chart = eval(chart_type)(name=container, date=x_is_date, x_axis_format=x_axis_format, color_category=color_category, resize=True, *args, **kwargs)
    #don't show the javascript tag <script>
    if not tag_script_js:
        chart.tag_script_js = False
    xdata = series['x']
    y_axis_list = [d for d in series.keys() if 'y' in d]

    for key in y_axis_list:
        ydata = series[key]
        axis_no = key.split('y')[1]

        name = series['name' + axis_no] if series.get('name' + axis_no) else None
        extra = series['extra' + axis_no] if series.get('extra' + axis_no) else {}

        if chart_type == 'linePlusBarChart' or chart_type == 'linePlusBarWithFocusChart':
            if key == 'y1':
                kwargs = series['kwargs1']
                chart.add_serie(name=name, y=ydata, x=xdata, extra=extra, **kwargs)
            else:
                chart.add_serie(name=name, y=ydata, x=xdata, extra=extra)
        elif chart_type == 'scatterChart':
            # get digit
            kwargs = series['kwargs' + axis_no]
            chart.add_serie(name=name, y=ydata, x=xdata, extra=extra, **kwargs)
        elif chart_type == 'pieChart':
            chart.add_serie(y=ydata, x=xdata, extra=extra)
        else:
            chart.add_serie(name=name, y=ydata, x=xdata, extra=extra)

    chart.buildhtml()

    html_string = chart.jschart + '\n'
    return mark_safe(html_string)


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
    chart.set_graph_height(height)
    chart.set_graph_width(width)
    chart.buildcontainer()

    return mark_safe(chart.container + '\n')


@register.simple_tag(name='include_chart_jscss')
def include_chart_jscss():
    """
    Include the html for the chart container and css for nvd3
    This will include something similar as :

        <link media="all" href="/static/nvd3/src/nv.d3.css" type="text/css" rel="stylesheet" />
        <script src="/static/d3/d3.min.js" type="text/javascript"></script>
        <script src="/static/nvd3/nv.d3.min.js" type="text/javascript"></script>

    **usage**:

        {% include_chart_jscss %}
    """
    chart = NVD3Chart()
    chart.header_css = [
        '<link media="all" href="%s" type="text/css" rel="stylesheet" />\n' % h for h in
        (
            settings.STATIC_URL + "nvd3/src/nv.d3.css",
        )
    ]

    chart.header_js = [
        '<script src="%s" type="text/javascript"></script>\n' % h for h in
        (
            settings.STATIC_URL + "d3/d3.min.js",
            settings.STATIC_URL + "nvd3/nv.d3.min.js"
        )
    ]
    chart.buildhtmlheader()
    return mark_safe(chart.htmlheader + '\n')
