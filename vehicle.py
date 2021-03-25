from threading import *
from requests import *
import time
import json


class Vehicle(Thread):
    def __init__(self, id, status = 'ready', vType = 'food', location = [30.256937, -97.74562], dock = [30.256937, -97.74562]):
        self.id
        self.status = status
        self.vType = vType
        self.location = location
        self.dock = dock
        self.heartbeating = False

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        
    def startHeartBeat(self):
        self.heartbeating = True
        self.heartbeat()

    def stopHeartBeat(self):
        self.heartbeating = False

    def heartbeat(self):
        while self.heartbeating:
            
            vehicleUpdateJSON = self.toJSON()
            heartbeatResponse = requests.get('supply.team22.sweispring21.tk/api/v1/vehicleHeartbeat', vehicleUpdateJSON, timeout=5)
            time.sleep(5)


## handle responses - should either be something to denote that no order has been sent OR
## an array of locations / directions of route that should trigger the following Vehicle response
            ## ---->>> Change status to busy, startRoute() function


            ## NO ROUTE to equal no order / do nothing yet response
            if heartbeatResponse == 'NO ROUTE':
                pass
            else:
                route = heartbeatResponse
                self.startRoute(route)
                ## consider sending a different HTTP Request as order confirmation

        

    def startRoute(self, route):
        self.status = busy
        ## parse through JSON Directions
        ## pull locations into steps array
        ## nextStep() until finalDest
        ## finalDest and reverse nextStep() until dock
        ## once at dock, update status to ready

