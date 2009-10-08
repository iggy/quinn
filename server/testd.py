#!/usr/bin/python

# test

import socket
import dbus, gobject, avahi
from dbus import DBusException
from dbus.mainloop.glib import DBusGMainLoop
from SRPSocket.SRPSocket import SRPSocket


import config

DBusGMainLoop(set_as_default=True)

config.main_loop = gobject.MainLoop()
config.bus = dbus.SystemBus()

config.server = dbus.Interface(
    config.bus.get_object(avahi.DBUS_NAME, avahi.DBUS_PATH_SERVER), 
    avahi.DBUS_INTERFACE_SERVER)

import qsrvutils

if socket.gethostname() == config.masterName:
    print "Starting up as master"
    
    if config.asPort is None:
        config.asPort = qsrvutils.find_open_port()

    config.server.connect_to_signal('StateChange', qsrvutils.server_state_changed)
    qsrvutils.server_state_changed(config.server.GetState())
    
    qsrvutils.server_init()
    
else:
    print "connecting to master"
    config.client = dbus.Interface(
        config.bus.get_object(
            avahi.DBUS_NAME,
            config.server.ServiceBrowserNew(
                avahi.IF_UNSPEC,
                avahi.PROTO_UNSPEC,
                config.asType,
                config.asDomain,
                dbus.UInt32(0))),
            avahi.DBUS_INTERFACE_SERVICE_BROWSER)

    config.client.connect_to_signal('ItemNew', qsrvutils.found_new_service)

try:
    config.main_loop.run()
except KeyboardInterrupt:
    pass

if not config.asGroup is None:
    config.asGroup.Free()

