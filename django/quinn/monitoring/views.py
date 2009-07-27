from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from quinn.monitoring.models import *

# Create your views here.

@login_required
def action(request):
    '''do something... used often by ajax functions'''
    return HttpResponse('foo')

@login_required
def index(request):
    '''view the network... sort of an overview of everything we know'''
    numhosts = len(Host.objects.all())
    nummon = 0
    numagents = 0
    racks = Rack.objects.all()
    return direct_to_template(request, 'monitoring/index.html', locals())
    
    
@login_required
def rack(request):
    '''view a specific rack's contents or create a new one'''
    if "which_rack" in request.GET:
        # show them a specific rack
        pass
    else:
        # show a new empty rack
        pass
    return HttpResponse('foo')

@login_required
def racks(request):
    '''view racks and their contents'''
    racks = Rack.objects.all()
    useq = range(0,42)
    return direct_to_template(request, 'monitoring/racks.html', locals())

@login_required
def host(request, hostid):
    '''view an individual host's details'''
    host = Host.objects.get(id=hostid)
    return direct_to_template(request, 'monitoring/host.html', locals())
    
