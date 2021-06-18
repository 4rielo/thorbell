#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import json
import requests

import main         #to read the lightOnOff status

#from CSB_MercurioR1.Pconfig import Ui_form
from Pluminaria_led import Ui_form

class LEDWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(LEDWindow, self).__init__()
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
            pass

        self.OnOffButton.setChecked(self.status.get('LED_Light'))          
        self.dialChange(self.status.get('LEDPWM'))

        self.tittleGlow.setText(main.texto.get("LEDTittle"))
        self.tittle.setText(main.texto.get("LEDTittle"))

        self.upButton.setAutoRepeat(True)
        self.upButton.setAutoRepeatDelay(initialPressDelay)
        self.upButton.setAutoRepeatInterval(autoRepeatDelay)
        self.upButton.clicked.connect(self.UpBtn_clicked)

        self.downButton.setAutoRepeat(True)
        self.downButton.setAutoRepeatDelay(initialPressDelay)
        self.downButton.setAutoRepeatInterval(autoRepeatDelay)
        self.downButton.clicked.connect(self.DownBtn_clicked)
        
        self.OnOffButton.clicked.connect(self.OnOff_clicked)
        
        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def DownBtn_clicked(self):
        #print("Clicked DOWN")
        if(main.lightPercent>0):
            main.lightPercent -=1
            self.dialChange(main.lightPercent)

        #if(not self.downButton.isDown()):                     #Si soltó el pulsador
        #Guardo el valor en memoria
        try:
            response = requests.post(f"{main.localhost}/status",params= {"LEDPWM" : main.lightPercent})
        except:
            #TODO: handling microprocess request failure
            pass
        #print(response.text)

    def UpBtn_clicked(self):
        #print("Clicked UP") 
        if(main.lightPercent<100):
            main.lightPercent +=1
            self.dialChange(main.lightPercent)

        i#f(not self.upButton.isDown()):                     #Si soltó el pulsador
        #Guardo el valor en memoria
        try:
            response = requests.post(f"{main.localhost}/status",params= {"LEDPWM" : main.lightPercent})
        except:
            #TODO: handling microprocess request failure
            pass
        #print(response.text)


    def OnOff_clicked(self):
        #print(f"On Off -> {self.OnOffButton.isChecked()}")
        main.lightOnOff=self.OnOffButton.isChecked()
        try:
            response = requests.post(f"{main.localhost}/status",params= {"LED_Light" : main.lightOnOff})
        except:
            #TODO: handling microprocess request failure
            pass
        
    def dialChange(self, slider):
        self.percentage_label.setText(str(slider) + " %")
        self.percentage_labelGlow.setText(str(slider) + " %")

        stopValue= (slider)/100
    #       print("Slider value= " + str(stopValue))
        gradient = stopValue-0.05
        if(gradient < 0):
            gradient = 0
            stopValue = 0.05
        if(stopValue>1):
            stopValue=1
        if(gradient>1):
            gradient=1
        progressBar_style=f"""
            QFrame{{
                background-image: url();
                border-radius: 92px;
                background-color: qradialgradient(
                                    spread:pad, 
                                    cx:0.5, 
                                    cy:0.5, 
                                    radius:0.5, 
                                    fx:0.5, 
                                    fy:0.5, 
                                    stop:{gradient} rgba(255, 255, 255, 145),
                                    stop:{stopValue} rgba(255, 255, 255, 0)
                                );
            }}"""
        self.Bar.setStyleSheet(progressBar_style)