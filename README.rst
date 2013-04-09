Django wrapper for nvd3 - Create beautiful charts effortlessly
==============================================================

:Description: Django-nvd3 is a wrapper for NVD3 graph library
:nvd3: NVD3 http://nvd3.org/
:d3: Data-Driven Documents http://d3js.org/


NVD3 is an attempt to build re-usable charts and chart components
for d3.js without taking away the power that d3.js gives you.


Installation
------------

Install, upgrade and uninstall django-nvd3.py with these commands::

    $ sudo pip install django-nvd3
    $ sudo pip install --upgrade django-nvd3
    $ sudo pip uninstall django-nvd3


How to Create Charts
---------------------

Here is a short example of how to create a lineWithFocusChart. Let’s say we have a simple model with the following fields:

...[describe model]


...[show some view code]


And you can use the ``load_nvd3`` filter in the django template to render the chart. ::

  <head>
      <!-- code to include the NVD3 and D3 libraries goes here -->
      <!-- load_nvd3 filter takes a comma-separated list of id's where -->
      <!-- the charts need to be rendered to                             -->
      {% load nvd3_graph %}
      {{ chartname|load_charts:"container" }}
  </head>
  <body>
      <div id='container'> Chart will be rendered here </div>
  </body>

...[show template code]


See the sample_project for an example of django-nvd3 usage.


Screenshot
----------

.. image:: https://raw.github.com/areski/django-nvd3/master/screenshot/screenshot-01.png


Demo
----

See a live demo on jsfiddle : http://jsfiddle.net/4KuSx/


Supported graph
---------------

Currently implemented nvd3 chart:

* lineWithFocusChart
* lineChart
* multiBarChart
* pieChart
* stackedAreaChart


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
