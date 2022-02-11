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

def restoreRequest( data):
    print('restoreRequest')
    # TODO: Implement replication service


server = SimpleXMLRPCServer((constants.REPLICATION_SERVER_1_ADDRESS, constants.REPLICATION_SERVER_1_PORT), allow_none=True)
serverrest = SimpleXMLRPCServer((constants.RESTORE_SERVER_1_ADDRESS, constants.RESTORE_SERVER_1_PORT), allow_none=True)

serverrest.register_function(restoreRequest, 'restoreRequest')
server.register_function(replicateRequest, 'replicateRequest')
server.serve_forever()
