import json
import requests
import time

from vehicle import Vehicle

def loadVehiclesFromDB():
    vehicleResponse = requests.get('http://supply.team22.sweispring21.tk/api/v1/supply/getAllVehicles')
    vehicleDict = json.loads(vehicleResponse.text)
    vehicleList = []
    for i in vehicleDict:
        av = Vehicle(i["_id"], i["status"], i["location"], i["dock"])
        vehicleList.append(av)
    return vehicleList

def showAllVehicles(vList):
    print("""_________________________________""")
    print("""*********************************""")
    index = 0
    for v in vList:
        print(index , ' ----- ' , v.toString())
        print("""*********************************""")
        index += 1
    print("""_________________________________""")

def showVehicle(index, vList):
    v = vList[index]
    print("""_________________________________""")
    print(v.toString())
    print("""_________________________________""")

def startAllHeartbeats(vList):
    for v in vList:
        if v.heartbeating == False:
            v.startHeartbeat()

def stopAllHeartbeats(vList):
    print("---STOPPING HEARTBEATS---")

    for v in vList:
        v.stopHeartBeat()

    while len(list(filter(lambda x: x._heartbeatThread.is_alive() == True, vList))) != 0:
        time.sleep(2)
        print("---STOPPING HEARTBEATS---")


def moveVehicle(index, x, y):
    pass
    v = refreshVehicleList[index]

def refreshVehicleList(main_list):
    new_list = loadVehiclesFromDB()

    # Remove old vehicles
    for oldVehicle in main_list:
        matched = False
        for vehicle in new_list:
            if vehicle == oldVehicle:
                matched = True
        if not matched:
            main_list.remove(oldVehicle)

    # Add new values
    for newVehicle in new_list:
        matched = False
        for vehicle in main_list:
            if vehicle == newVehicle:
                matched = True
        if not matched:
            main_list.append(newVehicle)

def main():
    mainVehicleList = []
    refreshVehicleList(mainVehicleList)
    simulating = True
    testOption = -1
    while simulating:
        print("""
 ::::::::::TESTING OPTIONS:::::::::
1  ::::   START ALL HEARTBEATS
2  ::::   SHOW VEHICLE LIST (UPDATE)
3  ::::   SELECT VEHICLE FROM LIST
4  ::::   STOP ALL HEARTBEATS
0  ::::   STOP SIMULATING AND EXIT (STOPS ALL HEARTBEATS)
""")
        testOption = int(input('SELECT OPTION FROM ABOVE ::: '))
        if testOption == 1:
            refreshVehicleList(mainVehicleList)
            startAllHeartbeats(mainVehicleList)
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 2:
            refreshVehicleList(mainVehicleList)
            showAllVehicles(mainVehicleList)
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 3:
            vehicleSelected = -1
            refreshVehicleList(mainVehicleList)
            showAllVehicles(mainVehicleList)
            vehicleSelected = input('SELECT VEHICLE ::: ')
            try:
                showVehicle(vehicleSelected, mainVehicleList)
                ## ADD SINGLE VEHICLE OPTIONS
            except:
                print("INVALID INPUT")
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 4:
            stopAllHeartbeats(mainVehicleList)
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 0:
            stopAllHeartbeats(mainVehicleList)
            simulating = False
            input('PRESS ENTER TO EXIT')
        else:
            print('INVALID OPTION INPUT')
            input('PRESS ENTER TO RETURN TO MENU')
            

if __name__ == "__main__":
    main()