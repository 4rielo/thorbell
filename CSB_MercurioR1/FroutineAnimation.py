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
from ProutineAnimation import Ui_form


class RoutineAnimationWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(RoutineAnimationWindow, self).__init__()
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
            response = requests.get(f"{main.localhost}/status").text
            self.status=json.loads(response)
        except:
            #TODO: add a function or routine that checkes whether the microservices process is running, 
            #and reboots it if needed
            self.status= dict()
            pass

        self.updateLanguage()
        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)

        self.animation.setMovie(self.movie)
        self.movie.start()

        self.TimingTimer.timeout.connect(self.goBack)
        self.TimingTimer.start()

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        #self.tittleGlow.setText(self.idioma.get("configTittle"))
        #self.tittle.setText(self.idioma.get("configTittle"))

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    