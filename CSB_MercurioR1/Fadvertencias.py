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
from Padvertencias import Ui_form

class AdvertenciaWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(AdvertenciaWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Advertencia")

        initialPressDelay=500          #Delay inicial, antes de tomar el "autoRepeat" (en ms)
        autoRepeatDelay=50            #Delay entre incremento cuando se mantiene presionado (en ms)

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
        
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            self.idioma = main.texto
    
        advertencias=self.status.get("WARNINGS")
        cantidad = len(advertencias)            #Cantidad de advertencias a mostrar
        self.listLabels = list()
        self.listLabelsGlow = list()
        self.listIcons = list()
        self.listEffects = list()

        vertical=360
        separacion = 50

        #self.Effect=QtWidgets.QGraphicsBlurEffect()
        #self.Effect.setBlurRadius(10)
        self.label_style=f"""
            QLabel{{
                font-size: 23px;
            }}"""

        self.tittleGlow.setText(self.idioma.get("warningTittle"))
        self.tittle.setText(self.idioma.get("warningTittle"))
        self.tittleGlow.setGraphicsEffect(self.Effect)


        for idx, a in enumerate(advertencias):
            """Por cada item en Advertencias, crea un ícono y su respectiva 
            información, obtenida del archivo de idioma"""

            #Ícono:
            Icon_style=f"""
                    QFrame {{
                        background-image: url({main.path}/icons/{a}.png);
                    }}"""
            self.listIcons.insert(idx, PySide2.QtWidgets.QFrame(self.BACKGROUND))
            self.listIcons[idx].setFixedSize(46, 47)
            self.listIcons[idx].setFrameShape(PySide2.QtWidgets.QFrame.NoFrame)
            #self.listIcons[idx].setFrameShadow(PySide2.QtWidgets.QFrame.Raised)
            self.listIcons[idx].setStyleSheet(Icon_style)

            #Texto descriptivo y su fondo de efecto glow
            self.listLabels.insert(idx, PySide2.QtWidgets.QLabel(self.BACKGROUND))      #Crea la etiqueta
            self.listLabelsGlow.insert(idx, PySide2.QtWidgets.QLabel(self.BACKGROUND))  

            self.listEffects.append(PySide2.QtWidgets.QGraphicsBlurEffect())        #Crea el efecto borroso 
            self.listEffects[idx].setBlurRadius(10)                                 #para la iluminosidad de fondo

            self.listLabels[idx].setText(self.idioma.get(a))     #escribe la etiqueta
            self.listLabelsGlow[idx].setText(self.idioma.get(a))     #y la etiqueta de efecto luminoso
            self.listLabelsGlow[idx].setGraphicsEffect(self.listEffects[idx])     #aplica efecto blur para simular iluminosidad
            self.listLabels[idx].raise_()                       #"levanta" la etiqueta si efecto, para que esté por encima de la borrosa

            self.BtnsLayout.addWidget(self.listIcons[idx], idx, 0)      #Agrega el ícono al layout, row= IDX, columna=0
            self.BtnsLayout.addWidget(self.listLabels[idx], idx, 1)     #Agrega la etiqueta al layout, row= IDX, columna= 1 
            self.BtnsLayout.addWidget(self.listLabelsGlow[idx], idx, 1) #Agrega el efecto de brillo, en la misma posicion que la etiqueta
        
        #print(self.listLabels)
        #print(self.listLabelsGlow)

        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    
