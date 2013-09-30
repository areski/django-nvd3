
.. _multiBarChart-model:

multiBarChart
-------------

A multiple bar graph contains comparisons of two or more categories or bars.
One axis represents a quantity and the other axis identifies a specific feature
about the categories. Reading a multiple bar graph includes looking at extremes
(tallest/longest vs. shortest) in each grouping.

.. image:: ../_static/screenshot/multiBarChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_multibarchart(request):
        """
        multibarchart page
        """
        nb_element = 10
        xdata = range(nb_element)
        ydata = [random.randint(1, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)
        ydata3 = map(lambda x: x * 3, ydata)
        ydata4 = map(lambda x: x * 4, ydata)

        extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}

        chartdata = {
            'x': xdata,
            'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
            'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
            'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
            'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
        }

        charttype = "multiBarChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }
        return render_to_response('multibarchart.html', data)

Template example::

    {% load static %}
    <link media="all" href="{% static 'nvd3/src/nv.d3.css' %}" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src='{% static 'd3/d3.min.js' %}'></script>
    <script type="text/javascript" src='{% static 'nvd3/nv.d3.min.js' %}'></script>

    {% load nvd3_tags %}
    <head>
        {% load_chart charttype chartdata "multibarchart_container" %}
    </head>
    <body>
        {% include_container "multibarchart_container" 400 600 %}
    </body>
