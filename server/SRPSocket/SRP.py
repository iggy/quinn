"""Secure Remote Passwords.  This is slightly different from the standard
implementation (with regard to the definition of 'u', the authentication
hash, and the fact that the database is a pickle).  Also the default random
number generator is not cryptographically strong.  It may be good enough to
password protect your MUD, if not your bank account.  Note that the passwd
database should not be world readable, or it will be vulnerable to a
dictionary attack (like the standard Unix password file).  See the SRP
distribution at http://srp.stanford.edu/srp/ for more information."""

import hashlib
from hmac import hmac
import random
import getpass
import pickle

# Some constants defining the sizes of various entities.

saltlen = 16    # bytes
tlen = 128      # bits
ablen = 128     # bits

# The prime field to work in, and the base to use.  Note that this must be
# common to both client and host. (Alternatively, the host can send these
# values to the client, who should then verify that they are safe.)
# The first number is a prime p of the form 2q + 1, where q is also prime.
# The second number is a generator in the field GF(p).

pflist = [(137656596376486790043182744734961384933899167257744121335064027192370741112305920493080254690601316526576747330553110881621319493425219214435734356437905637147670206858858966652975541347966997276817657605917471296442404150473520316654025988200256062845025470327802138620845134916799507318209468806715548156999L,
        8623462398472349872L)]

# New exceptions we raise.

class NoSuchUser(Exception): pass
class ImproperKeyValue(Exception): pass
class AuthFailure(Exception): pass

# Some utility functions:

def random_long(bits):

    """Generate a random long integer with the given number of bits."""

    r = 0L
    chunk = 24
    bchunk = (1 << chunk) - 1
    while bits > 0:
        if bits < chunk:
            bchunk = (1 << bits) - 1
        i = random.randint(0, bchunk)
        r = (r << chunk) + i
        bits = bits - chunk
    return r

def random_string(bytes):

    """Generate a random string with the given number of bytes."""

    r = ''
    for i in range(0, bytes):
        r = r + chr(random.randint(0, 255))
    return r

def string_to_long(s):

    """Convert a string of bytes into a long integer."""

    r = 0L
    for c in s:
        r = (r << 8) + ord(c)
    return r

def long_to_string(i):

    """Convert a long integer into a string of bytes."""

    s = ''
    while i > 0:
        s = chr(i & 255) + s
        i = i >> 8
    return s

def hash(s):

    """Hash a value with some hashing algorithm."""

    if type(s) != type(''):
        s = long_to_string(s)

    return hashlib.sha1.update(s).digest()

def private_key(u, s, p):

    """Given the username, salt, and cleartext password, return the private
    key, which is the long integer form of the hashed arguments."""

    h = hash(s + hash(u + p))
    x = string_to_long(h)
    return x

# This creates a new entry for the host password database.  In other words,
# this is called when the user changes his password.
# Note that when this is done over the network, the channel should be
# encrypted.  The password should obviously never be sent in the clear, and
# neither should the salt, verifier pair, as they are vulnerable to a
# dictionary attack.  For the same reason, the passwd database should not be
# world readable.

def create_new_verifier(u, p, pf):

    """Given a username, cleartext password, and a prime field, pick a
    random salt and calculate the verifier.  The salt, verifier tuple is
    returned."""

    s = random_string(saltlen)
    n, g = pf
    v = pow(g, private_key(u, s, p), n)
    return (s, v)

def new_passwd(user):
    pfid = 0
    pf = pflist[pfid]
    password = getpass.getpass('Enter new password for %s: ' % user)
    salt, verifier = create_new_verifier(user, password, pf)
    passwd[user] = (salt, verifier, pfid)

# This is the authentication protocol.  There are two parts, the client and
# the host.  These functions are called from the client side.

def client_begin(user):

    # Here we could optionally query the host for the pfid and salt, or
    # indeed the pf itself plus salt.  We'd have to verify that n and g
    # are valid in the latter case, and we need a local copy anyway in the
    # former.

    pfid = 0
    n, g = pflist[pfid]

    # Pick a random number and send it to the host, who responds with
    # the user's salt and more random numbers.  Note that in the standard
    # SRP implementation, u is derived from B.

    a = random_long(ablen)
    A = pow(g, a, n)

    return (A, a, g, n)

def client_key(user, passphrase, s, B, u, keys):
    A, a, g, n = keys

    # We don't trust the host.  Perhaps the host is being spoofed.

    if B <= 0 or n <= B:
        raise ImproperKeyValue

    # Calculate the shared, secret session key.

    x = private_key(user, s, passphrase)
    v = pow(g, x, n)
    t = B
    if t < v:
        t = t + n
    S = pow(t - v, a + u * x, n)
    K = hash(S)

    # Compute the authentication proof.
    # This verifies that we do indeed know the same session key,
    # implying that we knew the correct password (even though the host
    # doesn't know the password!)

    m = client_authenticator(K, n, g, user, s, A, B, u)

    return (K, m)

# The next function is called from the host side.

def lookup(user, A):

    """Look the user up in the passwd database, calculate our version of
    the session key, and return it along with a keyed hash of the values
    used in the calculation as proof.  The client must match this proof."""

    read_passwd()   # no way to specify the filename...
    if not passwd.has_key(user):
        raise NoSuchUser, user
    s, v, pfid = passwd[user]
    pf = pflist[pfid]
    n, g = pf

    # We don't trust the client, who might be trying to send bogus data in
    # order to break the protocol.

    if A <= 0 or n <= A:
        raise ImproperKeyValue

    # Pick our random public keys.

    while 1:
        b = random_long(ablen)
        B = (v + pow(g, b, n)) % n
        if B != 0: break
    u = pow(g, random_long(tlen), n)

    # Calculate the (private, shared secret) session key.

    t = (A * pow(v, u, n)) % n
    if t <= 1 or t + 1 == n:
        raise ImproperKeyValue  # WeakKeyValue -- could be our fault so retry
    S = pow(t, b, n)
    K = hash(S)

    # Create the proof using a keyed hash.

    m = client_authenticator(K, n, g, user, s, A, B, u)

    return (s, B, u, K, m)

# These two functions calculate the "proofs": keyed hashes of values used
# in the computation of the key.

def client_authenticator(K, n, g, user, s, A, B, u):
    return hmac(K, hash(n) + hash(g) + hash(user) + s + `A` + `B` + `u`)

def host_authenticator(K, A, m):
    return hmac(K, `A` + m)

# Simple password file management.

def read_passwd(filename = 'passwd'):
    global passwd
    try:
        f = open(filename)
        passwd = pickle.load(f)
        f.close()
    except:
        passwd = {}

def write_passwd(filename = 'passwd'):
    f = open(filename, 'w')
    pickle.dump(passwd, f)
    f.close()

# To set a user's initial password, run "python SRP.py" and issue a
# 'passwd user' command, followed by 'save'.  EOF to exit, 'quit' to abort.

if __name__ == '__main__':
    from cmd import Cmd
    class srp(Cmd):
        def __init__(self):
            Cmd().__init__(self)
            self.saved = 1
        def emptyline(self):
            pass
        def do_EOF(self, arg):
            print
            if not self.saved:
                print 'passwd file not saved; "quit" to abort or "save" first.'
                return
            return 1
        def do_quit(self, arg):
            return 1
        def do_list(self, arg):
            print passwd.keys()
        def do_passwd(self, user):
            new_passwd(user)
            self.saved = 0
        def do_del(self, user):
            if passwd.has_key(user):
                del(passwd[user])
            self.saved = 0
        def do_save(self, arg):
            write_passwd()
            self.saved = 1
    interp = srp()
    interp.prompt = "SRP> "
    read_passwd()
    interp.cmdloop()
