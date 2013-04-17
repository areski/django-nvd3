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
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
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

    chartdata = {'x': xdata, 'y1': ydata, 'y2': ydata2}
    charttype = "lineChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
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

    chartdata = {'x': xdata, 'y1': ydata, 'y2': ydata2, 'y3': ydata3, 'y4': ydata4}
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

    chartdata = {'x': xdata, 'y1': ydata, 'y2': ydata2, 'y3': ydata3, 'y4': ydata4}
    charttype = "multiBarChart"
    data = {
        'charttype': charttype,
        'chartdata': chartdata
    }
    return render_to_response('multibarchart.html', data)