import xmlrpc.client
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import constants

proxy = xmlrpc.client.ServerProxy('http://' + constants.COORDINATOR_ADDRESS + ':' + str(constants.COORDINATOR_PORT))

def getCoordinatorReplica(vote_request, data):
    proxy.replicateObjects(vote_request, data)
