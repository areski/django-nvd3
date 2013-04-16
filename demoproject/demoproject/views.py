from django.shortcuts import render_to_response
from django.template.context import RequestContext


def home(request):
    """
    Home page
    """
    xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
    ydata = [3, 4, 0, 1, 5, 7, 3]
    chartdata = {'x': xdata, 'y': ydata}
    data = {
        'test': 1,
        'chartdata': chartdata
    }
    return render_to_response('home.html', data,
           context_instance=RequestContext(request))
