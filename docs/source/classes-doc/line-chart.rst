
.. _lineChart-model:

lineChart
---------

A line chart or line graph is a type of chart which displays information
as a series of data points connected by straight line segments.

.. image:: ../_static/screenshot/lineChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_linechart(request):
        """
        lineChart page
        """
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: start_time + x * 1000000000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)

        extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
        chartdata = {'x': xdata,
                     'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
                     'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}
        charttype = "lineChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }
        return render_to_response('linechart.html', data)


Template example::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart charttype chartdata "linechart_container" True %}
    </head>
    <body>
        {% include_container "linechart_container" 400 600 %}
    </body>
