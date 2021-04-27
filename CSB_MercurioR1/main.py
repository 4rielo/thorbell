import sys

import PySide2
from PySide2 import QtGui, QtWidgets

#from CSB_MercurioR1 import Fprincipal
import threading
import time
import json
import Fprincipal

lightOnOff = False
lightPercent=100
texto = dict()

uvOnOff = False

path = __file__.replace("/main.py","")
dataPath=path + "../DATA"
statusFile= path + "/status.dat"

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
            "UVLED" : False,
            "UVLEDPWM" : 100,
            "UVLEDTIMER" : 0,
            "PWR" : False,
            "WARNINGS" : [
                "puerta_abierta",
                "filtro_saturado"
                ]
        }
        with open(statusFile, "w") as f:                   #Y lo guarda en statusFile (crea el archivo)
            json.dump(data,f)
        print("Status file not found. Creates initial (default) status file")
    
    print(path+"/idioma/" + data.get("Idioma") + ".dat")

    with open(path+"/idioma/" + data.get("Idioma") + ".dat") as f:
        global texto
        texto = json.load(f)
        
    

    status = threading.Thread(target=statusTimer, daemon=True)
    status.start()
    
    ###############################################    
    app = QtWidgets.QApplication(sys.argv)
    print("Loading Window")
    window = Fprincipal.MainWindow()   #  loader.load("mainwindow.ui", None)
    window.show()
    app.exec_()



if __name__ == "__main__":
    main()