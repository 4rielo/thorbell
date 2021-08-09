#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import main
import json
import requests
import subprocess    

#from CSB_MercurioR1.Pconfig import Ui_form
from Pactualizar import Ui_form


class ActualizarWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(ActualizarWindow, self).__init__()
        self.setupUi(self)
        #self.setWindowTitle("CONFIG")

        try:
            #Obtiene el "status" general
            response = requests.get(f"{main.localhost}/status").text
            self.status=json.loads(response)
        except:
            #TODO: add a function or routine that checkes whether the microservices process is running, 
            #and reboots it if needed
            self.status= {'WARNINGS':[]}
            print(self.status)
            pass

        self.updateLanguage()

        """Checks local version number. """
        try:
            self.currentVersion=open(main.globalPath + "/version.txt","r").readline()
        except:
            self.currentVersion="0.0.0"        
        
        if(self.currentVersion[-1]=="\n"):
            self.currentVersion=self.currentVersion[:-1]
        self.currentVersionValue.setText(self.currentVersion)

        self.checkRemoteVersion()

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        self.tittleGlow.setText(f"Actualizar")#self.idioma.get("configTittle"))
        self.tittle.setText(f"Actualizar")#self.idioma.get("configTittle"))

        self.actualizar_Btn.setText("Actualizar\ny Reiniciar")

        self.currentVersionLbl.setText("Versión Actual:")

        self.remoteVersionLbl.setText("Versión en servidor:")


    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def checkRemoteVersion(self):
        path=__file__
        path=path.replace("Factualizar.py","")
        if(not path):
            path = "./"

        with open(path+"repo.txt","r") as f:                 #obtiene la dirección del repositorio para descargar el update
            url=f.readline()
        #print(url)

        #Obtiene la dirección del archivo de versión
        with open(path+"versionURL.txt","r") as f:
            urlVersion=f.readline()

        #Aquí comienza el auto update
        try:
            fetch=requests.get(url)                 #Chekea tener conexión a internet, para ver si puede acceder al repositorio
            if(fetch):
                a=True                              #Conexión extablecida, pudo acceder al repo
                #self.updateLabel.setText("Repositorio externo\nencontrado")
        except:
            print("Update repository not found")            #No pudo acceder al repo
            self.remoteVersionValue.setText("Repositorio externo NO encontrado")
            a=False

        if(a):
            #print("Auto Update")
            if(not path):
                path = "./"
            #updatePath = path + "UPDATE/"
            self.updatePath="/home/applica/update/UPDATE/"
            #print(updatePath)
            command="rm -rf /home/applica/update/UPDATE"
            subprocess.run(command,shell=True)
            #command = "python3 -m pip install --upgrade git+" + url + "@stable -t " + updatePath 
            """Download file "version.txt" to update path, and open it to check on latest version number """
            command = f"wget -P {self.updatePath} -c {urlVersion}" 
            response=subprocess.run(command,capture_output=True,text=True,shell=True)
            #print(response)
            #print(updatePath+"version.txt")
            #Open file and read it's content.
            with open(self.updatePath+"version.txt","r") as f: 
                f = f.readline()
                if(f[-1]=="\n"):
                    f=f[:-1]
                new = f.split(".")
            self.remoteVersionValue.setText(f)
            self.newVersion=(int(new[0]),int(new[1]),int(new[2]))
            
    def UpdateFunction(self):

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
        #self.updateLabel.setText(f"Versión remota: {new}\nLocal: {currentVersion}")

        update=False
        """If "Stable" version from repository is greater than current version, performs update"""
        if(self.newVersion[0]>cVersion[0]):
            update=True
        elif(self.newVersion[1]>cVersion[1]):
            update=True
        elif(self.newVersion[2]>cVersion[2]):
            update=True
        
        if(update):
            #self.updateLabel.setText("Comienza la descarga")
            """Download stable version from git"""
            command="rm -rf /home/applica/update/UPDATE"
            subprocess.run(command,shell=True)
            #time.sleep(2)
            command = f"git clone {url} {updatePath} -b stable"
            response=subprocess.run(command,capture_output=True,text=True,shell=True)
            if(not response.returncode): # stdout.endswith("done.")):          #response from git clone is "Done"
                #self.updateLabel.setText("Descarga completada.\nEn momentos se reiniciará para completar actualización")
                time.sleep(5)
                command="reboot"
                subprocess.run(command,shell=True)