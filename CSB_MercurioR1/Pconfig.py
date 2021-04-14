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
        Background_Style= """
                QFrame{
                	background-image: url(./images/fondo.png);
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }"""
        self.BACKGROUND.setStyleSheet(Background_Style)

#**************************************************** HERE ARE THE BUTTONS
#UPDATE button
        self.update_Btn = QPushButton(self.BACKGROUND)
        self.update_Btn.setObjectName(u"update_Btn")
        self.update_Btn.setGeometry(QRect(190, 350, 100, 100))
        self.update_Btn.setCheckable(True)
        self.update_Btn.setFlat(True)
        UPDATE_Button = """
                QPushButton {
                        border-style: none; 
                        background-image: url(./icons/routine_off.png); 
                        background-repeat: no-repeat; 
                        background-position: center center} 
                QPushButton:checked{
                        border-style: none; 
                        background-image: url(./icons/routine_on.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }"""
        self.update_Btn.setStyleSheet(UPDATE_Button)
        self.update_Btn.focusPolicy = Qt.NoFocus
        
        self.updateLabel = QLabel(self.BACKGROUND)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(190, 300, 100, 16))
        self.updateLabel.setAttribute(Qt.WA_TranslucentBackground)
        update_style="""
                QLabel{
                        font-family: url(./fonts/Montserrat-Regular.ttf);
                        font-size: 13px;
                        color: white;
                }"""
        self.updateLabel.setStyleSheet(update_style)

#**********************************************************************************

        self.BACKGROUND.raise_()
        self.update_Btn.raise_()
    
        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"form", None))
        self.update_Btn.setText("")        
        self.updateLabel.setText(QCoreApplication.translate("form", u"Actualización", None))

    # retranslateUi
