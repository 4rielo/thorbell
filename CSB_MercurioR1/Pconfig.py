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
                }}"""
        self.BACKGROUND.setStyleSheet(Background_Style)
#**************************************************** Tittle

        self.tittle = QLabel(self.BACKGROUND)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(168, 88, 145, 22))
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
        self.tittleGlow.setGeometry(QRect(168, 88, 145, 22))
        self.tittleGlow.setAttribute(Qt.WA_TranslucentBackground)
        tittleGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 21px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)


#**************************************************** HERE ARE THE BUTTONS
#UPDATE button
        self.update_Btn = QPushButton(self.BACKGROUND)
        self.update_Btn.setObjectName(u"update_Btn")
        self.update_Btn.setGeometry(QRect(190, 350, 100, 100))
        self.update_Btn.setCheckable(True)
        self.update_Btn.setFlat(True)
        UPDATE_Button = f"""
                QPushButton {{
                        border-style: none; 
                        background-image: url({main.path}/icons/routine_off.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }} 
                QPushButton:checked{{
                        border-style: none; 
                        background-image: url({main.path}/icons/routine_on.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }}"""
        self.update_Btn.setStyleSheet(UPDATE_Button)
        self.update_Btn.focusPolicy = Qt.NoFocus

#back button
        self.return_Btn = QPushButton(self.BACKGROUND)
        self.return_Btn.setObjectName(u"return_Btn")
        self.return_Btn.setGeometry(QRect(41, 700, 38, 37))
        self.return_Btn.setCheckable(True)
        self.return_Btn.setFlat(True)
        return_Button = f"""
                QPushButton {{
                        border-style: none; 
                        background-image: url({main.path}/icons/back.png); 
                        background-repeat: no-repeat; 
                        background-position: center center
                }}"""
        self.return_Btn.setStyleSheet(return_Button)
        self.return_Btn.focusPolicy = Qt.NoFocus

#CurrentVersion Label        
        self.versionLabel = QLabel(self.BACKGROUND)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(10, 10, 200, 16))
        self.versionLabel.setAttribute(Qt.WA_TranslucentBackground)
        version_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 13px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.versionLabel.setStyleSheet(version_style)


#update Label        
        self.updateLabel = QLabel(self.BACKGROUND)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setGeometry(QRect(90, 300, 300, 32))
        self.updateLabel.setAttribute(Qt.WA_TranslucentBackground)
        update_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 13px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.updateLabel.setStyleSheet(update_style)

#**********************************************************************************

        self.BACKGROUND.raise_()
        self.update_Btn.raise_()
        self.tittle.raise_()
    
        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"form", None))
        self.update_Btn.setText("")        
        self.updateLabel.setText(QCoreApplication.translate("form", u"Actualización", None))

    # retranslateUi

