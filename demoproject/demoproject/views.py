from django.shortcuts import render_to_response
#from django.template.context import RequestContext


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
    data = {
        'test': 1,
        'chartdata': chartdata
    }
    return render_to_response('piechart.html', data)


def demo_linechart(request):
    """
    lineChart page
    """
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]
    chartdata = {'x': xdata, 'y': ydata}
    data = {
        'test': 1,
        'chartdata': chartdata
    }
    return render_to_response('piechart.html', data)


# type = "lineChart"
# chart = lineChart(name=type, date=True, height=350)
# chart.set_containerheader("\n\n<h2>" + type + "</h2>\n\n")

# start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)

# nb_element = 100
# xdata = range(nb_element)
# xdata = map(lambda x: start_time + x * 1000000000, xdata)
# ydata = [i + random.randint(1, 10) for i in range(nb_element)]
# ydata2 = map(lambda x: x * 2, ydata)

# chart.add_serie(y=ydata, x=xdata)
# chart.add_serie(y=ydata2, x=xdata)