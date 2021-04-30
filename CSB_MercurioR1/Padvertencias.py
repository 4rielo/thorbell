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
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 21px;
                        color: white;
                        background: transparent;
                        qproperty-alignment: AlignCenter;
                        max-height: 26px;
                        min-height: 26px;
                        max-width: 200px;
                        min-width: 200px;
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
        #self.tittle.setAttribute(Qt.WA_TranslucentBackground)
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                        max-width: 480px;
                        min-width: 480px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setObjectName(u"tittleGlow")
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 22))
        #self.tittleGlow.setAttribute(Qt.WA_TranslucentBackground)
        tittleGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 21px;
                        max-width: 480px;
                        min-width: 480px;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)
#**************************************************** HERE ARE THE BUTTONS

#Buttons layout
        self.BtnsLayout = QGridLayout(self.BACKGROUND)
        self.BtnsLayout.setGeometry(QRect(0, 120, 480, 560))
        self.BtnsLayout.setAlignment(Qt.AlignCenter)

    # Back Button
        self.backButton = QPushButton(self.BACKGROUND)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(41, 700, 38, 37))
        self.backButton.setFlat(True)
        backButton_style= f"""
                QPushButton {{
                        border-style: none; 
                        background-image: url({main.path}/icons/back.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }}"""
        self.backButton.setStyleSheet(backButton_style)
        self.backButton.focusPolicy = Qt.NoFocus


# raise order
        self.BACKGROUND.raise_()
        
        self.backButton.raise_()
        
        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"", None))
        
    # retranslateUi

