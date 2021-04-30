#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import main
import json

from Pinfo import Ui_form

class InfoWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CONFIG")

        print("Open: " + main.texto.get("configTittle"))
        """Checks local version number. """
        try:
            v=open(main.globalPath + "/version.txt","r")
            currentVersion=v.readline()
            v.close()
        except:
            currentVersion="0.0.0"        
        if(currentVersion[-1]=="\n"):
            currentVersion=currentVersion[:-1]

        #with open(main.statusFile) as f:
        #    status=json.load(f)

        with open(main.infoFile) as d:
            info=json.load(d)

        #currentVersion=info.get("currentVersion")
        versionDate=info.get("versionDate")
        Version=f"Version: {currentVersion}\nFecha: {versionDate}"

        self.versionLabel.setText(Version)
       
        postVenta = f"""{main.texto.get("postVenta")}\n\n{info.get("postVentaEmail")}\n{info.get("website")}"""
        self.postVentaGlow.setText(postVenta)
        self.postVenta.setText(postVenta)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()