from xmlrpc.server import SimpleXMLRPCServer
import os
import sys
import inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import constants

def replicateRequest(vote_request, data):
    print('replicateRequest')
    print(vote_request)
    print(data)
    if vote_request == 'commit':
        with open('data.json', 'w') as fp:
            json.dump(data, fp,sort_keys=True, indent=4)
        return 1
    else:
        print('abort')
        return -1

def restoreRequest( data):
    print('restoreRequest')
    # TODO: Implement restore service
    return 1


server = SimpleXMLRPCServer((constants.REPLICATION_SERVER_1_ADDRESS, constants.REPLICATION_SERVER_1_PORT), allow_none=True)
# serverrest = SimpleXMLRPCServer((constants.RESTORE_SERVER_1_ADDRESS, constants.RESTORE_SERVER_1_PORT), allow_none=True)

server.register_function(restoreRequest, 'restoreRequest')
server.register_function(replicateRequest, 'replicateRequest')
server.serve_forever()
