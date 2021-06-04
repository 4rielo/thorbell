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
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 13px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        background: transparent;
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
        #self.tittle.setAttribute(Qt.WA_TranslucentBackground)
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setObjectName(u"tittleGlow")
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 22))
        #self.tittleGlow.setAttribute(Qt.WA_TranslucentBackground)
        tittleGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 20px;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)


#**************************************************** HERE ARE THE BUTTONS
#UPDATE button
        self.update_Btn = QPushButton(self.BACKGROUND)
        self.update_Btn.setObjectName(u"update_Btn")
        self.update_Btn.setGeometry(QRect(190, 500, 100, 100))
        self.update_Btn.setCheckable(True)
        self.update_Btn.setFlat(True)
        UPDATE_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/routine_off.png); 
                }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/routine_on.png); 
                }}"""
        self.update_Btn.setStyleSheet(UPDATE_Button)
        self.update_Btn.setFocusPolicy(Qt.NoFocus)

#USB button
        self.usb_Btn = QPushButton(self.BACKGROUND)
        self.usb_Btn.setFixedSize(76, 48)
        usb_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/usb.png);
                }}"""
        self.usb_Btn.setStyleSheet(usb_BtnStyle)
        self.usb_Btn.setFocusPolicy(Qt.NoFocus)

        self.usbLabel = QLabel(self.BACKGROUND)
        self.usbLabel.setFixedSize(76, 16)
        #self.usbLabel.setAttribute(Qt.WA_TranslucentBackground)

#Info Button
        self.info_Btn = QPushButton(self.BACKGROUND)
        self.info_Btn.setObjectName(u"info_Btn")
        self.info_Btn.setFixedSize(76, 48)
        info_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/info.png);
                }}"""
        self.info_Btn.setStyleSheet(info_BtnStyle)
        self.info_Btn.setFocusPolicy(Qt.NoFocus)

        self.infoLabel = QLabel(self.BACKGROUND)
        self.infoLabel.setFixedSize(76, 16)
        #self.infoLabel.setAttribute(Qt.WA_TranslucentBackground)

        self.infoLabel_Glow = QLabel(self.BACKGROUND)
        self.infoLabel_Glow.setFixedSize(76, 16)
        #self.infoLabel_Glow.setAttribute(Qt.WA_TranslucentBackground)
        glowSize=f"""
                QLabel{{
                        font-size: 14px;
                }}"""
        self.infoLabel_Glow.setStyleSheet(glowSize)
        self.infoGlow=QGraphicsBlurEffect()
        self.infoGlow.setBlurRadius(10)
        self.infoLabel_Glow.setGraphicsEffect(self.infoGlow)


#Login Button
        self.login_Btn = QPushButton(self.BACKGROUND)
        self.login_Btn.setObjectName(u"login_Btn")
        self.login_Btn.setFixedSize(76, 48)
        login_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/login.png);
                }}"""
        self.login_Btn.setStyleSheet(login_BtnStyle)
        self.login_Btn.setFocusPolicy(Qt.NoFocus)

        self.loginLabel = QLabel(self.BACKGROUND)
        self.loginLabel.setFixedSize(76, 16)
        #self.loginLabel.setAttribute(Qt.WA_TranslucentBackground)

#Buttons layout
        self.BtnsLayout = QGridLayout(self.BACKGROUND)
        self.BtnsLayout.setGeometry(QRect(0, 376, 480, 86))
        self.BtnsLayout.setAlignment(Qt.AlignCenter)
        self.BtnsLayout.addWidget(self.usb_Btn,0,0)
        self.BtnsLayout.addWidget(self.usbLabel,1,0)
        self.BtnsLayout.addWidget(self.info_Btn,0,1)
        self.BtnsLayout.addWidget(self.infoLabel,1,1)
        self.BtnsLayout.addWidget(self.infoLabel_Glow,1,1)
        self.BtnsLayout.addWidget(self.login_Btn,0,2)
        self.BtnsLayout.addWidget(self.loginLabel,1,2)

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

#CurrentVersion Label        
        self.versionLabel = QLabel(self.BACKGROUND)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(10, 10, 200, 16))
        #self.versionLabel.setAttribute(Qt.WA_TranslucentBackground)

#update Label        
        self.updateLabel = QLabel(self.BACKGROUND)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(90, 300, 300, 32))
        #self.updateLabel.setAttribute(Qt.WA_TranslucentBackground)

#**********************************************************************************

        self.BACKGROUND.raise_()
        self.update_Btn.raise_()
        self.tittle.raise_()

        QMetaObject.connectSlotsByName(form)