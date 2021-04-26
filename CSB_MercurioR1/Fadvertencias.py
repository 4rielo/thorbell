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

            a=a.replace("_" , " ")
            a=a.capitalize()
            self.listLabels.append(PySide2.QtWidgets.QLabel(self.BACKGROUND))
            self.listLabels2.append(PySide2.QtWidgets.QLabel(self.BACKGROUND))

            if(idx<1):
                self.listLabels[idx].setObjectName(a)
                self.listLabels[idx].setText(a)
                self.listLabels[idx].setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
                self.listLabels[idx].setGeometry(PySide2.QtCore.QRect(208, vertical + 5 + idx * separacion , 300, 26))

            self.listLabels2[idx].setObjectName(a)
            self.listLabels2[idx].setText(a)
            self.listLabels2[idx].setAttribute(PySide2.QtCore.Qt.WA_TranslucentBackground, True)
            self.listLabels2[idx].setGeometry(PySide2.QtCore.QRect(211, vertical + 5 + idx * separacion , 300, 26))
            label_style=f"""
                QLabel{{
                    font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                    font-size: 23apx;
                    color: white;
                }}
            """
            if(idx<1):
                self.listLabels[idx].setStyleSheet(label_style)
                self.listEffects=QtWidgets.QGraphicsBlurEffect()
                self.listEffects.setBlurRadius(10)
                self.listLabels[idx].setGraphicsEffect(self.listEffects)
            self.listLabels2[idx].raise_()
        
        self.backButton.clicked.connect(self.goBack_clicked)
        
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)

    def goBack_clicked(self):                   #Function to go back to previous menu (close this window)
        self.close()

    
