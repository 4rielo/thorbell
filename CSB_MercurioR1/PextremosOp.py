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
                        background-position: center center;
                        background-image: url({main.path}/icons/login_button.png);
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 18px;
                        color: #1BDDD2;
                }}
                QPushButton:checked {{
                        background-image: url({main.path}/icons/login_button_pressed.png);
                        color: #001532;
                }}
                QLabel {{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 15px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        background: transparent;
                }}"""
        self.BACKGROUND.setStyleSheet(Background_Style)
        """El estilo de QPushButton se aplica al BACKGROUND, y se 
        hereda por todos los QPushButton que contiene, tanto en estado común, como 
        en estado "checked". No es necesario volver a especificar el estilo 
        de borde, la repetibilidad de imagen, o su posicion.
        """
#**************************************************** Tittle

        self.tittle = QLabel(self.BACKGROUND)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(0, 88, 480, 44))
        #self.tittle.setAttribute(Qt.WA_TranslucentBackground)
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setObjectName(u"tittleGlow")
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 44))
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

#**************************************************** HERE ARE THE infoLabels
        LabelsStyle = f"""
                QLabel{{
                        qproperty-alignment: AlignLeft;
                        }}"""

        self.velMinLbl = QLabel(self.BACKGROUND)
        self.velMinLbl.setGeometry(QRect(50, 180, 120, 22))
        self.velMinLbl.setStyleSheet(LabelsStyle)

        self.velMinValue = QLabel(self.BACKGROUND)
        self.velMinValue.setGeometry(QRect(170, 180, 140, 22))
        self.velMinValue.setStyleSheet(LabelsStyle)

        self.velMaxLbl = QLabel(self.BACKGROUND)
        self.velMaxLbl.setGeometry(QRect(50, 210, 200, 22))
        self.velMaxLbl.setStyleSheet(LabelsStyle)
        
        self.velMaxValue = QLabel(self.BACKGROUND)
        self.velMaxValue.setGeometry(QRect(170, 210, 140, 22))
        self.velMaxValue.setStyleSheet(LabelsStyle)

        self.pruebaRegLbl = QLabel(self.BACKGROUND)
        self.pruebaRegLbl.setGeometry(QRect(0, 450, 480, 22))

        self.motorValue = QLabel(self.BACKGROUND)
        self.motorValue.setGeometry(QRect(210, 580, 60, 22))
        
#**************************************************** HERE ARE THE BUTTONS
# Motor de Bajada button
        self.motorOnOff_Btn = QPushButton(self.BACKGROUND)
        self.motorOnOff_Btn.setGeometry(QRect(150, 500, 180, 55))
        self.motorOnOff_Btn.setFocusPolicy(Qt.NoFocus)
        self.motorOnOff_Btn.setCheckable(True)

        plus_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/up_released.png); 
                }}
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/up_pressed.png); 
                }}"""
        self.motorMas_Btn = QPushButton(self.BACKGROUND)
        self.motorMas_Btn.setGeometry(QRect(270, 580, 60, 40))
        self.motorMas_Btn.setStyleSheet(plus_Button)
        self.motorMas_Btn.setFocusPolicy(Qt.NoFocus)

        minus_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/down_released.png); 
                }}
                QPushButton::pressed {{
                        background-image: url({main.path}/icons/down_pressed.png); 
                }}"""
        self.motorMenos_Btn = QPushButton(self.BACKGROUND)
        self.motorMenos_Btn.setGeometry(QRect(150, 300, 60, 40))
        self.motorMenos_Btn.setStyleSheet(minus_Button)
        self.motorMenos_Btn.setFocusPolicy(Qt.NoFocus)

        self.extremoMas_Btn = QPushButton(self.BACKGROUND)
        self.extremoMas_Btn.setGeometry(QRect(270, 300, 60, 40))
        self.extremoMas_Btn.setStyleSheet(plus_Button)
        self.extremoMas_Btn.setFocusPolicy(Qt.NoFocus)

        self.extremoMenos_Btn = QPushButton(self.BACKGROUND)
        self.extremoMenos_Btn.setGeometry(QRect(150, 580, 60, 40))
        self.extremoMenos_Btn.setStyleSheet(minus_Button)
        self.extremoMenos_Btn.setFocusPolicy(Qt.NoFocus)

        guardarStyle =f"""
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/login_button_pressed.png);
                        color: #001532;
                }}"""
        self.guardar_Btn = QPushButton(self.BACKGROUND)
        self.guardar_Btn.setGeometry(QRect(280, 700, 180, 55))
        self.guardar_Btn.setFocusPolicy(Qt.NoFocus)
        self.guardar_Btn.setStyleSheet(guardarStyle)

#back button
        return_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/back.png); 
                }}"""
        self.return_Btn = QPushButton(self.BACKGROUND)
        self.return_Btn.setGeometry(QRect(41, 700, 38, 37))
        self.return_Btn.setFlat(True)
        self.return_Btn.setStyleSheet(return_Button)
        self.return_Btn.setFocusPolicy(Qt.NoFocus)

#**********************************************************************************
        self.velMinRadioBox = QRadioButton(self.BACKGROUND)
        self.velMinRadioBox.setGeometry(QRect(30,180,20,20))

        self.velMaxRadioBox = QRadioButton(self.BACKGROUND)
        self.velMaxRadioBox.setGeometry(QRect(30,210,20,20))
#**********************************************************************************

        #self.BACKGROUND.raise_()

        #self.tittle.raise_()

        QMetaObject.connectSlotsByName(form)