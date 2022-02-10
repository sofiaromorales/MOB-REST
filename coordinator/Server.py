from xmlrpc.server import SimpleXMLRPCServer
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import constants

def replicateObjects(vote_request, data):
    print('replicateObjects')
    print(data)
    ##  Call replication servers method `replicateObject(vote_request, data)`
    if vote_request == 'randomize':
        vote = 'commit' if bool(random.getrandbits(1)) else 'abort'
        ## replicationServ1.replicateObject(vote, data)`
        ## TODO: Return success or failure
    else:
        print('Not implemented yet')
        ## replicationServ2.replicateObject(vote, data)`
        ## TODO: Return success or failure


server = SimpleXMLRPCServer((constants.COORDINATOR_ADDRESS, constants.COORDINATOR_PORT), allow_none=True)
server.register_function(replicateObjects, 'replicateObjects')
server.serve_forever()
