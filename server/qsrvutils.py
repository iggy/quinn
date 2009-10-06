
import dbus, gobject, avahi, config, socket

def find_open_port():
    import random, socket
    while True:
        s = None
        try:
            port = random.randint(10000,32000)
            print "trying port", port
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('0.0.0.0', port))
            s.close()
            break
        except socket.error:
            # probably already open
            s.close()
            disp += 1
    print "will be listening on port ", port
    return port
    
def add_service():
    #global asName, asType, asPort, asDomain, asHost, asGroup, asTXT
    if config.asGroup is None:
        config.asGroup = dbus.Interface(
            config.bus.get_object(avahi.DBUS_NAME, config.server.EntryGroupNew()), 
            avahi.DBUS_INTERFACE_ENTRY_GROUP)
        config.asGroup.connect_to_signal('StateChange', entry_group_state_changed)
        
        config.asGroup.AddService(
            avahi.IF_UNSPEC,
            avahi.PROTO_UNSPEC,
            dbus.UInt32(0),
            config.asName,
            config.asType,
            config.asDomain,
            config.asHost,
            dbus.UInt16(config.asPort),
            avahi.string_array_to_txt_array(config.asTXT))
        config.asGroup.Commit()

def remove_service():
    #global asGroup
    if not config.asGroup is None:
        config.asGroup.Reset()
        
def server_state_changed(state):
    if state == avahi.SERVER_COLLISION:
        print "WARNING: Server name collision"
        remove_service()
    elif state == avahi.SERVER_RUNNING:
        add_service()

def entry_group_state_changed(state, error):
    #global asName, server, asRenameCount

    print "state change: %i" % state

    if state == avahi.ENTRY_GROUP_ESTABLISHED:
        print "Service established."
    elif state == avahi.ENTRY_GROUP_COLLISION:

        config.asRenameCount = config.asRenameCount - 1
        if config.asRenameCount > 0:
            config.asName = config.server.GetAlternativeServiceName(asName)
            print "WARNING: Service name collision, changing name to '%s' ..." % config.asName
            remove_service()
            add_service()

        else:
            print "ERROR: No suitable service name found after %i retries, exiting." % n_rename
            config.main_loop.quit()
    elif state == avahi.ENTRY_GROUP_FAILURE:
        print "Error in group state changed", error
        config.main_loop.quit()
        return


def service_resolved(*args):
    print 'service resolved'
    print 'name:', args[2]
    print 'address:', args[7]
    print 'port:', args[8]
    
    print "opening socket to %s:%s" % (args[7], args[8])
    
    try:
        sock = socket.socket()
        sock.connect((args[7], args[8]))
        sock.send("Hello World")
    except:
        print "error connecting to master"
        return

def print_error(*args):
    print 'error_handler'
    print args[0]


def found_new_service(interface, protocol, name, stype, domain, flags):
    print "Found Service: ", interface, protocol, name, stype, domain, flags
    
    if flags & avahi.LOOKUP_RESULT_LOCAL:
        # local service, skip
        print "Skipping local service"
        return
    
    config.server.ResolveService(interface, protocol, name, stype, 
        domain, avahi.PROTO_UNSPEC, dbus.UInt32(0), 
        reply_handler=service_resolved, error_handler=print_error)

def server_handler(conn, *args):
    line = conn.recv(4096)
    if not len(line):
        print "Connection closed."
        return False
    else:
        print line
        return True


def server_listener(sock, *args):
    conn, addr = sock.accept()
    print "Connected", conn, addr
    gobject.io_add_watch(conn, gobject.IO_IN, server_handler)
    return True


def server_init():
    config.sock = socket.socket()
    config.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    config.sock.bind((host, port))
    config.sock.listen(1)
    print "Listening..."
    gobject.io_add_watch(config.sock, gobject.IO_IN, server_listener)
    
    