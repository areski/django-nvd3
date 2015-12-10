from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^piechart/', views.demo_piechart, name='demo_piechart'),
    url(r'^linechart/', views.demo_linechart, name='demo_linechart'),
    url(r'^linechart_without_date/', views.demo_linechart_without_date, name='demo_linechart_without_date'),
    url(r'^linewithfocuschart/', views.demo_linewithfocuschart, name='demo_linewithfocuschart'),
    url(r'^multibarchart/', views.demo_multibarchart, name='demo_multibarchart'),
    url(r'^stackedareachart/', views.demo_stackedareachart, name='demo_stackedareachart'),
    url(r'^multibarhorizontalchart/', views.demo_multibarhorizontalchart, name='demo_multibarhorizontalchart'),
    url(r'^lineplusbarchart/', views.demo_lineplusbarchart, name='demo_lineplusbarchart'),
    url(r'^cumulativelinechart/', views.demo_cumulativelinechart, name='demo_cumulativelinechart'),
    url(r'^discretebarchart/', views.demo_discretebarchart, name='demo_discretebarchart'),
    url(r'^discretebarchart_with_date/', views.demo_discretebarchart_with_date, name='demo_discretebarchart_date'),
    url(r'^scatterchart/', views.demo_scatterchart, name='demo_scatterchart'),
    url(r'^linechart_with_ampm/', views.demo_linechart_with_ampm, name='demo_linechart_with_ampm'),
    # url(r'^demoproject/', include('demoproject.foo.urls')),
]
