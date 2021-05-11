#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import json

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
        
        with open(main.statusFile) as fp:
            status=json.load(fp)
        
        main.UV_Timer=status.get("UV_Timer")
        main.UV_TimerEnable=status.get("UV_TimerEnable")
        self.UV_Timer.setTime(PySide2.QtCore.QTime(0, 10))

        self.OnOffButton.setChecked(main.lightOnOff)          

        self.tittleGlow.setText(main.texto.get("UVTittle"))
        self.tittle.setText(main.texto.get("UVTittle"))

        self.upButton.setAutoRepeat(True)
        self.upButton.setAutoRepeatDelay(initialPressDelay)
        self.upButton.setAutoRepeatInterval(autoRepeatDelay)
        self.upButton.clicked.connect(self.UpBtn_clicked)

        self.downButton.setAutoRepeat(True)
        self.downButton.setAutoRepeatDelay(initialPressDelay)
        self.downButton.setAutoRepeatInterval(autoRepeatDelay)
        self.downButton.pressed.connect(self.DownBtn_clicked)
        
        self.OnOffButton.clicked.connect(self.OnOff_clicked)
        
        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def DownBtn_clicked(self):
        print("Clicked DOWN") 
        #Si el tiempo actual del timer es mayor que 00:00
        if(self.UV_Timer.time()>PySide2.QtCore.QTime(0, 0)):
            #Decrementa 1 minuto
            self.UV_Timer.setTime(self.UV_Timer.time().addSecs(-60))
            self.UV_TimerGlow.setTime(self.UV_Timer.time())
            #Changes Status data
            """with open(main.statusFile) as f:
                data=json.load(f)                               #and loads json object
            data.update( { "UV_Timer": main.UV_Timer } )           #updates LED status
            with open(main.statusFile, "w") as f:               #And saves it to status File
                json.dump(data,f)                               #as an JSON object"""

    def UpBtn_clicked(self):
        print("Clicked UP")
        #print(self.UV_Timer.time())
        #Si el tiempo actual del timer es menor que 99:59
        if(self.UV_Timer.time()<PySide2.QtCore.QTime(23, 59)):
            #incrementa 1 minuto
            self.UV_Timer.setTime(self.UV_Timer.time().addSecs(60))
            self.UV_TimerGlow.setTime(self.UV_Timer.time())
            """#Changes Status data
            with open(main.statusFile) as f:
                data=json.load(f)                               #and loads json object
            data.update( { "UV_Timer": main.UV_Timer } )           #updates LED status
            with open(main.statusFile, "w") as f:               #And saves it to status File
                json.dump(data,f)                               #as an JSON object"""

    def OnOff_clicked(self):
        main.UV_TimerEnable=self.OnOffButton.isChecked()

        #Changes Status data
        with open(main.statusFile) as f:
            data=json.load(f)                               #and loads json object
        data.update( { "UV_TimerEnable": main.UV_TimerEnable } )           #updates LED status
        with open(main.statusFile, "w") as f:               #And saves it to status File
            json.dump(data,f)                               #as an JSON object
