from django.template.defaultfilters import register
from django.utils.safestring import mark_safe
from django.conf import settings
from nvd3.NVD3Chart import NVD3Chart
from nvd3 import lineWithFocusChart, lineChart, \
    multiBarChart, pieChart, stackedAreaChart, \
    multiBarHorizontalChart, linePlusBarChart, \
    cumulativeLineChart, discreteBarChart, scatterChart, linePlusBarWithFocusChart


@register.simple_tag
def load_chart(chart_type, series, container, kw_extra, *args, **kwargs):
    """Loads the Chart objects in the container.

    **usage**:

        {% load_chart "lineWithFocusChart" data_set "div_lineWithFocusChart" %}

    **Arguments**:

        * ``chart_type`` - Give chart type name eg. lineWithFocusChart/pieChart
        * ``series`` - Data set which are going to be plotted in chart.
        * ``container`` - Chart holder in html page.

    **kw_extra settings**::
        * ``x_is_date`` - if enabled the x-axis will be display as date format
        * ``x_axis_format`` - set the x-axis date format, ie. "%d %b %Y"
        * ``tag_script_js`` - if enabled it will add the javascript tag '<script>'
        * ``jquery_on_ready`` - if enabled it will load the javascript only when page is loaded
            this will use jquery library, so make sure to add jquery to the template.
        * ``color_category`` - Define color category (eg. category10, category20, category20c)
    """
    if not chart_type:
        return False

    if not 'x_is_date' in kw_extra:
        kw_extra['x_is_date'] = False
    if not 'x_axis_format' in kw_extra:
        kw_extra['x_axis_format'] = "%d %b %Y"
    if not 'color_category' in kw_extra:
        kw_extra['color_category'] = "category20"
    if not 'tag_script_js' in kw_extra:
        kw_extra['tag_script_js'] = True
    # set the container name
    kw_extra['name'] = container

    # Build chart
    chart = eval(chart_type)(**kw_extra)

    xdata = series['x']
    y_axis_list = [d for d in series.keys() if 'y' in d]
    y_axis_list.sort()

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


@register.simple_tag
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
    chart = NVD3Chart()
    chart.name = include_container
    chart.set_graph_height(height)
    chart.set_graph_width(width)
    chart.buildcontainer()

    return mark_safe(chart.container + '\n')


@register.simple_tag
def include_chart_jscss(static_dir=''):
    """
    Include the html for the chart container and css for nvd3
    This will include something similar as :

        <link media="all" href="/static/nvd3/src/nv.d3.css" type="text/css" rel="stylesheet" />
        <script src="/static/d3/d3.min.js" type="text/javascript"></script>
        <script src="/static/nvd3/nv.d3.min.js" type="text/javascript"></script>

    **usage**:

        {% include_chart_jscss 'newfies' %}

    **Arguments**:

        * ``static_dir`` -
    """
    if static_dir:
        static_dir += '/'

    chart = NVD3Chart()
    chart.header_css = [
        '<link media="all" href="%s" type="text/css" rel="stylesheet" />\n' % h for h in
        (
            "%s%snvd3/src/nv.d3.css" % (settings.STATIC_URL, static_dir),
        )
    ]

    chart.header_js = [
        '<script src="%s" type="text/javascript"></script>\n' % h for h in
        (
            "%s%sd3/d3.min.js" % (settings.STATIC_URL, static_dir),
            "%s%snvd3/nv.d3.min.js" % (settings.STATIC_URL, static_dir)
        )
    ]
    chart.buildhtmlheader()
    return mark_safe(chart.htmlheader + '\n')
