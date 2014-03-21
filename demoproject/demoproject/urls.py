from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('demoproject.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^piechart/', 'demo_piechart', name='demo_piechart'),
    url(r'^linechart/', 'demo_linechart', name='demo_linechart'),
    url(r'^linechart_without_date/', 'demo_linechart_without_date', name='demo_linechart_without_date'),
    url(r'^linewithfocuschart/', 'demo_linewithfocuschart', name='demo_linewithfocuschart'),
    url(r'^multibarchart/', 'demo_multibarchart', name='demo_multibarchart'),
    url(r'^stackedareachart/', 'demo_stackedareachart', name='demo_stackedareachart'),
    url(r'^multibarhorizontalchart/', 'demo_multibarhorizontalchart', name='demo_multibarhorizontalchart'),
    url(r'^lineplusbarchart/', 'demo_lineplusbarchart', name='demo_lineplusbarchart'),
    url(r'^cumulativelinechart/', 'demo_cumulativelinechart', name='demo_cumulativelinechart'),
    url(r'^discretebarchart/', 'demo_discretebarchart', name='demo_discretebarchart'),
    url(r'^discretebarchart_with_date/', 'demo_discretebarchart_with_date', name='demo_discretebarchart_date'),
    url(r'^scatterchart/', 'demo_scatterchart', name='demo_scatterchart'),
    url(r'^linechart_with_ampm/', 'demo_linechart_with_ampm', name='demo_linechart_with_ampm'),
    url(r'^lineplusbarwithfocuschart/', 'demo_lineplusbarwithfocuschart', name='demo_lineplusbarwithfocuschart'),
    url(r'^lineplusbarwithfocuschart_without_date/', 'demo_lineplusbarwithfocuschart_without_date', name='demo_lineplusbarwithfocuschart_without_date'),
    # url(r'^demoproject/', include('demoproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
