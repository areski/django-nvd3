
.. _cumulativeLineChart-model:

cumulativeLineChart
-------------------

A cumulative line chart is used when you have one important grouping representing
an ordered set of data and one value to show, summed over time.

.. image:: ../_static/screenshot/cumulativeLineChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_cumulativelinechart(request):
        """
        cumulativelinechart page
        """
        start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
        nb_element = 100
        xdata = range(nb_element)
        xdata = map(lambda x: start_time + x * 1000000000, xdata)
        ydata = [i + random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)

        extra_serie1 = {"tooltip": {"y_start": "", "y_end": " calls"}}
        extra_serie2 = {"tooltip": {"y_start": "", "y_end": " min"}}

        chartdata = {
            'x': xdata,
            'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1,
            'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
        }

        charttype = "cumulativeLineChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata,
        }
        return render_to_response('cumulativelinechart.html', data)


Template example::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart charttype chartdata "cumulativelinechart_container" True %}
    </head>
    <body>
        {% include_container "cumulativelinechart_container" 400 600 %}
    </body>
