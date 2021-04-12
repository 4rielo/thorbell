#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading

from CSB_MercurioR1.Pconfig import Ui_form

class ConfigWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONFIG")

        self.update_Btn.clicked.connect(self.UpdateFunction)

        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def UpdateFunction(self):
        import subprocess
        import requests

        path=__file__
        path=path.replace("auto_update.py","")
        """f = open(path+"autoupdate.txt", "r")        #abre archivo que indica si se desea realizar un auto-update

        if(f.read(4)=="true"):                              #si el archivo comienza con la palabra "true",
            a=True                                  #ejecuta un auto update
        else:
            a=False"""

        f=open(path+"repo.txt","r")                 #obtiene la dirección del repositorio para descargar el update
        url=f.readline()
        print(url)
        #Aquí comienza el auto update
        try:
            fetch=requests.get(url)
            if(fetch):
                a=True
        except:
            print("Update repository not found")
            a=False

        if(a):
            #print("Auto Update")
            #if(not path):
            #    path = "./"
            #updatePath = path + "UPDATE/"
            updatePath="/home/applica/THORBELL/"
            print(updatePath)
            command = "python3 -m pip install --upgrade git+" + url + "@stable -t " + updatePath 
            response=subprocess.run(command,capture_output=True,text=True,shell=True)
            print(response)
            #if(response.stderr):
            #    print("ERROR: "+response.stderr)