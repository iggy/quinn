import SRPSocket

# To set a user's initial password, run "python SRP.py" (from the server)
# and issue a 'passwd user' command, followed by 'save'.  EOF to exit,
# 'quit' to abort.

# Start the server with "python server.py"

# This will create an authenticated socket and secure session key for 'user':

sock, key = SRPSocket.SRPSocket('', 1234, 'user')
