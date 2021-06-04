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
        
        self.OnOffButton.setChecked(main.lightOnOff)          
        self.dialChange(main.lightPercent)

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
            #Changes Status data
            """with open(main.statusFile) as f:
                data=json.load(f)                               #and loads json object
            data.update( { "LEDPWM": main.lightPercent } )           #updates LED status
            with open(main.statusFile, "w") as f:               #And saves it to status File
                json.dump(data,f)                               #as an JSON object"""

        if(not self.downButton.isDown()):                     #Si soltó el pulsador
            #Guardo el valor en memoria
            response = requests.post(main.localhost,params= {"LEDPWM" : main.lightPercent})
            print(response.text)

    def UpBtn_clicked(self):
        #print("Clicked UP")
        if(main.lightPercent<100):
            main.lightPercent +=1
            self.dialChange(main.lightPercent)
            #Changes Status data
            """with open(main.statusFile) as f:
                data=json.load(f)                               #and loads json object
            data.update( { "LEDPWM": main.lightPercent } )           #updates LED status
            with open(main.statusFile, "w") as f:               #And saves it to status File
                json.dump(data,f)                               #as an JSON object"""

        if(not self.upButton.isDown()):                     #Si soltó el pulsador
            #Guardo el valor en memoria
            response = requests.post(main.localhost,params= {"LEDPWM" : main.lightPercent})
            print(response.text)


    def OnOff_clicked(self):
        print(f"On Off -> {self.OnOffButton.isChecked()}")
        main.lightOnOff=self.OnOffButton.isChecked()
        response = requests.post(main.localhost,params= {"LED_Light" : main.lightOnOff})
        """#Changes Status data
        with open(main.statusFile) as f:
            data=json.load(f)                               #and loads json object
        data.update( { "LED": main.lightOnOff } )           #updates LED status
        with open(main.statusFile, "w") as f:               #And saves it to status File
            json.dump(data,f)                               #as an JSON object"""

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