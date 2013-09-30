
.. _lineWithFocusChart-model:

lineWithFocusChart
------------------

A lineWithFocusChart or line graph is a type of chart which displays information
as a series of data points connected by straight line segments.
The lineWithFocusChart provide a smaller chart that act as a selector,
this is very useful if you want to zoom on a specific time period.

.. image:: ../_static/screenshot/lineWithFocusChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_linewithfocuschart(request):
        """
        linewithfocuschart page
        """
        nb_element = 100
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

        xdata = range(nb_element)
        xdata = map(lambda x: start_time + x * 1000000000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        ydata3 = map(lambda x: x * 3, ydata)
        ydata4 = map(lambda x: x * 4, ydata)

        tooltip_date = "%d %b %Y %H:%M:%S %p"
        extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                       "date_format": tooltip_date}
        chartdata = {
            'x': xdata,
            'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
            'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
            'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
            'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
        }
        charttype = "lineWithFocusChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }
        return render_to_response('linewithfocuschart.html', data)


Template example::

    {% load static %}
    <link media="all" href="{% static 'nvd3/src/nv.d3.css' %}" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src='{% static 'd3/d3.min.js' %}'></script>
    <script type="text/javascript" src='{% static 'nvd3/nv.d3.min.js' %}'></script>

    {% load nvd3_tags %}
    <head>
        {% load_chart charttype chartdata "linewithfocuschart_container" True "%d %b %Y %H" %}
    </head>
    <body>
        {% include_container "linewithfocuschart_container" 400 '100%' %}
    </body>
