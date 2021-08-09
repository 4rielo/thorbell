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
from PajustesMotores import Ui_form
from FextremosOp import extremosOpWindow
from FajustePID import AjustesPIDWindow

class AjusteMotoresWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(AjusteMotoresWindow, self).__init__()
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

        self.extremoOp1_Btn.clicked.connect(self.extremoOp1)
        self.extremoOp2_Btn.clicked.connect(self.extremoOp2)

        self.PID1_Btn.clicked.connect(self.ajustePID1)
        self.PID2_Btn.clicked.connect(self.ajustePID2)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto

        self.tittleGlow.setText("Ajustes de Motores")#self.idioma.get("configTittle"))
        self.tittle.setText("Ajustes de Motores")#self.idioma.get("configTittle"))

        self.PID1_Btn.setText("PID 1")
        self.PID2_Btn.setText("PID 2")

        self.motor1_Btn.setText("Motor 1")
        self.motor2_Btn.setText("Motor 2")

        self.extremoOp1_Btn.setText("Extremos de \nOperacion 1")
        self.extremoOp2_Btn.setText("Extremos de \nOperacion 2")

    def extremoOp1(self):
        self.extremoOp = extremosOpWindow(1)
        self.extremoOp.show()

    def extremoOp2(self):
        self.extremoOp = extremosOpWindow(2)
        self.extremoOp.show()

    def editAjustesVisualizacion(self):
        self.ajustesWindow = AjustesVisualizacionWindow()
        self.ajustesWindow.show()

    def ajustePID1(self):
        self.ajustePIDWindow = AjustesPIDWindow(1)
        self.ajustePIDWindow.show()

    def ajustePID2(self):
        self.ajustePIDWindow = AjustesPIDWindow(2)
        self.ajustePIDWindow.show()

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()
