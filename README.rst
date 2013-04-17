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

Install, upgrade and uninstall django-nvd3.py with these commands::

    #Install
    $ sudo pip install django-nvd3

    #Upgrade
    $ sudo pip install --upgrade django-nvd3

    #Uninstall
    $ sudo pip uninstall django-nvd3


Or if you don't have `pip`, use easy_install to install django-nvd3::

    $ sudo easy_install django-nvd3


Dependencies
------------

Django-nvd3 have one major dependencie:

* python-nvd3 : https://github.com/areski/python-nvd3


How to Create Charts
---------------------

Here is a short example of how to create a lineWithFocusChart. Let’s say we have a simple model with the following fields:


TODO: ...[show some code for model]


TODO: ...[show some view code]


And you can use the ``nvd3_tags`` filter in the django template to render the chart. ::

::

    {% load nvd3_tags %}
    <head>
        <!-- code to include the NVD3 and D3 libraries goes here -->
        <!-- load_nvd3 filter takes a comma-separated list of id's where -->
        <!-- the charts need to be rendered to                             -->
        {% include_nvd3jscss %}
        {% load_chart "lineWithFocusChart" chartdata "lineWithFocusChart_container" "500" "800" %}
    </head>
    <body>
        <div id="lineWithFocusChart_container"><svg style="height:500px;width:800px;"></svg></div>
    </body>

...[show template code]


See the sample_project for an example of django-nvd3 usage.


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
