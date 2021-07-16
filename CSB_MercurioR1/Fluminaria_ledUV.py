#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import json
import requests
import datetime

import main         #to read the lightOnOff status

#from CSB_MercurioR1.Pconfig import Ui_form
from Pluminaria_ledUV import Ui_form

class UVWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(UVWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("LED")

        initialPressDelay=500          #Delay inicial, antes de tomar el "autoRepeat" (en ms)
        autoRepeatDelay=50            #Delay entre incremento cuando se mantiene presionado (en ms)
        
        try:
            #Obtiene el "status" general
            response = requests.get(f"{main.localhost}/status").text
            self.status=json.loads(response)
        except:
            #TODO: add a function or routine that checkes whether the microservices process is running, 
            #and reboots it if needed
            self.status= dict()
            print("Error getting status")
            pass

        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto
        
        main.UV_Timer = datetime.time.fromisoformat(self.status.get("UV_Timer"))
        #main.UV_Timer = datetime.timedelta(main.UV_Timer)
        main.UV_TimerEnable = self.status.get("UV_TimerEnable")

        self.UV_Timer.setTime(PySide2.QtCore.QTime(main.UV_Timer.hour, main.UV_Timer.minute))

        self.OnOffButton.setChecked(self.status.get('UV_Light'))
        self.timerBtn.setChecked(self.status.get('UV_TimerEnable'))

        self.tittleGlow.setText(self.idioma.get("UVTittle"))
        self.tittle.setText(self.idioma.get("UVTittle"))

        self.upButton.setAutoRepeat(True)
        self.upButton.setAutoRepeatDelay(initialPressDelay)
        self.upButton.setAutoRepeatInterval(autoRepeatDelay)
        self.upButton.clicked.connect(self.UpBtn_clicked)

        self.downButton.setAutoRepeat(True)
        self.downButton.setAutoRepeatDelay(initialPressDelay)
        self.downButton.setAutoRepeatInterval(autoRepeatDelay)
        self.downButton.clicked.connect(self.DownBtn_clicked)
        
        self.OnOffButton.clicked.connect(self.OnOff_clicked)
        self.timerBtn.clicked.connect(self.TimerOnOf_clicked)
        
        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def DownBtn_clicked(self):
        #print("Clicked DOWN") 
        #Si el tiempo actual del timer es mayor que 00:00
        if(self.UV_Timer.time()>PySide2.QtCore.QTime(0, 0)):
            #Decrementa 1 minuto
            self.UV_Timer.setTime(self.UV_Timer.time().addSecs(-60))
            self.UV_TimerGlow.setTime(self.UV_Timer.time())
        
        if(not self.downButton.isDown()):           #Soltó el pulsador, actualiza el valor del temporizador en microservicios
            try:
                main.UV_Timer=main.UV_Timer.replace(
                    hour = self.UV_Timer.time().hour(),
                    minute = self.UV_Timer.time().minute()
                )
                response = requests.post(f"{main.localhost}/status",params= {"UV_Timer" : main.UV_Timer.__str__()})
            except:
                #TODO: handling microprocess request failure
                pass

    def UpBtn_clicked(self):
        #print("Clicked UP")
        #print(self.UV_Timer.time())
        #Si el tiempo actual del timer es menor que 99:59
        if(self.UV_Timer.time()<PySide2.QtCore.QTime(23, 59)):
            #incrementa 1 minuto
            self.UV_Timer.setTime(self.UV_Timer.time().addSecs(60))
            self.UV_TimerGlow.setTime(self.UV_Timer.time())
        if(not self.upButton.isDown()):           #Soltó el pulsador, actualiza el valor del temporizador en microservicios
            try:
                main.UV_Timer=main.UV_Timer.replace(
                    hour = self.UV_Timer.time().hour(),
                    minute = self.UV_Timer.time().minute()
                )
                response = requests.post(f"{main.localhost}/status",params= {"UV_Timer" : main.UV_Timer.__str__()})
            except:
                #TODO: handling microprocess request failure
                pass

    def OnOff_clicked(self):
        main.uvOnOff=self.OnOffButton.isChecked()

        #Changes Status data
        try:
            response = requests.post(f"{main.localhost}/status",params= {"UV_Light" : main.uvOnOff})
        except:
            #TODO: handling microprocess request failure
            pass
        
       
    def TimerOnOf_clicked(self):
        main.UV_TimerEnable=self.timerBtn.isChecked()

        #Changes Status data
        try:
            response = requests.post(f"{main.localhost}/status",params= {"UV_TimerEnable" : main.UV_TimerEnable})
        except:
            #TODO: handling microprocess request failure
            pass