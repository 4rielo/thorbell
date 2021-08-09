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
from PpruebasControl import Ui_form


class PruebasControlWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(PruebasControlWindow, self).__init__()
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

        self.tomacorrientes_Btn.setText("Tomacorrientes")
        self.motorBajadaOnOff_Btn.setText("MotorBajada")
        self.motorSubidaOnOff_Btn.setText("MotorSubida")

        self.velFlujoLbl.setText("Velocidad de Flujo")
        self.flujoBajadaLbl.setText("Bajada")
        self.flujoSubidaLbl.setText("Subida")

        self.presionFiltrosLbl.setText("Presion en Filtros")
        self.presionBajadaLbl.setText("Bajada")
        self.presionSubidaLbl.setText("Subida")

        self.flujoBajadaValue.setText("0.00")
        self.flujoSubidaValue.setText("0.00")
        self.presionBajadaValue.setText("0")
        self.presionSubidaValue.setText("0")

        self.MotorSubidaValue.setText("50%")
        self.MotorBajadaValue.setText("50%")

    def pantallaAjustes(self):
        self.ajustesWindow = AjustesWindow()
        self.ajustesWindow.show()

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()
