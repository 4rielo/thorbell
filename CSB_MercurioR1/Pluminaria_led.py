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

#LED light button
        self.OnOffButton = QPushButton(self.BACKGROUND)
        self.OnOffButton.setObjectName(u"OnOffButton")
        self.OnOffButton.setGeometry(QRect(195, 583, 100, 100))
        self.OnOffButton.setCheckable(True)
        self.OnOffButton.setFlat(True)
        LUZ_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/led_off.png); 
                }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/led_on.png); 
                }}"""
        self.OnOffButton.setStyleSheet(LUZ_Button)
        self.OnOffButton.focusPolicy = Qt.NoFocus

#Down button
        self.downButton = QPushButton(self.BACKGROUND)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setGeometry(QRect(17, 382, 57, 34))
        #self.downButton.setCheckable(False)
        self.downButton.setFlat(True)
        downButton_style = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/down_released.png); 
                }}
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/down_pressed.png); 
                }}"""
        self.downButton.setStyleSheet(downButton_style)
        self.downButton.focusPolicy = Qt.NoFocus

#Up button
        self.upButton = QPushButton(self.BACKGROUND)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setGeometry(QRect(406, 382, 57, 34))
        #self.upButton.setCheckable(False)
        self.upButton.setFlat(True)
        upButton_style = f"""   
                QPushButton {{
                        background-image: url({main.path}/icons/up_released.png); 
                }}
                QPushButton:pressed{{
                        background-image: url({main.path}/icons/up_pressed.png); 
                }}"""
        self.upButton.setStyleSheet(upButton_style)
        self.upButton.focusPolicy = Qt.NoFocus

#************************************************Here are the center round progress bar indicators
        Bar_InitialStyle=f"""
                QFrame{{
                	background-image: url();
                	border-radius: 92px;
                	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 145), stop:0.05 rgba(255, 255, 255, 0));
                }}"""

        self.ProgressBar = QFrame(self.BACKGROUND)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(0, 161, 480, 479))
        self.ProgressBar.setAutoFillBackground(True)
        ProgressBar_style=f"""
                QFrame{{
                	background-image: url({main.path}/images/dial_completo.png);
                }}"""
        self.ProgressBar.setStyleSheet(ProgressBar_style)
        self.ProgressBar.setFrameShape(QFrame.NoFrame)
        self.ProgressBar.setFrameShadow(QFrame.Plain)
        self.Bar = QFrame(self.ProgressBar)
        self.Bar.setObjectName(u"Bar")
        self.Bar.setGeometry(QRect(153, 147, 185, 185))
        self.Bar.setStyleSheet(Bar_InitialStyle)
        self.Bar.setFrameShape(QFrame.NoFrame)
        self.Bar.setFrameShadow(QFrame.Raised)        

        self.percentage_label = QLabel(self.ProgressBar)
        self.percentage_label.setGeometry(QRect(218, 220, 54, 26))
        ProgressValue_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 21px;
                }}"""
        self.percentage_label.setStyleSheet(ProgressValue_style)
        #self.label_2.setAlignment(Qt.AlignCenter)

        self.BACKGROUND.raise_()
        self.ProgressBar.raise_()
        self.OnOffButton.raise_()
        self.upButton.raise_()
        self.downButton.raise_()
        self.backButton.raise_()
        

        QMetaObject.connectSlotsByName(form)
    # setupUi