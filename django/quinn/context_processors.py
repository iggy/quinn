from quinn.monitoring.models import Rack

def menu_contents(request):
    '''Add what we need for the menu to RequestContext'''
    racks = Rack.objects.all()
    return {'menuracks':racks}