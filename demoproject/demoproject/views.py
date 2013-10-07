# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
#from django.template.context import RequestContext
import random
import datetime
import time


def home(request):
    """
    home page
    """
    return render_to_response('home.html')


def demo_piechart(request):
    """
    pieChart page
    """
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]

    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata, 'y1': ydata, 'extra1': extra_serie}
    charttype = "pieChart"

    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('piechart.html', data)


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

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"},
                   "date_format": tooltip_date}
    chartdata = {'x': xdata,
                 'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
                 'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}

    charttype = "lineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'date_tag': True,
    }
    return render_to_response('linechart.html', data)


def demo_linechart_without_date(request):
    """
    lineChart page
    """
    extra_serie = {}
    xdata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ydata = [3, 5, 7, 8, 3, 5, 3, 5, 7, 6, 3, 1]
    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
    }
    charttype = "lineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'date_tag': False,
    }
    return render_to_response('linechart.html', data)


def demo_linewithfocuschart(request):
    """
    linewithfocuschart page
    """
    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
    }
    charttype = "lineWithFocusChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('linewithfocuschart.html', data)


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

    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    date_chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "multiBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'date_chartdata': date_chartdata,
    }
    return render_to_response('multibarchart.html', data)


def demo_stackedareachart(request):
    """
    stackedareachart page
    """
    nb_element = 100
    xdata = range(nb_element)
    xdata = map(lambda x: 100 + x, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}
    extra_serie2 = {"tooltip": {"y_start": "", "y_end": " calls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
    }
    charttype = "stackedAreaChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('stackedareachart.html', data)


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


def demo_lineplusbarchart(request):
    """
    lineplusbarchart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 100
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = [i + random.randint(1, 10) for i in reversed(range(nb_element))]
    kwargs1 = {}
    kwargs1['bar'] = True

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {"tooltip": {"y_start": "$ ", "y_end": ""},
                    "date_format": tooltip_date}
    extra_serie2 = {"tooltip": {"y_start": "", "y_end": " min"},
                    "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1, 'kwargs1': kwargs1,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
    }

    charttype = "linePlusBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('lineplusbarchart.html', data)


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

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " calls"},
                    "date_format": tooltip_date}
    extra_serie2 = {"tooltip": {"y_start": "", "y_end": " min"},
                    "date_format": tooltip_date}

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


def demo_discretebarchart_with_date(request):
    """
    discretebarchart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 10

    xdata = list(range(nb_element))
    xdata = [start_time + x * 1000000000 for x in xdata]
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {
        'x': xdata, 'name1': '', 'y1': ydata, 'extra1': extra_serie1,
    }
    charttype = "discreteBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('discretebarchart_with_date.html', data)


def demo_scatterchart(request):
    """
    scatterchart page
    """
    nb_element = 50
    xdata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata1 = [i * random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata1)
    ydata3 = map(lambda x: x * 5, ydata1)

    kwargs1 = {'shape': 'circle'}
    kwargs2 = {'shape': 'cross'}
    kwargs3 = {'shape': 'triangle-up'}

    extra_serie1 = {"tooltip": {"y_start": "", "y_end": " balls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata1, 'kwargs1': kwargs1, 'extra1': extra_serie1,
        'name2': 'series 2', 'y2': ydata2, 'kwargs2': kwargs2, 'extra2': extra_serie1,
        'name3': 'series 3', 'y3': ydata3, 'kwargs3': kwargs3, 'extra3': extra_serie1
    }
    charttype = "scatterChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('scatterchart.html', data)


def demo_linechart_with_ampm(request):
    """
    lineChart page
    """
    xdata = []
    ydata = []
    ydata2 = []

    ydata = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 4, 3, 3, 5, 7, 5, 3, 16, 6, 9, 15, 4, 12]
    ydata2 = [9, 8, 11, 8, 3, 7, 10, 8, 6, 6, 9, 6, 5, 4, 3, 10, 0, 6, 3, 1, 0, 0, 0, 1]

    for i in range(0, 24):
        xdata.append(i)

    #tooltip_date = ""  # "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
    chartdata = {'x': xdata,
                 'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
                 'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie}
    charttype = "lineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('linechart_with_ampm.html', data)


def demo_lineplusbarwithfocuschart(request):
    """
    lineplusbarwithfocuschart page
    """
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    nb_element = 100

    xdata = list(range(nb_element))
    xdata = [start_time + x * 1000000000 for x in xdata]
    ydata = [i + random.randint(-10, 10) for i in range(nb_element)]
    ydata2 = [200 - i + random.randint(-10, 10) for i in range(nb_element)]

    kwargs1 = {}
    kwargs1['bar'] = True

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie1 = {"tooltip": {"y_start": "$ ", "y_end": ""},
                    "date_format": tooltip_date}
    extra_serie2 = {"tooltip": {"y_start": "", "y_end": " min"},
                    "date_format": tooltip_date}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie1, 'kwargs1': kwargs1,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie2,
    }

    charttype = "linePlusBarWithFocusChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
    }
    return render_to_response('lineplusbarwithfocuschart.html', data)
