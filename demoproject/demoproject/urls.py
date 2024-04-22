from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('piechart/', views.demo_piechart, name='demo_piechart'),
    path('linechart/', views.demo_linechart, name='demo_linechart'),
    path('linechart_without_date/', views.demo_linechart_without_date, name='demo_linechart_without_date'),
    path('linewithfocuschart/', views.demo_linewithfocuschart, name='demo_linewithfocuschart'),
    path('multibarchart/', views.demo_multibarchart, name='demo_multibarchart'),
    path('stackedareachart/', views.demo_stackedareachart, name='demo_stackedareachart'),
    path('multibarhorizontalchart/', views.demo_multibarhorizontalchart, name='demo_multibarhorizontalchart'),
    path('lineplusbarchart/', views.demo_lineplusbarchart, name='demo_lineplusbarchart'),
    path('cumulativelinechart/', views.demo_cumulativelinechart, name='demo_cumulativelinechart'),
    path('discretebarchart/', views.demo_discretebarchart, name='demo_discretebarchart'),
    path('discretebarchart_with_date/', views.demo_discretebarchart_with_date, name='demo_discretebarchart_date'),
    path('scatterchart/', views.demo_scatterchart, name='demo_scatterchart'),
    path('linechart_with_ampm/', views.demo_linechart_with_ampm, name='demo_linechart_with_ampm'),
    # path('^demoproject/', include('demoproject.foo.urls')),
]
