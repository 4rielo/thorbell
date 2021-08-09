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
from Pservicio import Ui_form
from Fajustes import AjustesWindow
from FpruebasControl import PruebasControlWindow

class ServiceWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(ServiceWindow, self).__init__()
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

        self.updateLanguage()

        self.ajustes_Btn.clicked.connect(self.pantallaAjustes)
        self.pruebas_Btn.clicked.connect(self.pantallaPruebas)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        self.tittleGlow.setText("Servicio")#self.idioma.get("configTittle"))
        self.tittle.setText("Servicio")#self.idioma.get("configTittle"))

        self.reparaciones_Btn.setText("Reparaciones")
        self.ajustes_Btn.setText("Ajustes")
        self.pruebas_Btn.setText("Pruebas")

    def pantallaAjustes(self):
        self.ajustesWindow = AjustesWindow()
        self.ajustesWindow.show()

    def pantallaPruebas(self):
        self.pruebasWindow = PruebasControlWindow()
        self.pruebasWindow.show()

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()
