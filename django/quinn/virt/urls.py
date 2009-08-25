from django.conf.urls.defaults import *

urlpatterns = patterns('virt.views',
    (r'', 'index'),
)

    #(r'host/(?P<hostid>\d+)', 'host'),
    #(r'racks/', 'racks'),
    #(r'rack/', 'rack'),
