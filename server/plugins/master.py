# -*- coding: utf-8 -*-
import dbus, gobject, avahi, socket, anyjson
from quinn.server.plugins import QuinnPlugin
#from quinn.server.testd import main_loop

class MasterPlugin(QuinnPlugin):
    def __init__(self):
        print "Starting up as master"

        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # listen on all interfaces and a "random" open unprivileged port
        self.sock.bind(('', 0))
        self.sock.listen(4)
        print "Listening...", self.sock.getsockname()
        gobject.io_add_watch(self.sock, gobject.IO_IN, self.server_listener)

        # some other avahi init stuff
        self.bus = dbus.SystemBus()

        self.server = dbus.Interface(
            self.bus.get_object(avahi.DBUS_NAME, avahi.DBUS_PATH_SERVER),
            avahi.DBUS_INTERFACE_SERVER)

        self.asType = "_quinn._tcp"
        self.asTXT = "txt record"
        self.asDomain = "local"
        self.asGroup = None
        self.asRenameCount = 12
        (self.asHostname, self.asPort) = self.sock.getsockname()

        # set up the service with avahi
        self.server.connect_to_signal('StateChange', self.server_state_changed)
        self.server_state_changed(self.server.GetState())


    def data_in_handler(self, conn, *args):
        """run when data comes in from one of clients"""
        line = conn.recv(4096)
        if not len(line):
            print "Connection closed."
            return False

        print "data_in_handler:", anyjson.deserialize(line)

        return True


    def server_listener(self, sock, *args):
        """setup connection coming in to listen for incoming data"""
        conn, addr = sock.accept()
        print "Connected", conn, addr
        gobject.io_add_watch(conn, gobject.IO_IN, self.data_in_handler)
        return True

    def add_service(self):
        """add a service
        run by self.server_state_change() and self.entry_group_state_changed()
        """
        if self.asGroup is None:
            self.asGroup = dbus.Interface(
                self.bus.get_object(avahi.DBUS_NAME, self.server.EntryGroupNew()),
                avahi.DBUS_INTERFACE_ENTRY_GROUP)
            self.asGroup.connect_to_signal('StateChange', self.entry_group_state_changed)

            self.asGroup.AddService(
                avahi.IF_UNSPEC,
                avahi.PROTO_UNSPEC,
                dbus.UInt32(0),
                socket.gethostname(),
                self.asType,
                self.asDomain,
                '',
                dbus.UInt16(self.asPort),
                avahi.string_array_to_txt_array(self.asTXT))
            self.asGroup.Commit()

    def remove_service(self):
        if not self.asGroup is None:
            self.asGroup.Reset()

    def server_state_changed(self, state):
        """connected to the avahi server main loop signal "StateChanged"
        """
        if state == avahi.SERVER_COLLISION:
            print "WARNING: Server name collision"
            self.remove_service()
        elif state == avahi.SERVER_RUNNING:
            self.add_service()

    def entry_group_state_changed(self, state, error):
        """connected to the avahi service group signal "StateChanged"
        """
        print "state change: %i" % state

        if state == avahi.ENTRY_GROUP_ESTABLISHED:
            print "Service established."
        elif state == avahi.ENTRY_GROUP_COLLISION:

            self.asRenameCount = self.asRenameCount - 1
            if self.asRenameCount > 0:
                self.asName = self.server.GetAlternativeServiceName(socket.gethostname())
                print "WARNING: Service name collision, changing name to '%s' ..." % self.asName
                self.remove_service()
                self.add_service()

            else:
                print "ERROR: No suitable service name found after %i retries, exiting." % n_rename
                main_loop.quit()
        elif state == avahi.ENTRY_GROUP_FAILURE:
            print "Error in group state changed", error
            main_loop.quit()
            return