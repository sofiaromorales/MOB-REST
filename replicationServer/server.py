from xmlrpc.server import SimpleXMLRPCServer
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import constants

def replicateRequest(vote_request, data):
    print('replicateRequest')
    if vote_request == 'commit':
        # TODO: Implement replication service
        return 1
    else:
        return -1

server = SimpleXMLRPCServer((constants.REPLICATION_SERVER_1_ADDRESS, constants.REPLICATION_SERVER_1_PORT), allow_none=True)
server.register_function(replicateRequest, 'replicateRequest')
server.serve_forever()
