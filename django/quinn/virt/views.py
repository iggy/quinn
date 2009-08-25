# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template



@login_required
def index(request):
    '''dunno just yet'''
    return direct_to_template(request, 'virt/index.html', locals())