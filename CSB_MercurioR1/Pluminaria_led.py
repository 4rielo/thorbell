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


class Ui_Form(object):
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
        Background_Style= """
                QFrame{
                	background-image: url(./images/fondo.png);
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }"""
        self.BACKGROUND.setStyleSheet(Background_Style)

#**************************************************** HERE ARE THE BUTTONS
    # Back Button
        self.backButton = QPushButton(self.BACKGROUND)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(41, 700, 38, 37))
        self.backButton.setFlat(True)
        backButton_style= """
            QPushButton {
                        border-style: none; 
                        background-image: url(./icons/back.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                        }
        """
        self.backButton.setStyleSheet(backButton_style)
        self.backButton.focusPolicy = Qt.NoFocus

    #LED light button
        self.OnOffButton = QPushButton(self.BACKGROUND)
        self.OnOffButton.setObjectName(u"OnOffButton")
        self.OnOffButton.setGeometry(QRect(195, 583, 100, 100))
        self.OnOffButton.setCheckable(True)
        self.OnOffButton.setFlat(True)
        LUZ_Button = """
                QPushButton {
                        border-style: none; 
                        background-image: url(./icons/led_off.png); 
                        background-repeat: no-repeat; 
                        background-position: center center} 
                QPushButton:checked{
                        border-style: none; 
                        background-image: url(./icons/led_on.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }"""
        self.OnOffButton.setStyleSheet(LUZ_Button)
        self.OnOffButton.focusPolicy = Qt.NoFocus

        self.title = QFrame(self.BACKGROUND)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(160, 81, 160, 29))
        self.title.setFrameShape(QFrame.NoFrame)
        self.title.setFrameShadow(QFrame.Raised)
        title_style="""
                QFrame {
                	background-image: url(./images/title.png);
                	background-repeat: no-repeat;
                }"""
        self.title.setStyleSheet(title_style)

#Down button
        self.downButton = QPushButton(self.BACKGROUND)
        self.downButton.setObjectName(u"downButton")
        self.downButton.setGeometry(QRect(17, 382, 57, 34))
        self.downButton.setCheckable(False)
        self.downButton.setFlat(True)
        downButton_style = """
                QPushButton {
                        border-style: none; 
                        background-image: url(./icons/down_released.png); 
                        background-repeat: no-repeat; 
                        background-position: center center} """
        """        QPushButton:checked{
                        border-style: none; 
                        background-image: url(./icons/down_pressed.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }"""
        self.downButton.setStyleSheet(downButton_style)
        self.downButton.focusPolicy = Qt.NoFocus

#Up button
        self.upButton = QPushButton(self.BACKGROUND)
        self.upButton.setObjectName(u"upButton")
        self.upButton.setGeometry(QRect(406, 382, 57, 34))
        self.upButton.setCheckable(False)
        self.upButton.setFlat(True)
        upButton_style = """
                QPushButton {
                        border-style: none; 
                        background-image: url(./icons/up_released.png); 
                        background-repeat: no-repeat; 
                        background-position: center center} """
        """        QPushButton:checked{
                        border-style: none; 
                        background-image: url(./icons/up_pressed.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }"""
        self.upButton.setStyleSheet(upButton_style)
        self.upButton.focusPolicy = Qt.NoFocus

        self.horizontalSlider = QSlider(self.BACKGROUND)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(100, 130, 100, 20))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
#************************************************Here are the center round progress bar indicators
        Bar_InitialStyle="""
                QFrame{
                	background-image: url();
                	border-radius: 92px;
                	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 145), stop:0.05 rgba(255, 255, 255, 0));
                }"""

        self.ProgressBar = QFrame(self.BACKGROUND)
        self.ProgressBar.setObjectName(u"ProgressBar")
        self.ProgressBar.setGeometry(QRect(0, 161, 480, 479))
        self.ProgressBar.setAutoFillBackground(True)
        ProgressBar_style="""
                QFrame{
                	background-image: url(./images/dial_completo.png);
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }"""
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
        self.percentage_label.setObjectName(u"percentage_label")
        self.percentage_label.setGeometry(QRect(218, 220, 54, 26))
        self.percentage_label.setAttribute(Qt.WA_TranslucentBackground)
        ProgressValue_style="""
                QLabel{
                        font-family: url(./fonts/Montserrat-Regular.ttf);
                        font-size: 21px;
                        color: white;
                }"""
        self.percentage_label.setStyleSheet(ProgressValue_style)
        #self.label_2.setAlignment(Qt.AlignCenter)

        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("Form", u"", None))
        self.OnOffButton.setText(QCoreApplication.translate("Form", u"", None))
        self.percentage_label.setText(QCoreApplication.translate("Form", u"", None))
        self.downButton.setText(QCoreApplication.translate("Form", u"", None))
        self.upButton.setText(QCoreApplication.translate("Form", u"", None))
    # retranslateUi

