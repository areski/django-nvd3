
.. _stackedAreaChart-model:

stackedAreaChart
----------------

The stacked area chart is identical to the area chart, except the areas are stacked
on top of each other, rather than overlapping. This can make the chart much easier to read.

.. image:: ../_static/screenshot/stackedAreaChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_stackedareachart(request):
        """
        stackedareachart page
        """
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: 100 + x, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)

        extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}
        extra_serie2 = {"tooltip": {"y_start": "", "y_end": " calls"}}

        chartdata = {
            'x': xdata,
            'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1,
            'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
        }
        charttype = "stackedAreaChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }
        return render_to_response('stackedareachart.html', data)

Template example::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart charttype chartdata "stackedareachart_container" %}
    </head>
    <body>
        {% include_container "stackedareachart_container" 400 600 %}
    </body>
