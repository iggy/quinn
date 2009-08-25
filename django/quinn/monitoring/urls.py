from django.conf.urls.defaults import *

urlpatterns = patterns('monitoring.views',
    (r'host/(?P<hostid>\d+)', 'host'),
    (r'racks/', 'racks'),
    (r'newrack/', 'newrack'),
    (r'rack/(?P<rid>\d+)', 'rack'),
    (r'', 'index'),
)