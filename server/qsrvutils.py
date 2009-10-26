# -*- coding: utf-8 -*-

import dbus, gobject, avahi, config, socket



def service_resolved(*args):
    """callback run by found_new_service() when a useable service is found on
    the network
    """
    print 'service resolved'
    print 'name:', args[2]
    print 'address:', args[7]
    print 'port:', args[8]

    if not config.mstr_sock:
        # open up the socket to the master daemon
        print "opening socket to %s:%s" % (args[7], args[8])
        try:
            import time
            config.mstr_sock = socket.socket()
            config.mstr_sock.connect((args[7], args[8]))
            config.mstr_sock.send("{'init':{'plugins':['linux-stats','kvm-host']}}")
            #time.sleep(10)
            #print "Sending extra data"
            #config.mstr_sock.send("{'report':{'plugin':'linux-stats','data':{'diskfree':'123456561432'}}}")
        except Exception, E:
            print "error connecting to master", E
            return
    else:
        print "socket already open"

    # load all the plugins

def print_error(*args):
    """callback run by found_new_service() when there is an error"""
    print 'error_handler'
    print args[0]


def found_new_service(interface, protocol, name, stype, domain, flags):
    """callback run by the avahi main loop when a service is found on the network"""
    print "Found Service: ", interface, protocol, name, stype, domain, flags

    if flags & avahi.LOOKUP_RESULT_LOCAL:
        # local service, skip
        print "Skipping local service"
        return

    config.server.ResolveService(interface, protocol, name, stype,
        domain, avahi.PROTO_UNSPEC, dbus.UInt32(0),
        reply_handler=service_resolved, error_handler=print_error)
