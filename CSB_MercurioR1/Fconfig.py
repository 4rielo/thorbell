#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading

#from CSB_MercurioR1.Pconfig import Ui_form
from Pconfig import Ui_form

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
        path=path.replace("Fconfig.py","")

        f=open(path+"repo.txt","r")                 #obtiene la dirección del repositorio para descargar el update
        url=f.readline()
        print(url)

        #Obtiene la dirección del archivo de versión
        f=open(path+"versionURL.txt","r")
        urlVersion=f.readline()

        #Aquí comienza el auto update
        try:
            fetch=requests.get(url)                 #Chekea tener conexión a internet, para ver si puede acceder al repositorio
            if(fetch):
                a=True                              #Conexión extablecida, pudo acceder al repo
                self.updateLabel.setText("Repositorio externo\nencontrado")
        except:
            print("Update repository not found")            #No pudo acceder al repo
            self.updateLabel.setText("Repositorio externo\nNO encontrado")
            a=False

        if(a):

            #print("Auto Update")
            if(not path):
                path = "./"
            #updatePath = path + "UPDATE/"
            updatePath="/home/applica/update/UPDATE/"
            print(updatePath)
            #command = "python3 -m pip install --upgrade git+" + url + "@stable -t " + updatePath 
            """Download file "version.txt" to update path, and open it to check on latest version number """
            command = "wget -P " + updatePath + " -c " + urlVersion #https://raw.githubusercontent.com/4rielo/thorbell/stable/version.txt
            response=subprocess.run(command,capture_output=True,text=True,shell=True)
            print(response)
            #print(updatePath+"version.txt")
            """Open file and read it's content."""
            f = open(updatePath+"version.txt","r").readline()
            if(f[-1]=="\n"):
                f=f[:-1]

            self.updateLabel.setText("Versión remota: " + f)
            new = f.split(".")
            newVersion=(int(new[0]),int(new[1]),int(new[2]))

            """Checks local version number. """
            localPath = "/home/applica/THORBELL/"
            currentVersion=open(localPath + "version.txt","r").readline()
            if(currentVersion[-1]=="\n"):
                currentVersion=currentVersion[:-1]
            curr=currentVersion.split(".")
            cVersion=(int(curr[0]),int(curr[1]),int(curr[2]))

            update=False
            """If "Stable" version from repository is greater than current version, performs update"""
            if(newVersion[0]>cVersion[0]):
                update=True
            elif(newVersion[1]>cVersion[1]):
                update=True
            elif(newVersion[2]>cVersion[2]):
                update=True
            
            if(update):
                """Download stable version from git"""
                command="rm -r /home/applica/update/UPDATE"
                subprocess.run(command)
                time.sleep(2)
                self.updateLabel.setText("Comienza la descarga")
                command = "git clone " + url + " " + updatePath + " -b stable"
                response=subprocess.run(command,capture_output=True,text=True,shell=True)
                if(response.stdout.endswith("done.")):          #response from git clone is "Done"
                    self.updateLabel.setText("Descarga completada.\nDebe reiniciar para completar actualización")
                    time.sleep(5)
                    command="reboot"
                    subprocess.run(command,shell=True)
                    