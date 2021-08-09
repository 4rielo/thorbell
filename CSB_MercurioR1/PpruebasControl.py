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
        self.tittle.setGeometry(QRect(0, 88, 480, 22))
        #self.tittle.setAttribute(Qt.WA_TranslucentBackground)
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
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

#**************************************************** HERE ARE THE infoLabels
        LabelsStyle = f"""
                QLabel{{
                        qproperty-alignment: AlignLeft;
                        }}"""

        self.velFlujoLbl = QLabel(self.BACKGROUND)
        self.velFlujoLbl.setGeometry(QRect(20, 150, 200, 22))
        self.velFlujoLbl.setStyleSheet(LabelsStyle)

        self.flujoBajadaLbl = QLabel(self.BACKGROUND)
        self.flujoBajadaLbl.setGeometry(QRect(20, 180, 120, 22))
        self.flujoBajadaLbl.setStyleSheet(LabelsStyle)

        self.flujoBajadaValue = QLabel(self.BACKGROUND)
        self.flujoBajadaValue.setGeometry(QRect(140, 180, 140, 22))
        self.flujoBajadaValue.setStyleSheet(LabelsStyle)

        self.flujoSubidaLbl = QLabel(self.BACKGROUND)
        self.flujoSubidaLbl.setGeometry(QRect(20, 210, 200, 22))
        self.flujoSubidaLbl.setStyleSheet(LabelsStyle)
        
        self.flujoSubidaValue = QLabel(self.BACKGROUND)
        self.flujoSubidaValue.setGeometry(QRect(140, 210, 140, 22))
        self.flujoSubidaValue.setStyleSheet(LabelsStyle)

        self.presionFiltrosLbl = QLabel(self.BACKGROUND)
        self.presionFiltrosLbl.setGeometry(QRect(20, 250, 200, 22))
        self.presionFiltrosLbl.setStyleSheet(LabelsStyle)

        self.presionBajadaLbl = QLabel(self.BACKGROUND)
        self.presionBajadaLbl.setGeometry(QRect(20, 280, 120, 22))
        self.presionBajadaLbl.setStyleSheet(LabelsStyle)

        self.presionBajadaValue = QLabel(self.BACKGROUND)
        self.presionBajadaValue.setGeometry(QRect(140, 280, 140, 22))
        self.presionBajadaValue.setStyleSheet(LabelsStyle)

        self.presionSubidaLbl = QLabel(self.BACKGROUND)
        self.presionSubidaLbl.setGeometry(QRect(20, 310, 200, 22))
        self.presionSubidaLbl.setStyleSheet(LabelsStyle)
        
        self.presionSubidaValue = QLabel(self.BACKGROUND)
        self.presionSubidaValue.setGeometry(QRect(140, 310, 140, 22))
        self.presionSubidaValue.setStyleSheet(LabelsStyle)

        self.MotorBajadaValue = QLabel(self.BACKGROUND)
        self.MotorBajadaValue.setGeometry(QRect(90, 580, 40, 40))

        self.MotorSubidaValue = QLabel(self.BACKGROUND)
        self.MotorSubidaValue.setGeometry(QRect(350, 580, 40, 40))
        
#**************************************************** HERE ARE THE BUTTONS
#Tomacorrientes button
        self.tomacorrientes_Btn = QPushButton(self.BACKGROUND)
        self.tomacorrientes_Btn.setGeometry(QRect(280, 150, 180, 55))
        self.tomacorrientes_Btn.setFocusPolicy(Qt.NoFocus)
        self.tomacorrientes_Btn.setCheckable(True)

# Motor de Bajada button
        self.motorBajadaOnOff_Btn = QPushButton(self.BACKGROUND)
        self.motorBajadaOnOff_Btn.setGeometry(QRect(20, 500, 180, 55))
        self.motorBajadaOnOff_Btn.setFocusPolicy(Qt.NoFocus)
        self.motorBajadaOnOff_Btn.setCheckable(True)

        plus_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/up_released.png); 
                }}
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/up_pressed.png); 
                }}"""
        self.motorBajadaMas_Btn = QPushButton(self.BACKGROUND)
        self.motorBajadaMas_Btn.setGeometry(QRect(140, 580, 60, 40))
        self.motorBajadaMas_Btn.setStyleSheet(plus_Button)
        self.motorBajadaMas_Btn.setFocusPolicy(Qt.NoFocus)

        minus_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/down_released.png); 
                }}
                QPushButton::pressed {{
                        background-image: url({main.path}/icons/down_pressed.png); 
                }}"""
        self.motorBajadaMenos_Btn = QPushButton(self.BACKGROUND)
        self.motorBajadaMenos_Btn.setGeometry(QRect(20, 580, 60, 40))
        self.motorBajadaMenos_Btn.setStyleSheet(minus_Button)
        self.motorBajadaMenos_Btn.setFocusPolicy(Qt.NoFocus)

#Motor de Subida button
        self.motorSubidaOnOff_Btn = QPushButton(self.BACKGROUND)
        self.motorSubidaOnOff_Btn.setGeometry(QRect(280, 500, 180, 55))
        self.motorSubidaOnOff_Btn.setFocusPolicy(Qt.NoFocus)
        self.motorSubidaOnOff_Btn.setCheckable(True)

        self.motorSubidaMas_Btn = QPushButton(self.BACKGROUND)
        self.motorSubidaMas_Btn.setGeometry(QRect(400, 580, 60, 40))
        self.motorSubidaMas_Btn.setStyleSheet(plus_Button)
        self.motorSubidaMas_Btn.setFocusPolicy(Qt.NoFocus)

        self.motorSubidaMenos_Btn = QPushButton(self.BACKGROUND)
        self.motorSubidaMenos_Btn.setGeometry(QRect(280, 580, 60, 40))
        self.motorSubidaMenos_Btn.setStyleSheet(minus_Button)
        self.motorSubidaMenos_Btn.setFocusPolicy(Qt.NoFocus)

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

        #self.BACKGROUND.raise_()

        #self.tittle.raise_()

        QMetaObject.connectSlotsByName(form)