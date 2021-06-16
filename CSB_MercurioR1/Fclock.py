#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import subprocess
import requests
import json
from datetime import datetime, date

import main
from Pclock import Ui_form

class ClockWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(ClockWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CLOCK")
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 
        
        #Título de la pantalla de calendario
        calendar = f"{main.texto.get('clockTittle')}"
        self.tittleGlow.setText(calendar)
        self.tittle.setText(calendar)

        #Etiquetas de inicio y fin
        self.horaActualLbl.setText(f"{main.texto.get('horaActual')}")
        self.fechaActualLbl.setText(f"{main.texto.get('fechaActual')}")
        
        #*****************Asignación de funciones según botones

        #botón de salir
        self.return_Btn.clicked.connect(self.goBack)

        #Botones de fecha y hora de inicio
        self.horaPlusBtn.clicked.connect(self.increaseHora)
        self.horaPlusBtn.setAutoRepeat(True)
        self.horaPlusBtn.setAutoRepeatDelay(500)
        self.horaPlusBtn.setAutoRepeatInterval(100)

        self.GMTPlusBtn.clicked.connect(self.increaseGMT)
        self.GMTPlusBtn.setAutoRepeat(True)
        self.GMTPlusBtn.setAutoRepeatDelay(500)
        self.GMTPlusBtn.setAutoRepeatInterval(100)

        self.horaMinusBtn.clicked.connect(self.decreaseHora)
        self.horaMinusBtn.setAutoRepeat(True)
        self.horaMinusBtn.setAutoRepeatDelay(500)
        self.horaMinusBtn.setAutoRepeatInterval(100)

        self.GMTMinusBtn.clicked.connect(self.decreaseGMT)
        self.GMTMinusBtn.setAutoRepeat(True)
        self.GMTMinusBtn.setAutoRepeatDelay(500)
        self.GMTMinusBtn.setAutoRepeatInterval(100)

        self.fechaPlusBtn.clicked.connect(self.increaseFecha)
        self.fechaPlusBtn.setAutoRepeat(True)
        self.fechaPlusBtn.setAutoRepeatDelay(500)
        self.fechaPlusBtn.setAutoRepeatInterval(100)
        
        self.fechaMinusBtn.clicked.connect(self.decreaseFecha)
        self.fechaMinusBtn.setAutoRepeat(True)
        self.fechaMinusBtn.setAutoRepeatDelay(500)
        self.fechaMinusBtn.setAutoRepeatInterval(100)

        #Modificación de fechas y hora de inicio y fin - Actualización del valor
        self.horaEdit.timeChanged.connect(self.updateHora)
        self.gmtEdit.valueChanged.connect(self.updateHora)
        self.fechaEdit.dateChanged.connect(self.updateFecha)

        #Mostrar fecha y hora actual
        try:
            #Obtiene el "status" general
            currentTimeDate = requests.get(f"{main.localhost}/status", params = "time").text
            currentTimeDate=datetime.fromisoformat(currentTimeDate)
            #Actualiza hora y fecha
            
            gmtValue = requests.get(f"{main.localhost}/status",params = 'GMT').text
            self.gmtEdit.setValue(gmtValue.value())

            """self.today = currentTimeDate.today()
            self.now = currentTimeDate.now()"""
            
        except:
            #TODO: add a function or routine that checks whether the microservices process is running, 
            #and reboots it if needed
            currentTimeDate=datetime.now()
            """self.today=date.today()         #Obtiene la fecha de hoy
            self.now=datetime.now()"""
            pass
        
        todayQt = PySide2.QtCore.QDate(currentTimeDate.year, currentTimeDate.month, currentTimeDate.day)
        hourQt = PySide2.QtCore.QTime(currentTimeDate.hour, currentTimeDate.minute,0)

        self.horaEdit.setTime(hourQt)
        self.fechaEdit.setDate(todayQt)
        

    #***************************************************************

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def increaseHora(self):
        self.horaEdit.setTime(self.horaEdit.time().addSecs(60))      #Incremento la hora en un minuto

    def decreaseHora(self):
        self.horaEdit.setTime(self.horaEdit.time().addSecs(-60))      #Decremento la hora en un minuto

    def increaseGMT(self):
        self.gmtEdit.setValue(self.gmtEdit.value()+1)

    def decreaseGMT(self):
        self.gmtEdit.setValue(self.gmtEdit.value()-1)

    def increaseFecha(self):
        self.fechaEdit.setDate(self.fechaEdit.date().addDays(1))

    def decreaseFecha(self):
        self.fechaEdit.setDate(self.fechaEdit.date().addDays(-1))

    def updateHora(self):
        """fecha = self.fechaEdit.date()
        fecha = f"{fecha.year}-{fecha.month}-{fecha.day}"
        hora = f"{self.horaEdit.hour}:{self.horaEdit.minute}:{self.horaEdit.seconds}"""
        pass

        """command = f"timedatectl set-time '{fecha} {hora}'"
        response = subprocess.run(command, capture_output=True,text=True,shell=True)
        print(response)"""

    def updateFecha(self):
        #command = f"timedatectl set-time '{self.fechaEdit.year}-{self.fechaEdit.month}-{self.fechaEdit.day} {self.horaEdit.hour}:{self.horaEdit.minute}:{self.horaEdit.seconds}'"
        #response = subprocess.run(command, shell=True)
        pass