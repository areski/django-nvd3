.. :changelog:

History
-------


0.9.1 (2015-10-12)
------------------

* Add changelog to Manifest


0.9.0 (2015-10-12)
------------------

* add charset to js script tag


0.8.2 (2015-04-06)
------------------

* bump python-nvd3==0.13.7


0.8.1 (2015-04-06)
------------------

* fix error linePlusBarWithFocusChart


0.8.0 (2015-04-06)
------------------

* add support for nvd3 version 1.7.1
* bump requirement python-nvd3==0.13.6
* remove lineplusbarwithfocuschart


0.7.8 (2015-03-09)
------------------

* python3 * replace 'unicode' with 'str'


0.6.1 (2013-12-05)
------------------

* fix y-series not sorted alphabetically thanks @miquelcamprodon


0.6.0 (2013-10-31)
------------------

* fixes on demo project to include js tag in html
* update on simple_tag to work with Django 1.3


0.5.0 (2013-10-09)
------------------

* change settings behavior, now it works with a global extra settings passed as kwargs
* refactoring


0.4.1 (2013-10-04)
------------------

* discreteBarChart support date on xAxis


0.4.0 (2013-10-03)
------------------

* Support new chart linePlusBarWithFocusChart


0.3.1 (2013-09-30)
------------------

* Documentation / Readme update


0.3.0 (2013-09-30)
------------------

* Use Bower to install D3 and NVD3


0.2.0 (2013-09-20)
------------------

* Enable resize by default


0.1.12 (2013-07-09)
-------------------

* Generalise the axis_formatting


0.1.11 (2013-05-30)
-------------------

* Python3 Fix for setup.py TypeError (by DanMeakin)


0.1.10 (2013-05-30)
-------------------

* Add example for multichart with Date + test


0.1.9 (2013-04-06)
------------------

* Make sure we got something in chartype parameter / help the test


0.1.8 (2013-04-25)
------------------

* Option to use cdn or use local file for the JS and CSS


0.1.7 (2013-04-24)
------------------

* Add custom dateformat for tooltip : ``x_axis_date_format`` * display x-axis date in various format ie "%d %b %Y"


0.1.6 (2013-04-23)
------------------

* Add color_category : Define color category (eg. category10, category20, category20c)


0.1.5 (2013-04-23)
------------------

* Fix set height and width useset_graph_height and set_graph_width


0.1.4 (2013-04-23)
------------------

* Add tag_script_js : disable javascript <script> tag


0.1.2 (2013-04-22)
------------------

* Change dependencies to python-nvd3 to version 0.3 instead of 0.3.3


0.1.1 (2013-04-22)
------------------

* Change dependencies to python-nvd3 version * fix lineChart tooltip


0.1 (2013-04-12)
----------------

* Proper project release including support for the following chart::

    lineWithFocusChart
    lineChart
    multiBarChart
    pieChart
    stackedAreaChart
    multiBarHorizontalChart
    linePlusBarChart
    cumulativeLineChart
    discreteBarChart
    scatterChart


0.0.1 (2013-04-09)
------------------

* First release
