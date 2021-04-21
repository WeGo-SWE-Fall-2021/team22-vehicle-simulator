import vehicle
import json
import requests


vehicleList = []

def loadVehicles():
    vehicleResponse = requests.get('supply.team22.sweispring21.tk/api/v1/getAllVehicles')
    vehicleDict = json.loads(vehicleResponse.text)
    return vehicleDict

def showAllVehicles():
    print("""_________________________________""")
    print("""*********************************""")
    for v in vehicleList:
        print("""{v.vehicleId}***{v.status}***{v.location}***{v.dock}***{v.heartbeating}***""")
        print("""*********************************""")
    print("""_________________________________""")

def showVehicle(index):
    v = vehicleList[index]
    print("""_________________________________""")
    print("""{v.vehicleId}***{v.status}***{v.location}***{v.dock}***{v.heartbeating}***""")
    print("""_________________________________""")

def startAllHeartbeats():
    for v in vehicleList:
        if v.running = False:
            v.run()
        else:
            v.startHeartbeat()

def stopAllHeartbeats():
    for v in vehicleList:
        v.heartbeating = False

def moveVehicle(index, x, y):
    pass
    v = vehicleList[index]

def main():
    loadVehicles()
    simulating = True
    testOption = -1
    while simulating:
        print("""
 ::::::::::TESTING OPTIONS:::::::::
S  ::::   START ALL HEARTBEATS
1  ::::   SHOW VEHICLE LIST (UPDATE)
2  ::::   SELECT VEHICLE FROM LIST
3  ::::   STOP ALL HEARTBEATS
X  ::::   STOP SIMULATING AND EXIT (STOPS ALL HEARTBEATS)
""")
        testOption = input('SELECT OPTION FROM ABOVE ::: ')
        if testOption == 'S':
            startAllHeartbeats()
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 1:
            loadVehicles()
            showAllVehicles()
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 2:
            vehicleSelected = -1
            loadVehicles()
            showAllVehicles()
            vehicleSelected = input('SELECT VEHICLE ::: ')
            try:
                selectedVehicle = vehicleList[vehicleSelected]
                showVehicle()
                ## ADD SINGLE VEHICLE OPTIONS
            except:
                print("INVALID INPUT")
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == '3':
            stopAllHeartbeats()
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 'X':
            stopAllHeartbeats()
            simulating = False
            input('PRESS ENTER TO EXIT')
        else:
            print('INVALID OPTION INPUT')
            input('PRESS ENTER TO RETURN TO MENU')
            


if __name__ == "__main__":
    main()