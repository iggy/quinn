"""SRP authenticated sockets."""

import SRP
import socket
import SocketServer
import string
import base64
import getpass

def SRPSocket(host, port, user, passphrase = None):
    """Create a connection to the given host and port, which must be
    running the SRPServer.  Perform authentication and return the socket
    and session key if successful, or raise an exception if not."""

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    key = SRPAuth(sock, user, passphrase)
    return (sock, key)

def SRPAuth(sock, user, passphrase = None):
    """Perform an SRP authentication on a socket.  Return the session key
    if authentication was successful, or raise an exception if it was not.
    The other end of the socket must be ready to receive the SRP
    commands."""

    if not passphrase:
	passphrase = getpass.getpass('Enter passphrase for %s: ' % user)

    # Send the USER command.

    sock.send('USER %s\n' % user)

    # Get the client-side keys and send the public one.

    keys = SRP.client_begin(user)
    A = keys[0]
    sock.send(encode_long(A))

    # Read the response.

    file = sock.makefile('rb')
    line = file.readline()
    if line[0:3] != 'KEY':
	raise SRP.NoSuchUser, line
    s = read_string(file)
    B = read_long(file)
    u = read_long(file)

    # Now calculate the session key and send the proof.

    K, m = SRP.client_key(user, passphrase, s, B, u, keys)
    sock.send(encode_string(m))
    line = file.readline()
    if line[0:3] != 'AOK':
	raise SRP.AuthFailure, line

    # Authenticate the host.

    m1 = SRP.host_authenticator(K, A, m)
    m = read_string(file)
    if m != m1:
	raise SRP.AuthFailure, "Host authentication failed."

    # All done, return the session key.

    return K

# This is the server that handles the host side of SRP authentication.

class SRPHost(SocketServer.BaseRequestHandler):
    def handle(self):
	sock = self.request
	file = sock.makefile('rb')

	# Receive the username and public key A from the client.

	while 1:
	    line = file.readline()
	    if not line:
		return
	    if line[0:4] == 'USER':
		l = string.split(line)
		if len(l) == 2:
		    break
	    sock.send('Please specify USER.\n')
	user = l[1]
	try:
	    A = read_long(file)
	except EOFError:
	    return

	# Calculate the public and private values, and send the public stuff
	# to the client.

	try:
	    s, B, u, K, m = SRP.lookup(user, A)
	except SRP.NoSuchUser:
	    sock.send('No such user "%s".\n' % user)
	    return
	sock.send('KEY\n')
	sock.send(encode_string(s))
	sock.send(encode_long(B))
	sock.send(encode_long(u))

	# The client now sends us its proof.

	try:
	    m1 = read_string(file)
	except EOFError:
	    return
	if m != m1:
	    sock.send('Client authentication failed.\n')
	    return
	sock.send('AOK\n')

	# Send the host authentication proof.

	sock.send(encode_string(SRP.host_authenticator(K, A, m)))

	# At this point (assuming the client accepts the host authentication),
	# the socket has been authenticated and K is the secret session key.

	if self.__dict__.has_key('auth_socket'):
	    self.auth_socket(file, sock, K)
	else:

	    # Simple echo server.

	    while 1:
		s = file.readline()
		if not s:
		    return
		sock.send(s)

# To specify a different server than the simple echo server, subclass SRPHost
# and provide an 'auth_socket' method that is passed the socket (as a
# readable file object and as the socket object itself), and the session key.
# Then pass that to SRPServer as the second argument.

def SRPServer(port, server = SRPHost):
    s = SocketServer.ForkingTCPServer(('', port), server)
    s.serve_forever()

# Utility functions to read/write long ints and strings from/to a file (or
# socket).  Values are stored in base64 delimited by blank lines.

def encode_long(val):
    s = base64.encodestring(SRP.long_to_string(val))
    return s + '\n'

def read_long(file):
    ll = []
    while 1:
	line = file.readline()
	if not line:
	    raise EOFError
	l = string.strip(line)
	if not l:
	    break
	ll.append(l)
    val = SRP.string_to_long(base64.decodestring(string.join(ll, '')))
    return val

def encode_string(val):
    s = base64.encodestring(val)
    return s + '\n'

def read_string(file):
    ll = []
    while 1:
	line = file.readline()
	if not line:
	    raise EOFError
	l = string.strip(line)
	if not l:
	    break
	ll.append(l)
    val = base64.decodestring(string.join(ll, ''))
    return val

