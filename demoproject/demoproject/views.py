from django.shortcuts import render_to_response, redirect


def home(request):
    """
    Home page
    """
    return render_to_response('home.html',
                              {'test': 1})
