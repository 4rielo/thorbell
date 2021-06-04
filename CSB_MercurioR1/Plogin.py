# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import main

class Ui_form(object):
    def setupUi(self, form):
        if not form.objectName():
            form.setObjectName(u"form")
        form.resize(480, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form.sizePolicy().hasHeightForWidth())
        form.setSizePolicy(sizePolicy)
        form.setMinimumSize(QSize(480, 800))
        form.setMaximumSize(QSize(480, 800))
        form.setAutoFillBackground(True)

        self.BACKGROUND = QFrame(form)
        self.BACKGROUND.setObjectName(u"BACKGROUND")
        self.BACKGROUND.setFrameShape(QFrame.NoFrame)
        self.BACKGROUND.setGeometry(QRect(0, 0, 480, 800))
        Background_Style= f"""
                QFrame{{
                	background-image: url({main.path}/images/fondo.png);
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }}
                QPushButton {{
                        border-style: none;
                        background-repeat: no-repeat;
                        background-position: center center
                }}
                """
        self.BACKGROUND.setStyleSheet(Background_Style)
        """El estilo de QPushButton se aplica al BACKGROUND, y se 
        hereda por todos los QPushButton que contiene, tanto en estado común, como 
        en estado "checked". No es necesario volver a especificar el estilo 
        de borde, la repetibilidad de imagen, o su posicion.
        """
#**************************************************** Tittle

        self.tittle = QLabel(self.BACKGROUND)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(0, 88, 480, 22))
        self.tittle.setAttribute(Qt.WA_TranslucentBackground)
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setObjectName(u"tittleGlow")
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 22))
        self.tittleGlow.setAttribute(Qt.WA_TranslucentBackground)
        tittleGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 20px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)

#**************************************************** Typed digits + show icon
        self.Password = QFrame(self.BACKGROUND)
        self.Password.setGeometry(QRect(100,150,280,58))
        self.Password.setAutoFillBackground(True)
        self.Password.setFrameShape(QFrame.NoFrame)
        self.Password.setFrameShadow(QFrame.Plain)
        Password_style=f"""
                QFrame{{
                	background-image: url({main.path}/icons/number_labels.png);
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }}
                QLineEdit{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 18px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        
                        background: transparent;
                        border: none;
                }}"""#background: rgba(255,255,255,0);
        self.Password.setStyleSheet(Password_style)

        self.PassLabel = QLineEdit(self.Password)
        #self.PassLabel.setAttribute(Qt.WA_TranslucentBackground)
        self.PassLabel.setGeometry(0,0,280,58)
        
        self.ShowPassword = QPushButton(self.Password)
        self.ShowPassword.setGeometry(222, 20, 25, 18)
        self.ShowPassword.setCheckable(True)
        self.ShowPassword.setFlat(True)
        showHide_Style=f"""
                QPushButton{{
                        background-image: url({main.path}/icons/password_hide.png);
                }}
                QPushButton:checked{{
                        background-image: url({main.path}/icons/password_show.png);
                }}"""
        self.ShowPassword.setStyleSheet(showHide_Style)
        self.ShowPassword.setFocusPolicy(Qt.NoFocus)

#****************************************************


#**************************************************** HERE ARE THE BUTTONS
#Keypad buttons
        self.KeyPad = QFrame(self.BACKGROUND)
        self.KeyPad.setGeometry(99, 225, 282, 453)
        self.KeyPad.setFrameShape(QFrame.NoFrame)
#Buttons layout
        self.BtnsLayout = QGridLayout(self.KeyPad)
        self.BtnsLayout.setGeometry(QRect(0, 0, 282, 359))
        self.BtnsLayout.setAlignment(Qt.AlignCenter)
        self.BtnsLayout.setHorizontalSpacing(23)
        self.BtnsLayout.setVerticalSpacing(23)
        self.key = list()
        keypad_Style=f"""
                QFrame {{
                        background-image: url();
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }}
                QPushButton{{
                        background-image: url({main.path}/icons/login_keypad.png);
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 18px;
                        color: #1BDDD2;
                }}
                QPushButton:pressed{{
                        background-image: url({main.path}/icons/login_keypad_pressed.png);
                        color: #001532;
                }}"""
        self.KeyPad.setStyleSheet(keypad_Style)
        for digit in range(10):
                self.key.insert(digit, QPushButton(self.KeyPad))
                self.key[digit].setFixedSize(78, 78)
                self.key[digit].setFlat(True)
                self.key[digit].setFocusPolicy(Qt.NoFocus)
                self.key[digit].setText(str(digit))
                if(digit):
                        self.BtnsLayout.addWidget(self.key[digit], int((digit-1)/3), ((digit-1)%3))
                else:
                        self.BtnsLayout.addWidget(self.key[0], 3, 1)

        self.keyAsterix=QPushButton(self.KeyPad)
        self.keyAsterix.setFixedSize(78, 78)
        self.keyAsterix.setFlat(True)
        self.keyAsterix.setFocusPolicy(Qt.NoFocus)
        self.keyAsterix.setText("*")
        self.BtnsLayout.addWidget(self.keyAsterix, 3, 0)

        self.keyNumeral = QPushButton(self.KeyPad)
        self.keyNumeral.setFixedSize(78, 78)
        self.keyNumeral.setFlat(True)
        self.keyNumeral.setFocusPolicy(Qt.NoFocus)
        self.keyNumeral.setText("#")
        self.BtnsLayout.addWidget(self.keyNumeral, 3, 2)

        self.deleteBtn = QPushButton(self.KeyPad)
        self.deleteBtn.setFixedSize(78, 56)
        deleteBtn_Style=f"""
                QPushButton{{
                        background-image: url({main.path}/icons/delete.png);
                }}
                QPushButton:pressed{{
                        background-image: url({main.path}/icons/delete_pressed.png);
                }}"""
        self.deleteBtn.setStyleSheet(deleteBtn_Style)
        self.deleteBtn.setFlat(True)
        self.deleteBtn.setFocusPolicy(Qt.NoFocus)
        self.BtnsLayout.addWidget(self.deleteBtn, 4, 0)

        self.loginBtn = QPushButton(self.KeyPad)
        self.loginBtn.setFixedSize(167, 55)
        self.loginBtn.setText("login")
        loginBtn_Style=f"""
                QPushButton{{
                        background-image: url({main.path}/icons/login_button.png);
                }}
                QPushButton:pressed{{
                        background-image: url({main.path}/icons/login_button_pressed.png);
                }}"""
        self.loginBtn.setStyleSheet(loginBtn_Style)
        self.loginBtn.setFlat(True)
        self.loginBtn.setFocusPolicy(Qt.NoFocus)
        self.BtnsLayout.addWidget(self.loginBtn, 4, 1, 1, 2)
#back button
        self.return_Btn = QPushButton(self.BACKGROUND)
        self.return_Btn.setObjectName(u"return_Btn")
        self.return_Btn.setGeometry(QRect(41, 700, 38, 37))
        self.return_Btn.setCheckable(True)
        self.return_Btn.setFlat(True)
        return_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/back.png); 
                }}"""
        self.return_Btn.setStyleSheet(return_Button)
        self.return_Btn.setFocusPolicy(Qt.NoFocus)

#**********************************************************************************

        self.BACKGROUND.raise_()
        self.tittle.raise_()
        self.KeyPad.raise_()

        QMetaObject.connectSlotsByName(form)


