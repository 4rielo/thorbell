#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import main
import json

#from CSB_MercurioR1.Pconfig import Ui_form
from Pconfig import Ui_form
from Finfo import InfoWindow
from Flogin import LoginWindow

class ConfigWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONFIG")

        print("Open: " + main.texto.get("configTittle"))

        self.tittleGlow.setText(main.texto.get("configTittle"))
        self.tittle.setText(main.texto.get("configTittle"))

        self.usbLabel.setText("USB")
        self.infoLabel.setText("Info")
        self.infoLabel_Glow.setText("Info")

        with open(main.statusFile) as f:
            status=json.load(f)
        if(status.get("screenUser")):
            self.loginLabel.setText("Log Out")
        else: 
            self.loginLabel.setText("Log In")

        self.update_Btn.clicked.connect(self.UpdateFunction)
        self.info_Btn.clicked.connect(self.showInfo)
        self.login_Btn.clicked.connect(self.login)

        """Checks local version number. """
        try:
            currentVersion=open(main.globalPath + "/version.txt","r").readline()
        except:
            currentVersion="0.0.0"        
        
        if(currentVersion[-1]=="\n"):
            currentVersion=currentVersion[:-1]
        self.versionLabel.setText("Current: " + currentVersion)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def showInfo(self):
        self.infoWindow = InfoWindow()
        self.infoWindow.show()

    def login(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.show()

    def UpdateFunction(self):
        import subprocess
        import requests

        path=__file__
        path=path.replace("Fconfig.py","")

        with open(path+"repo.txt","r") as f:                 #obtiene la dirección del repositorio para descargar el update
            url=f.readline()
        print(url)

        #Obtiene la dirección del archivo de versión
        with open(path+"versionURL.txt","r") as f:
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
            command="rm -rf /home/applica/update/UPDATE"
            subprocess.run(command,shell=True)
            #command = "python3 -m pip install --upgrade git+" + url + "@stable -t " + updatePath 
            """Download file "version.txt" to update path, and open it to check on latest version number """
            command = "wget -P " + updatePath + " -c " + urlVersion #https://raw.githubusercontent.com/4rielo/thorbell/stable/version.txt
            response=subprocess.run(command,capture_output=True,text=True,shell=True)
            print(response)
            #print(updatePath+"version.txt")
            #Open file and read it's content.
            with open(updatePath+"version.txt","r") as f: 
                f = f.readline()
                if(f[-1]=="\n"):
                    f=f[:-1]
                new = f.split(".")
            
            newVersion=(int(new[0]),int(new[1]),int(new[2]))

            """Checks local version number. """
            localPath = "/home/applica/THORBELL/"
            try:
                f=open(localPath + "version.txt","r")
                currentVersion=f.readline()
                f.close()
            except:
                currentVersion="0.0.0"
            if(currentVersion[-1]=="\n"):
                currentVersion=currentVersion[:-1]
            curr=currentVersion.split(".")
            cVersion=(int(curr[0]),int(curr[1]),int(curr[2]))
            self.updateLabel.setText(f"Versión remota: {new}\nLocal: {currentVersion}")

            update=False
            """If "Stable" version from repository is greater than current version, performs update"""
            if(newVersion[0]>cVersion[0]):
                update=True
            elif(newVersion[1]>cVersion[1]):
                update=True
            elif(newVersion[2]>cVersion[2]):
                update=True
            
            if(update):
                self.updateLabel.setText("Comienza la descarga")
                """Download stable version from git"""
                command="rm -rf /home/applica/update/UPDATE"
                subprocess.run(command,shell=True)
                #time.sleep(2)
                command = f"git clone {url} {updatePath} -b stable"
                response=subprocess.run(command,capture_output=True,text=True,shell=True)
                if(not response.returncode): # stdout.endswith("done.")):          #response from git clone is "Done"
                    self.updateLabel.setText("Descarga completada.\nEn momentos se reiniciará para completar actualización")
                    time.sleep(5)
                    command="reboot"
                    subprocess.run(command,shell=True)
                    