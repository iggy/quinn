# -*- coding: utf-8 -*-
import dbus, gobject, socket
from quinn.server.plugins import QuinnPlugin
from quinn.server.models import *

from quinn.django.quinn.virt.models import KSMStat

class KvmhostPlugin(QuinnPlugin):
    """plugin for admin'ing kvm VMs and getting some info from the hosts"""
    def __init__(self):
        # setup timer to check ksm statistics
        gobject.timeout_add(60000, self.check_ksm_stats)
        
    def check_ksm_stats(self):
        # read the ksm stats from sysfs and record them in the DB
        pass