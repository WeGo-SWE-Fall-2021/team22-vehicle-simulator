from threading import *
from requests import *
import time


class Vehicle(Thread):
    def __init__(self, status = 'ready', vType = 'food', location = [30.256937, -97.74562], dock = [30.256937, -97.74562]):
        self.status = status
        self.vType = vType
        self.location = location
        self.dock = dock
        self.heartbeating = False
        
    def startHeartBeat(self):
        self.heartbeating = True
        self.heartbeat()

    def stopHeartBeat(self):
        self.heartbeating = False

    def heartbeat(self):
        while self.heartbeating:
            ## add params to request to send vehicle updates
            heartbeat = requests.get('supply.team22.sweispring21.tk/api/v1/heartbeat')
            time.sleep(5)

        ## handle responses - should either be something to denote that no order has been sent OR
        ## an array of locations / directions of route that should trigger the following Vehicle response
            ## ---->>> Change status to busy, startRoute() function

    def startRoute(self, route):



