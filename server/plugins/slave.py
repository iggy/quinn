# -*- coding: utf-8 -*-
import dbus, gobject, avahi, socket, anyjson
from quinn.server.plugins import QuinnPlugin

class SlavePlugin(QuinnPlugin):
    def __init__(self):
        self.asType = "_quinn._tcp"
        self.asDomain = "local"
        self.mstr_sock = None

        print "init SlavePlugin"

        self.bus = dbus.SystemBus()
        self.server = dbus.Interface(
            self.bus.get_object(avahi.DBUS_NAME, avahi.DBUS_PATH_SERVER),
            avahi.DBUS_INTERFACE_SERVER)
        self.browser = dbus.Interface(
            self.bus.get_object(
                avahi.DBUS_NAME,
                self.server.ServiceBrowserNew(
                    avahi.IF_UNSPEC,
                    avahi.PROTO_UNSPEC,
                    self.asType,
                    self.asDomain,
                    dbus.UInt32(0))),
            avahi.DBUS_INTERFACE_SERVICE_BROWSER)

        self.browser.connect_to_signal('ItemNew', self.found_new_service)


    def service_resolved(self, *args):
        """callback run by found_new_service() when a master is found on
        the network
        """
        print 'service resolved'
        print 'name:', args[2]
        print 'address:', args[7]
        print 'port:', args[8]

        try:
            import time
            self.mstr_sock = socket.socket()
            self.mstr_sock.connect((args[7], args[8]))
            d = {
                'init':{
                    'plugins':['linux-stats','kvm-host']
                }
            }
            self.mstr_sock.send(anyjson.serialize(d))
            #time.sleep(10)
            #print "Sending extra data"
            #self.mstr_sock.send("{'report':{'plugin':'linux-stats','data':{'diskfree':'123456561432'}}}")
        except Exception, E:
            print "error connecting to master", E
            return

        # load all the plugins

    def print_error(self, *args):
        """callback run by found_new_service() when there is an error"""
        print 'slave plugin: found_new_service error handler'
        print args


    def found_new_service(self, interface, protocol, name, stype, domain, flags):
        """callback run by the avahi main loop when a service is found on the network"""
        #print "Found Service: ", interface, protocol, name, stype, domain, flags

        #if flags & avahi.LOOKUP_RESULT_LOCAL:
            # local service, skip
            #print "Skipping local service"
            #return

        # FIXME should this be self.browser ?
        self.server.ResolveService(interface, protocol, name, stype,
            domain, avahi.PROTO_UNSPEC, dbus.UInt32(0),
            reply_handler=self.service_resolved, error_handler=self.print_error)
