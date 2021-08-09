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
from PextremosOp import Ui_form


class extremosOpWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self, motor=1):
        super(extremosOpWindow, self).__init__()
        self.setupUi(self)
        #self.setWindowTitle("CONFIG")

        self.motor = motor

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

        self.velMinRadioBox.setChecked(True)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        self.tittleGlow.setText(f"Extremos de Operación\nMotor {self.motor}")#self.idioma.get("configTittle"))
        self.tittle.setText(f"Extremos de Operación\nMotor {self.motor}")#self.idioma.get("configTittle"))

        self.motorOnOff_Btn.setText(f"Motor {self.motor}")

        self.guardar_Btn.setText("Guardar")

        self.pruebaRegLbl.setText("Prueba de Regulación")

        self.velMaxLbl.setText("Vel. máxima")
        self.velMinLbl.setText("Vel. mínima")

        self.velMinValue.setText("25%")
        self.velMaxValue.setText("100%")
        self.motorValue.setText("50%")

    def pantallaAjustes(self):
        self.ajustesWindow = AjustesWindow()
        self.ajustesWindow.show()

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()