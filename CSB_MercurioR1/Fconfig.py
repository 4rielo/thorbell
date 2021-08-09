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

#from CSB_MercurioR1.Pconfig import Ui_form
from Pconfig import Ui_form
from Finfo import InfoWindow
from Flogin import LoginWindow
from Fservicio import ServiceWindow

class ConfigWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONFIG")

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

        try:
            #Obtiene el "status" general
            print("Retrieving available Languages")
            response = requests.get(f"{main.localhost}/language?list").text
            self.availableLanguages=json.loads(response)
            print(self.availableLanguages)
        except:
            self.availableLanguages=""

        for x in self.availableLanguages:
            x=x.replace(".dat","")
            self.LanguageBox.addItem(x)
            if(x == self.status['Idioma']):
                self.LanguageBox.setCurrentText(x)

        try:
            #Obtiene el "status" general
            response = requests.get(f"{main.localhost}/status").text
            self.status=json.loads(response)
        except:
            #TODO: add a function or routine that checkes whether the microservices process is running, 
            #and reboots it if needed
            self.status= dict()
            pass

        self.updateLanguage()

        self.infoLabel.setText("Info")
        #self.infoLabel_Glow.setText("Info")

        if(self.status.get("screenUser")):
            self.loginLabel.setText("Log Out")
        else: 
            self.loginLabel.setText("Log In")

        #self.update_Btn.clicked.connect(self.UpdateFunction)
        self.info_Btn.clicked.connect(self.showInfo)
        self.login_Btn.clicked.connect(self.login)
        self.language_Btn.clicked.connect(self.showLanguages)
        self.LanguageBox.setVisible(False)
        self.language_Btn.setChecked(False)

        self.LanguageBox.currentTextChanged.connect(self.changeLanguage)
        """Checks local version number. """
        """try:
            currentVersion=open(main.globalPath + "/version.txt","r").readline()
        except:
            currentVersion="0.0.0"        
        
        if(currentVersion[-1]=="\n"):
            currentVersion=currentVersion[:-1]
        self.versionLabel.setText("Current: " + currentVersion)"""

        self.turnOff_Btn.clicked.connect(self.servicioWindow)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        self.tittleGlow.setText(self.idioma.get("configTittle"))
        self.tittle.setText(self.idioma.get("configTittle"))
        self.languageLabel.setText(self.idioma.get("idioma"))
        self.turnOffLabel.setText(self.idioma.get("apagar"))

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def showLanguages(self):
        self.LanguageBox.setVisible(self.language_Btn.isChecked())
        #self.languageWindow = LanguageWindow()
        #self.languageWindow.show()

    def changeLanguage(self):
        selectedLanguage=self.LanguageBox.currentText()
        #selectedLanguage += '.dat'
        #print(selectedLanguage)
        self.status['Idioma'] = selectedLanguage
        try:
            response = requests.post(f"{main.localhost}/status", params= {'Idioma': self.status['Idioma']}).text
            print(response)
        except:
            pass
        
        self.updateLanguage()

    def showInfo(self):
        self.infoWindow = InfoWindow()
        self.infoWindow.show()

    def servicioWindow(self):
        #self.servicieWindow = ServiceWindow()
        #self.servicieWindow.show()
        pass

    def login(self):            #Dependiendo de si ya se está logueado o no
        if(self.status.get("screenUser")):                  #Si se está logueado
            self.loginLabel.setText("Log In")
            self.status.update({"screenUser" : ""})
            try:
                response = requests.post(json.dumps(f"{main.localhost}/status", params = {"screenUser" : self.status.get('screenUser')}))
            except:
                #TODO: add a function or routine that checks whether the microservices process is running, 
                #and reboots it if needed
                pass

        else: 
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
                    