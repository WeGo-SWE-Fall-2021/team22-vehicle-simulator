import vehicle
import json
import requests

def loadVehicles():
    vehicleResponse = requests.get('http://supply.team22.sweispring21.tk/api/v1/supply/getAllVehicles')
    vehicleDict = json.loads(vehicleResponse.text)
    vehicleList = []
    for i in vehicleDict:
        av = vehicle.Vehicle(i["_id"], i["status"], i["location"], i["dock"])
    
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
        if v.running == False:
            v.run()
        else:
            v.startHeartbeat()

def stopAllHeartbeats(vList):
    for v in vList:
        v.heartbeating = False

def moveVehicle(index, x, y):
    pass
    v = vehicleList[index]

def main():
    vList = loadVehicles()
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
            vList = loadVehicles()
            startAllHeartbeats(vList)
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 2:
            vList = loadVehicles()
            showAllVehicles(vList)
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 3:
            vehicleSelected = -1
            vList = loadVehicles()
            showAllVehicles(vList)
            vehicleSelected = input('SELECT VEHICLE ::: ')
            try:
                showVehicle(vehicleSelected, vList)
                ## ADD SINGLE VEHICLE OPTIONS
            except:
                print("INVALID INPUT")
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 4:
            stopAllHeartbeats(vList)
            input('PRESS ENTER TO RETURN TO MENU')
        elif testOption == 0:
            stopAllHeartbeats(vList)
            simulating = False
            input('PRESS ENTER TO EXIT')
        else:
            print('INVALID OPTION INPUT')
            input('PRESS ENTER TO RETURN TO MENU')
            

if __name__ == "__main__":
    main()