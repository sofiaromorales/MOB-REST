import random
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import constants

def replicateObjects(vote_request, data):
    print('coordinator replicateObjects')
    ##  Call replication servers method `replicateObject(vote_request, data)`
    if vote_request == 'randomize':
        vote = 'commit' if bool(random.getrandbits(1)) else 'abort'
        return replicationServerProxy.replicateRequest(vote, data)
    else:
        return replicationServerProxy.replicateRequest(vote_request, data)

def restoregetObjects():
    print('restoregetObjects')
    return replicationServerProxy.restoreRequest()


# restoreServerProxy = xmlrpc.client.ServerProxy('http://' + constants.COORDINATOR_ADDRESS + ':' + str(constants.RESTORE_SERVER_1_PORT))

replicationServerProxy = xmlrpc.client.ServerProxy('http://' + constants.REPLICATION_SERVER_1_ADDRESS + ':' + str(constants.REPLICATION_SERVER_1_PORT))

server = SimpleXMLRPCServer((constants.COORDINATOR_ADDRESS, constants.COORDINATOR_PORT), allow_none=True)
server.register_function(restoregetObjects, 'restoregetObjects')
server.register_function(replicateObjects, 'replicateObjects')
# server = SimpleXMLRPCServer((constants.REPLICATION_SERVER_1_ADDRESS, constants.COORDINATOR_PORT), allow_none=True)

server.serve_forever()
