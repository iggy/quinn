from django.conf.urls.defaults import *

urlpatterns = patterns('monitoring.views',
    (r'host/(?P<hostid>\d+)', 'host'),
    (r'rack/', 'rack'),
    (r'', 'index'),
)