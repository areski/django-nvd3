
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

    {% load static %}
    <link media="all" href="{% static 'nvd3/src/nv.d3.css' %}" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src='{% static 'd3/d3.min.js' %}'></script>
    <script type="text/javascript" src='{% static 'nvd3/nv.d3.min.js' %}'></script>

    {% load nvd3_tags %}
    <head>
        {% load_chart charttype chartdata "discretebarchart_container" %}
    </head>
    <body>
        {% include_container "discretebarchart_container" 400 600 %}
    </body>
