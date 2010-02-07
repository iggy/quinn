# -*- coding: utf-8 -*-
import dbus, gobject, socket
from quinn.server.plugins import QuinnPlugin

class ControlsocketPlugin(QuinnPlugin):
    """create a control socket and listen for commands coming in on it"""
    def __init__(self):
        print "init ControlsocketPlugin"

        self.sock = socket.socket(AF_UNIX)
        self.sock.bind('./quinnctl.sock')
        self.sock.listen(4)

        gobject.io_add_watch(self.sock, gobject.IO_IN, self.sock_listener)

    def data_handler(self, conn, *args):
        line = conn.recv(4096)
        if not len(line):
            print "Connection closed."
            return False

        if line == "quit":
            sys.exit()

        if line[:6] == "reload":
            reload(line[7:])

        if line[:7] == "modload":
            import


        return True

    def sock_listener(self, sock, *args):
        """setup connection coming in to listen for incoming data"""
        conn, addr = sock.accept()
        print "Connected", conn, addr
        gobject.io_add_watch(conn, gobject.IO_IN, self.data_in_handler)
        return True