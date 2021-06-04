#Fconfig.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import main
import json

from Plogin import Ui_form

class LoginWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("LOGIN")

        self.tittleGlow.setText(main.texto.get("loginTittle"))
        self.tittle.setText(main.texto.get("loginTittle"))

        with open(main.statusFile) as fp:
            self.status=json.load(fp)
        with open(main.usersFile) as us:
            self.users=json.load(us)

        self.currentUser=self.users.get(self.status.get("screenUser"))

        self.currentPass=""
        self.PassLabel.setText(self.currentPass)
        if(self.ShowPassword.isDown()):          #clicked
            self.PassLabel.setEchoMode(PySide2.QtWidgets.QLineEdit.Normal)
        else:
            self.PassLabel.setEchoMode(PySide2.QtWidgets.QLineEdit.Password)

        self.return_Btn.clicked.connect(self.goBack)
        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint)

        for number in range(10):
            self.key[number].pressed.connect(self.keyPressed)

        self.keyAsterix.clicked.connect(self.asterix)
        self.keyNumeral.clicked.connect(self.numeral)
        self.deleteBtn.clicked.connect(self.delete)

        self.ShowPassword.clicked.connect(self.showPassword)

        self.loginBtn.clicked.connect(self.login)
        

    def goBack(self):                   #Function to go back to previous menu (close this window)
        self.close()

    def showPassword(self):
        #print("ShowPassword")
        #print(self.ShowPassword.isChecked())
        if(self.ShowPassword.isChecked()):          #clicked
            self.PassLabel.setEchoMode(PySide2.QtWidgets.QLineEdit.Normal)
        else:
            self.PassLabel.setEchoMode(PySide2.QtWidgets.QLineEdit.Password)

    def keyPressed(self):
        number=int()
        for x in range(10):
            if(self.key[x].isDown()):
                number=x
        self.currentPass += str(number)
        #self.currentPass += number
        #print(number)
        self.PassLabel.setText(self.currentPass)

    def asterix(self):
        self.currentPass += "*"
        self.PassLabel.setText(self.currentPass)

    def numeral(self):
        self.currentPass += "#"
        self.PassLabel.setText(self.currentPass)

    def delete(self):
        self.currentPass = self.currentPass[:-1]
        self.PassLabel.setText(self.currentPass)

    def login(self):
        #TODO: check password against password list in "users.dat" File
        #and register whether a valid user tries to log in
        
        pass