from threading import *
import requests
import time
import json

## status: ready, busy, oos
## vType: food
class Vehicle(Thread):
    def __init__(self, vehicleId, status, location, dock):
        self.vehicleId = vehicleId
        self.status = status
        self.location = location
        self.dock = dock
        self.heartbeating = False
        self.running = False

    def run(self):
        self.startHeartbeat()
        self.running = True

    def toDict(self):
        vAsDict = {}
        vAsDict["vehicleId"] = self.vehicleId
        vAsDict["location"] = self.location
        vAsDict["status"] = self.status
        return vAsDict

        
    def startHeartbeat(self):
        self.heartbeating = True
        self.heartbeat()

    def stopHeartBeat(self):
        self.heartbeating = False
        self.status = 'oos'

    def heartbeat(self):
        while self.heartbeating:
            
            payload = self.toDict()
            heartbeatResponse = requests.post('https://supply.team22.sweispring21.tk/api/v1/supply/vehicleHeartbeat',  json=payload, timeout=10)
            time.sleep(15)

## handle responses - should either be something to denote that no order has been sent OR
## an array of locations / directions of route that should trigger the following Vehicle response
            ## ---->>> Change status to busy, startRoute() function


            ## NO ROUTE to equal no order / do nothing yet response
            if heartbeatResponse == {'Heartbeat' : 'Received'} and heartbeatResponse.status_code == 200:
                pass
            elif heartbeatResponse.status_code == 200:
                route = json.loads(heartbeatResponse.text)
                self.startRoute(route)
                ## consider sending a different HTTP Request as order confirmation
            else:
                pass

        
    def toString(self):
        retStr = f"""ID = {self.vehicleId} *** STATUS = {self.status} *** LOCATION = {self.location} *** DOCK = {self.dock} *** isHB = {self.heartbeating} ***"""
        return retStr

    def startRoute(self, route):

        ## STORE ROUTE RESPONSE TO ARRAY FOR VEHICLE USE
        self.status = 'busy'
        ## finalDest and reverse nextStep() until dock
        ## once at dock, update status to ready
        for i in range (0, len(route)):
            ## ITERATE ROUTE SIMULATION TO BETTER REPRESENT ROUTE
            time.sleep(45)
            self.location = route[i]

        ## Return to Dock
        for i in range (len(route), 0, -1):
            ## ITERATE ROUTE SIMULATION TO BETTER REPRESENT ROUTE
            time.sleep(45)
            self.location = route[i]
        
        self.location = self.dock
        self.status = 'ready'


## TESTING
def main():
    pass

if __name__ == "__main__":
    main()