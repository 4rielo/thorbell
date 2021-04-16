#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading


import main         #to read the lightOnOff status

#from CSB_MercurioR1.Pconfig import Ui_form
from Pluminaria_led import Ui_form

class LEDWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(LEDWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("LED")

        self.upButton.clicked.connect(self.increase)
        self.downButton.clicked.connect(self.decrease)

        self.OnOffButton.setChecked(main.lightOnOff)
        self.OnOffButton.clicked.connect(self.OnOff)

        self.backButton.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

#Funcion para decrementar el porcentaje de iluminación
    def decrease(self):
        firstKey=1
        while(self.downButton.isChecked()):
            if(main.lightPercent>0):
                main.lightPercent -= 1
            self.percentage_label.setText(str(main.lightPercent) + "%")
            if(firstKey):           
                time.sleep(0.8)
                firstKey=0
            else:
                time.sleep(0.1)

#Función para incrementar el porcentaje de iluminación
    def increase(self):
        firstKey=1
        while(self.upButton.isChecked()):
            if(main.lightPercent<100):
                main.lightPercent += 1
            self.percentage_label.setText(str(main.lightPercent) + "%")
            if(firstKey):
                time.sleep(0.8)
                firstKey=0
            else:
                time.sleep(0.1)

    def OnOff(self):
        main.lightOnOff=self.luz_Btn.isChecked()