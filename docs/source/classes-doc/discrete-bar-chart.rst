
.. _discreteBarChart-model:

discreteBarChart
----------------

A discrete bar chart or bar graph is a chart with rectangular bars with
lengths proportional to the values that they represent.

.. image:: ../_static/screenshot/discreteBarChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_discretebarchart(request):
    """
    discretebarchart page
    """
    xdata = ["A", "B", "C", "D", "E", "F", "G"]
    ydata = [3, 12, -10, 5, 35, -7, 2]

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {
        'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
    }
    charttype = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('discretebarchart.html', data)


Template example::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart charttype chartdata "discretebarchart_container" %}
    </head>
    <body>
        {% include_container "discretebarchart_container" 400 600 %}
    </body>
