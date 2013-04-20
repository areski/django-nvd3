
.. _multiBarHorizontalChart-model:

multiBarHorizontalChart
-----------------------

A multiple horizontal bar graph contains comparisons of two or more categories or bars.

.. image:: ../_static/screenshot/multiBarHorizontalChart.png

Django example::

    from django.shortcuts import render_to_response
    import random
    import datetime
    import time

    def demo_multibarhorizontalchart(request):
        """
        multibarhorizontalchart page
        """
        nb_element = 10
        xdata = range(nb_element)
        ydata = [i + random.randint(-10, 10) for i in range(nb_element)]
        ydata2 = map(lambda x: x * 2, ydata)

        extra_serie = {"tooltip": {"y_start": "", "y_end": " mins"}}

        chartdata = {
            'x': xdata,
            'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
            'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        }

        charttype = "multiBarHorizontalChart"
        data = {
            'charttype': charttype,
            'chartdata': chartdata
        }
        return render_to_response('multibarhorizontalchart.html', data)

Template example::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart charttype chartdata "multibarhorizontalchart_container" %}
    </head>
    <body>
        {% include_container "multibarhorizontalchart_container" 400 600 %}
    </body>
