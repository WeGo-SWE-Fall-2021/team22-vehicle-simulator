import vehicle
import json

vehicleList = []

def loadVehicles():
    ## LOAD VEHICLES INTO LIST FROM DATABASE
    pass

def showAllVehicles():
    ## PRINT VEHICLE LIST TO CONSOLE FOR TEST USER
    pass

def showVehicle():
    ## PRINT SINGLE VEHICLE TO CONSOLE FOR TEST USER
    pass

def startAllHeartbeats():
    # START ALL VEHICLE HEARTBEATS
    pass

def stopAllHeartbeats():
    # STOP ALL VEHICLE HEARTBEATS
    pass

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