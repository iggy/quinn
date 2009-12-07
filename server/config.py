import socket#, qsrvutils

# master daemon name
masterName = "vmhost03"

# advertised service variables
asName = "%s" % (socket.gethostname())
asType = "_quinn._tcp"
asPort = None #qsrvutils.find_open_port() # FIXME racy, we find an open one here and don't actually bind till later
asTXT = "txt record"
asDomain = "local"
asHost = "" #socket.gethostname()
asGroup = None
asRenameCount = 12

# other "globals"
bus = None
main_loop = None
server = None
client = None
mstr_sock = None