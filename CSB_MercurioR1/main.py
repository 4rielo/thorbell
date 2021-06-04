import sys

import PySide2
from PySide2 import QtGui, QtWidgets

#from CSB_MercurioR1 import Fprincipal
import threading
import time
import json
import Fprincipal
from datetime import datetime, date
import subprocess

lightOnOff = False
lightPercent=100
uvOnOff = False
UV_Timer = 0
UV_TimerEnable = False
texto = dict()

path = __file__.replace("/main.py","")
dataPath=path + "/../DATA"
statusFile= path + "/status.dat"
usersFile = path + "/users.dat"
infoFile= path +"/info.dat"
globalPath = path + "/.."
port = 8085
localhost = f"http://localhost:{port}"

def statusTimer():              #StatusTimer, reads statuts file every XXX seconds, and activates or deactivates outputs
    ms100=0
    global statusFile
    while(True):
        ms100 += 1
        if(ms100>10):
            #HERE READS THE STATUS FILE AND ACTS ACCORDINGLY
            with open(statusFile) as f:
                data = json.load(f)
            
            ms100=0
        time.sleep(0.1)

def main():
    global statusFile
    global texto
    #HERE OPENS STATUS FILE AND SETS OUTPUTS TO 0
    try:                 
        print("Trying to open status file")           
        f=open(statusFile, "r")         #Busca el archivo statusFile, si existe, lo abre
        data = json.load(f)               #y carga el último estado guardado
        f.close()                       #(cierra el archivo, no lo necesita por ahora)
        print("Status File found, reading initial status")
    except:                             #Si no econtró el arvchivo
        data = {                        #genera un status inicial
            "Idioma" : "es-AR",
            "LED" : False,
            "LEDPWM" : 100,
            "UV_Light" : False,
            "UV_PWM" : 100,
            "UV_Timer" : 0,
            "UV_TimerEnable": False,
            "UV_Calendar": False,
            "UV_Calendar_init": format(datetime.now(),"%Y/%m/%d %H:%M"),
            "UV_Calendar_end": format(datetime.now(),"%Y/%m/%d %H:%M"),
            "PWR" : False,
            "screenUser" : "",
            "webUsers" : {
                "userA" : {
                    "ip" : "",
                    "user": "",
                },
            },
            "WARNINGS" : []
        }
        with open(statusFile, "w") as f:                   #Y lo guarda en statusFile (crea el archivo)
            json.dump(data,f)
        print("Status file not found. Creates initial (default) status file")
    
    print(path+"/idioma/" + data.get("Idioma") + ".dat")

    with open(path+"/idioma/" + data.get("Idioma") + ".dat") as f:
        global texto
        texto = json.load(f)
        
    

    #status = threading.Thread(target=statusTimer, daemon=True)
    #status.start()
    
    ###############################################    
    app = QtWidgets.QApplication(sys.argv)
    print("Loading Window")
    window = Fprincipal.MainWindow()   #  loader.load("mainwindow.ui", None)
    window.show()
    app.exec_()

def MicroProcesses():
    command = f"python3 {globalPath}/statusServer.py {port}"
    subprocess.run(command,shell=True)


if __name__ == "__main__":
    microProcess=threading.Thread(target=MicroProcesses,daemon=True)
    microProcess.start()

    main()