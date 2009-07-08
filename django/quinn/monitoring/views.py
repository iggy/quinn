from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def action(request):
    '''do something... used often by ajax functions'''
    pass

@login_required
def index(request):
    '''view the network... sort of an overview of everything we know'''
    pass
    
@login_required
def rack(request):
    '''view a specific rack's contents or create a new one'''
    if "which_rack" in request.GET:
        # show them a specific rack
        pass
    else:
        # show a new empty rack
        pass

@login_required
def host(request, hostid):
    '''view an individual host's details'''
    pass
    
