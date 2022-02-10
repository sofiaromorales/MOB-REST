from xmlrpc.server import SimpleXMLRPCServer
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import constants

def restoreRequest( data):
    print('restoreRequest')
    # TODO: Implement replication service
      

server = SimpleXMLRPCServer((constants.RESTORE_SERVER_1_ADDRESS, constants.RESTORE_SERVER_1_PORT), allow_none=True)
server.register_function(restoreRequest, 'restoreRequest')
server.serve_forever()
