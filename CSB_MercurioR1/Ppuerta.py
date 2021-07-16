# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'luminaria_led.ui'
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
                        color: white;      
                        qproperty-alignment: AlignCenter;
                        background: transparent;
                }}"""
        self.BACKGROUND.setStyleSheet(Background_Style)

        self.tittle = QLabel(self.BACKGROUND)
        self.tittle.setGeometry(QRect(0, 88, 480, 22))
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 22))
        tittleGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 21px;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)
#**************************************************** HERE ARE THE BUTTONS
    # Back Button
        self.backButton = QPushButton(self.BACKGROUND)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(41, 700, 38, 37))
        self.backButton.setFlat(True)
        backButton_style= f"""
                QPushButton {{
                        background-image: url({main.path}/icons/back.png); 
                }}"""
        self.backButton.setStyleSheet(backButton_style)
        self.backButton.focusPolicy = Qt.NoFocus

#Subir puerta button
        subir_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/up_released.png); 
                }} 
                QPushButton:pressed{{
                        background-image: url({main.path}/icons/up_pressed.png); 
                }}"""
        self.subirBtn = QPushButton(self.BACKGROUND)
        self.subirBtn.setGeometry(QRect(190, 200, 100, 100))
        self.subirBtn.setFlat(True)
        self.subirBtn.setStyleSheet(subir_Button)
        self.subirBtn.focusPolicy = Qt.NoFocus

#Bajar puerta button
        bajar_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/down_released.png); 
                }}
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/down_pressed.png); 
                }}"""
        self.bajarBtn = QPushButton(self.BACKGROUND)
        self.bajarBtn.setGeometry(QRect(190, 533, 100, 100))
        self.bajarBtn.setFlat(True)
        self.bajarBtn.setStyleSheet(bajar_Button)
        self.bajarBtn.focusPolicy = Qt.NoFocus

#Posicion de trabajo puerta button
        posTrabajo_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/controlPuerta_trabajo.png); 
                }}"""
        self.posTrabajoBtn = QPushButton(self.BACKGROUND)
        self.posTrabajoBtn.setGeometry(QRect(190, 366, 100, 100))
        self.posTrabajoBtn.setFlat(True)
        self.posTrabajoBtn.setStyleSheet(posTrabajo_Button)
        self.posTrabajoBtn.focusPolicy = Qt.NoFocus

#Abierta puerta button
        abrir_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/controlPuerta_abierta.png); 
                }}"""
        self.abrirBtn = QPushButton(self.BACKGROUND)
        self.abrirBtn.setGeometry(QRect(40, 366, 100, 100))
        self.abrirBtn.setFlat(True)
        self.abrirBtn.setStyleSheet(abrir_Button)
        self.abrirBtn.focusPolicy = Qt.NoFocus

#Cerrada puerta button
        cerrar_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/controlPuerta_cerrada.png); 
                }}"""
        self.cerrarBtn = QPushButton(self.BACKGROUND)
        self.cerrarBtn.setGeometry(QRect(340, 366, 100, 100))
        self.cerrarBtn.setFlat(True)
        self.cerrarBtn.setStyleSheet(cerrar_Button)
        self.cerrarBtn.focusPolicy = Qt.NoFocus


        """self.BACKGROUND.raise_()
        self.ProgressBar.raise_()
        self.OnOffButton.raise_()
        self.upButton.raise_()
        self.downButton.raise_()
        self.backButton.raise_()"""
        

        QMetaObject.connectSlotsByName(form)
    # setupUi
