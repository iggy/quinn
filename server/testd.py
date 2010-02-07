#!/usr/bin/python
# -*- coding: utf-8 -*-

# test

import socket, sys, os
try:
    import dbus, gobject, avahi
except ImportError:
    print "You need the python-avahi, avahi-daemon, python-gobject, and python-dbus packages (and their deps) installed"
    sys.exit(1)
from dbus import DBusException
from dbus.mainloop.glib import DBusGMainLoop
#sys.path.append(os.path.abspath('../../')) # FIXME remove when we start installing in the system

#from quinn.server.SRPSocket.SRPSocket import SRPSocket
#from quinn.server import config
#from quinn.server import qsrvutils
import quinn.server.plugins

# django init stuff
# FIXME hackish, won't be required when we start installing to the system
#sys.path.append(os.path.abspath('../django/'))

#from django.core.management import setup_environ
#import quinn.settings
#setup_environ(quinn.settings)

os.environ['DJANGO_SETTINGS_MODULE'] = 'quinn.django.quinn.settings'
from django.core.management import setup_environ
import quinn.django.quinn.settings as settings
setup_environ(settings)

DBusGMainLoop(set_as_default=True)

main_loop = gobject.MainLoop()
plugins = {}

for arg in sys.argv[1:]:
    name = 'quinn.server.plugins.%s' % (arg,)
    __import__(name)
    mod = sys.modules[name]
    print mod, dir(mod)
    plug = "%s.%sPlugin" % (name, arg.capitalize())
    #print 'dir:', dir(quinn.server.plugins.master)
    #plugins[arg] = eval(plug)
    plug = getattr(mod, arg.capitalize()+'Plugin')
    plug()

print plugins

try:
    main_loop.run()
except KeyboardInterrupt:
    pass

# FIXME handle exits for the plugins I guess
#if not config.asGroup is None:
    #config.asGroup.Free()

