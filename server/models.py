# django init stuff, after this we should be able to access django models 
# for whatever info we need

#import sys, os.path

# FIXME hackish, won't be required when we start installing to the system
#sys.path.append(os.path.abspath('../django/'))

from django.core.management import setup_environ
import quinn.django.quinn.settings
setup_environ(quinn.django.quinn.settings)

# from quinn.models import scannets, etc.
#from quinn.django.quinn.monitoring.models import Host
#from quinn.django.quinn.virt.models import KSMStat

# FIXME also hackish
#sys.path.append(os.path.abspath('../SRPSocket/'))
from quinn.server.SRPSocket import SRPSocket
