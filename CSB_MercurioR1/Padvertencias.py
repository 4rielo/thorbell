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
                }}"""
        self.BACKGROUND.setStyleSheet(Background_Style)

        self.title = QFrame(self.BACKGROUND)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(154, 76, 173, 38))
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        title_style=f"""
                QFrame {{
                	background-image: url({main.path}/images/Advertencia_title.png);
                	background-repeat: no-repeat;
                }}"""
        self.title.setStyleSheet(title_style)
#**************************************************** HERE ARE THE BUTTONS
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

