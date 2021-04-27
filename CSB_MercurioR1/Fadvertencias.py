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
from Padvertencias import Ui_form

class AdvertenciaWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(AdvertenciaWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Advertencia")

        initialPressDelay=500          #Delay inicial, antes de tomar el "autoRepeat" (en ms)
        autoRepeatDelay=50            #Delay entre incremento cuando se mantiene presionado (en ms)
        with open(main.statusFile) as f:
            data=json.load(f)                               #and loads json object

        #TODO read warnings from status.dat and add labels and icons to "advertencias"
        advertencias=data.get("WARNINGS")
        cantidad = len(advertencias)            #Cantidad de advertencias a mostrar
        self.listLabels = list()
        self.listLabels2 = list()
        self.listIcons = list()
        self.listEffects = list()

        vertical=360
        separacion = 50

        self.Effect=QtWidgets.QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.label_style=f"""
            QLabel{{
                font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                font-size: 23apx;
                color: white;
            }}
        """

        self.tittleGlow.setText(main.texto.get("warningTittle"))
        self.tittle.setText(main.texto.get("warningTittle"))

        for idx, a in enumerate(advertencias):
            self.listIcons.append(PySide2.QtWidgets.QFrame(self.BACKGROUND))
            self.listIcons[idx].setGeometry(PySide2.QtCore.QRect(157, vertical + idx * separacion, 46, 47))
            self.listIcons[idx].setFrameShape(PySide2.QtWidgets.QFrame.NoFrame)
            self.listIcons[idx].setFrameShadow(PySide2.QtWidgets.QFrame.Raised)
            Icon_style=f"""
                    QFrame {{
                        background-image: url({main.path}/icons/{a}.png);
                        background-repeat: no-repeat;
                    }}"""
            self.listIcons[idx].setStyleSheet(Icon_style)

            #a=a.replace("_" , " ")
            #a=a.capitalize()
            self.listLabels.append(PySide2.QtWidgets.QLabel(self.BACKGROUND))
            self.listLabels2.append(PySide2.QtWidgets.QLabel(self.BACKGROUND))
            
            #aux=len(a)
            #print("Aux: " + str(aux))
            position=211 #- round(aux/3)

            self.listLabels[idx].setObjectName(main.texto.get(a))
            self.listLabels[idx].setText(main.texto.get(a))
            self.listLabels[idx].setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
            self.listLabels[idx].setGeometry(PySide2.QtCore.QRect(position, vertical + 10 + idx * separacion , 200, 26))
            self.listLabels[idx].setStyleSheet(self.label_style)
            self.listLabels[idx].setGraphicsEffect(self.Effect)

            self.listLabels2[idx].setObjectName(main.texto.get(a))
            self.listLabels2[idx].setText(main.texto.get(a))
            self.listLabels2[idx].setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
            self.listLabels2[idx].setGeometry(PySide2.QtCore.QRect(211, vertical + 10 + idx * separacion , 200, 26))
            
            self.listLabels2[idx].raise_()
        
        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    
