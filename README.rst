Django Wrapper for NVD3 - It's time for beautiful charts
========================================================

:Description: Django-nvd3 is a wrapper for NVD3 graph library
:nvd3: NVD3 http://nvd3.org/
:d3: Data-Driven Documents http://d3js.org/


NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.


.. image:: https://www.travis-ci.org/areski/django-nvd3.png?branch=master

|endorse|

.. |endorse| image:: https://api.coderwall.com/areski/endorsecount.png
    :target: https://coderwall.com/areski


Installation
------------

Install, upgrade and uninstall django-nvd3 with these commands::

    $ pip install django-nvd3
    $ pip install --upgrade django-nvd3
    $ pip uninstall django-nvd3


Dependencies
------------

Django-nvd3 have one major dependencie:

* python-nvd3 : https://github.com/areski/python-nvd3


Example how to create a pieChart
--------------------------------

Let’s say we have a simple view in which we want to display the amount of calories per fruit.

So to achieve this, we will edit our view.py, we will prepare the data that will be displayed::

    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('piechart.html', data)


We pass charttype and chartdata to use them in our template later.

Our template piechart.html could look like::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart charttype chartdata "piechart_container" "400" "600" %}
    </head>
    <body>
        <h1>Fruits vs Calories</h1>
        <div id="piechart_container"><svg style="height:400px;width:600px;"></svg></div>
    </body>

As showed above we use include_nvd3jscss to include the needed javascript and css code for NVD3.
We start preparing and display the javascript code needed to render our pieChart::

    {% load_chart charttype chartdata "piechart_container" "400" "600" %}

Finally we created a div container which will be used to display the chart.


The result will be a beautiful and interactive chart:

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/piechart_fruits_vs_calories.png


More examples, please look at the demoproject directory in our repository, it shows an simple example for all the supported
chart by django-nvd3.


Demo
----

See a live demo on jsfiddle : http://jsfiddle.net/4KuSx/


Supported nvd3 charts
---------------------

Charts list:

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/lineWithFocusChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/lineChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/multiBarChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/pieChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/stackedAreaChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/multiBarHorizontalChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/linePlusBarChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/cumulativeLineChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/discreteBarChart.png

.. image:: https://raw.github.com/areski/django-nvd3/master/docs/source/_static/screenshot/scatterChart.png


Projects using Django-nvd3
--------------------------

* CDR-Stats : www.cdr-stats.org
* Newfies-Dialer : www.newfies-dialer.org


Documentation
-------------

Documentation is available on 'Read the Docs':
http://django-nvd3.readthedocs.org


License
-------

Django-nvd3 is licensed under MIT, see `MIT-LICENSE.txt`.
