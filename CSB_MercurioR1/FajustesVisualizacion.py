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
from PajustesVisualizacion import Ui_form


class AjustesVisualizacionWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(AjustesVisualizacionWindow, self).__init__()
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

        self.constanteBajadaRadioBox.setChecked(True)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        self.tittleGlow.setText("Ajustes de Visualización")#self.idioma.get("configTittle"))
        self.tittle.setText("Ajustes de Visualización")#self.idioma.get("configTittle"))

        self.motorSubidaOnOff_Btn.setText("MotorSubida")
        self.motorBajadaOnOff_Btn.setText("MotorBajada")
        self.guardar_Btn.setText("Guardar")

        self.bajadaTittle.setText("Bajada")
        self.constanteBajadaLbl.setText("Constante")
        self.constanteBajadaValue.setText("0.00")

        self.velBajadaLbl.setText("Velocidad")
        self.velBajadaValue.setText("0.00")

        self.salidaTittle.setText("Salida")
        self.constanteSalidaLbl.setText("Constante")
        self.constanteSalidaValue.setText("0.00")

        self.velSalidaLbl.setText("Velocidad")
        self.velSalidaValue.setText("0.00")

        self.MotorSubidaValue.setText("50%")
        self.MotorBajadaValue.setText("50%")

    def pantallaAjustes(self):
        self.ajustesWindow = AjustesWindow()
        self.ajustesWindow.show()

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()
