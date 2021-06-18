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
from Ppuerta import Ui_form

class PuertaWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(PuertaWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("LED")

        try:
            #Obtiene el "status" general
            response = requests.get(f"{main.localhost}/status").text
            self.status=json.loads(response)
        except:
            #TODO: add a function or routine that checkes whether the microservices process is running, 
            #and reboots it if needed
            self.status= dict()
            pass

        self.tittleGlow.setText(main.texto.get("puertaTittle"))
        self.tittle.setText(main.texto.get("puertaTittle"))

        initialPressDelay=500          #Delay inicial, antes de tomar el "autoRepeat" (en ms)
        autoRepeatDelay=500            #Delay entre incremento cuando se mantiene presionado (en ms)

        self.subirBtn.setAutoRepeat(True)
        self.subirBtn.setAutoRepeatDelay(initialPressDelay)
        self.subirBtn.setAutoRepeatInterval(autoRepeatDelay)
        self.subirBtn.clicked.connect(self.subir_clicked)
        self.subir_1er = False

        self.bajarBtn.setAutoRepeat(True)
        self.bajarBtn.setAutoRepeatDelay(initialPressDelay)
        self.bajarBtn.setAutoRepeatInterval(autoRepeatDelay)
        self.bajarBtn.clicked.connect(self.bajar_clicked)
        self.bajar_1er = False

        self.posTrabajoBtn.clicked.connect(self.posTrabajo_clicked)
        self.cerrarBtn.clicked.connect(self.cerrar_clicked)
        self.abrirBtn.clicked.connect(self.abrir_clicked)
        
        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def subir_clicked(self):
        if(self.subir_1er):             #Si es verdadero, ya había pulsado el botón de subir
            try:
                response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'subir_cont'})
            except:
                pass
        else:                   #Si es falso, es la primera vez que se pulsa el botón de subir
            try:                    #y comienza con una rampa de aceleración
                response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'subir_init'})
            except:
                pass

        if(subirBtn.isDown()):             #si está presionado, revisa si es la primera vez que se presiona
            self.subir_1er=True            #ya no es el primer click
        else:
            self.subir_1er=False            #Si soltó el pulsador, resetea el flag de primer click        
    
    def bajar_clicked(self):
        if(self.bajar_1er):         #Si es verdadero, ya había pulsado el botón de bajar
            try:                        #y continúa subiendo con velocidad constante
                response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'bajar_cont'})
            except:
                pass
        else:                       #si es falso, es la primera evz que se pulsa el botón de bajar
            try:                        #y comienza con una rampa de aceleración
                response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'bajar_init'})
            except:
                pass

    def posTrabajo_clicked(self):
        try:
            response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'trabajo'})
        except:
            pass

    def abrir_clicked(self):
        try:
            response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'abrir'})
        except:
            pass

    def cerrar_clicked(self):
        try:
            response = requests.post(f"{main.localhost}/status",params = {'puerta' : 'cerrar'})
        except:
            pass