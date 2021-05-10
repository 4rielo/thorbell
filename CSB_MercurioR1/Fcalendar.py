#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import main
import json
from datetime import datetime, date

from Pcalendar import Ui_form

class CalendarWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(CalendarWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONFIG")

        print("Open: " + main.texto.get("configTittle"))

        calendar = f"{main.texto.get('calendarTittle')}"
        self.tittleGlow.setText(calendar)
        self.tittle.setText(calendar)

        self.inicioLbl.setText(f"{main.texto.get('calendarInit')}")
        self.endLbl.setText(f"{main.texto.get('calendarEnd')}")
        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

        today=date.today()
        today = PySide2.QtCore.QDate(today.year, today.month, today.day)
        self.initDateEdit.setDate(today)
        self.endDateEdit.setDate(today)

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()