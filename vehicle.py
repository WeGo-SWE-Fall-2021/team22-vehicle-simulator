from threading import *
import requests
import time
import json

## status: ready, busy, oos
## vType: food
class Vehicle:
    def __init__(self, vehicleId, status, location, dock):
        self._vehicleId = vehicleId
        self._status = status
        self._location = location
        self._dock = dock
        self._heartbeating = False
        self._heartbeatThread = None

    @property
    def vehicleId(self):
        return self._vehicleId

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, value):
        self._location = value

    @property
    def dock(self):
        return self._dock

    @dock.setter
    def dock(self, value):
        self._dock = value

    @property
    def heartbeating(self):
        return self._heartbeating

    @heartbeating.setter
    def heartbeating(self, value):
        self._heartbeating = value

    def toDict(self):
        vAsDict = {}
        vAsDict["vehicleId"] = self.vehicleId
        vAsDict["location"] = self.location
        vAsDict["status"] = self.status
        return vAsDict
        
    def startHeartbeat(self):
        self.heartbeating = True
        self._heartbeatThread = Thread(target=self.heartbeat, name=f"Vehicle_{self.vehicleId}")
        self._heartbeatThread.start()

    def stopHeartBeat(self):
        self.heartbeating = False

    def heartbeat(self):
        while self.heartbeating:
            self.status = "ready"
            payload = self.toDict()
            heartbeatResponse = requests.put('https://supply.team22.sweispring21.tk/api/v1/supply/vehicleHeartbeat',  json=payload, timeout=10)

            ## handle responses - should either be something to denote that no order has been sent OR
            ## an array of locations / directions of route that should trigger the following Vehicle response
            ## ---->>> Change status to busy, startRoute() function

            json_body = json.loads(heartbeatResponse.text)

            ## NO ROUTE to equal no order / do nothing yet response
            if json_body == {'Heartbeat' : 'Received'} and heartbeatResponse.status_code == 200:
                pass
            elif heartbeatResponse.status_code == 200:
                self.startRoute(json_body)
                ## consider sending a different HTTP Request as order confirmation
            else:
                pass
            time.sleep(15)

        self.status = 'oos'
        payload = self.toDict()
        heartbeatResponse = requests.put('https://supply.team22.sweispring21.tk/api/v1/supply/vehicleHeartbeat',  json=payload, timeout=10)

    def toString(self):
        retStr = f"""ID = {self.vehicleId} *** STATUS = {self.status} *** LOCATION = {self.location} *** DOCK = {self.dock} *** isHB = {self.heartbeating} ***"""
        return retStr

    def startRoute(self, route):
        self.status = 'busy'

        coordinates = route["coordinates"]
        ## STORE ROUTE RESPONSE TO ARRAY FOR VEHICLE USE

        last_index_location = 0
        last_location_latitude = float(self.location.split(",")[0])
        last_location_longitude = float(self.location.split(",")[1])

        for i in range(0, len(coordinates)):
            coordinate = coordinates[i]
            latitude = coordinate[0]
            longitude = coordinate[1]
            if last_location_latitude == latitude and last_location_longitude == longitude:
                last_index_location = i
                break

        ## finalDest and reverse nextStep() until dock
        ## once at dock, update status to ready
        while self.heartbeating and last_index_location < len(coordinates):
            coordinate = coordinates[last_index_location]
            latitude = coordinate[0]
            longitude = coordinate[1]
            self.location = f"{latitude},{longitude}"

            payload = self.toDict()
            heartbeatResponse = requests.put('https://supply.team22.sweispring21.tk/api/v1/supply/vehicleHeartbeat',  json=payload, timeout=10)
            time.sleep(2)
            last_index_location += 1

        ## Return to Dock
        last_index_location = len(coordinates) - 1
        while self.heartbeating and last_index_location >= 0:
            coordinate = coordinates[i]
            latitude = coordinate[0]
            longitude = coordinate[1]
            self.location = f"{latitude},{longitude}"

            payload = self.toDict()
            heartbeatResponse = requests.put('https://supply.team22.sweispring21.tk/api/v1/supply/vehicleHeartbeat',  json=payload, timeout=10)
            time.sleep(1)
            last_index_location -= 1

        if self.heartbeating:
            self.location = self.dock
            self.status = 'ready'

    def __eq__(self, value):
        return isinstance(value, Vehicle) and self.vehicleId == value.vehicleId

    def __hash__(self):
        return hash(self.vehicleId)
## TESTING
def main():
    pass

if __name__ == "__main__":
    main()