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
                """
        self.BACKGROUND.setStyleSheet(Background_Style)
        """El estilo de QPushButton se aplica al BACKGROUND, y se 
        hereda por todos los QPushButton que contiene, tanto en estado común, como 
        en estado "checked". No es necesario volver a especificar el estilo 
        de borde, la repetibilidad de imagen, o su posicion.
        """
#**************************************************** Logo

        self.logo = QFrame(self.BACKGROUND)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(0, 71, 480, 48)
        self.logo.setAttribute(Qt.WA_TranslucentBackground)
        logo_Style= f"""
                QFrame{{
                	background-image: url({main.path}/images/Logo.png);
                }}"""
        self.logo.setStyleSheet(logo_Style)
#****************************************************

#**************************************************** Tittle

        self.postVenta = QLabel(self.BACKGROUND)
        self.postVenta.setObjectName(u"postVenta")
        self.postVenta.setGeometry(QRect(0, 0, 480, 800))
        self.postVenta.setAttribute(Qt.WA_TranslucentBackground)
        postVenta_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.postVenta.setStyleSheet(postVenta_style)

        self.postVentaGlow = QLabel(self.BACKGROUND)
        self.postVentaGlow.setObjectName(u"postVentaGlow")
        self.postVentaGlow.setGeometry(QRect(0, 0, 480, 800))
        self.postVentaGlow.setAttribute(Qt.WA_TranslucentBackground)
        postVentaGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                }}"""
        self.postVentaGlow.setStyleSheet(postVentaGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(5)
        self.postVentaGlow.setGraphicsEffect(self.Effect)


#CurrentVersion Label        
        self.versionLabel = QLabel(self.BACKGROUND)
        self.versionLabel.setObjectName(u"versionLabel")
        self.versionLabel.setGeometry(QRect(41, 619, 400, 50))
        self.versionLabel.setAttribute(Qt.WA_TranslucentBackground)
        version_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 13px;
                        color: white;
                        qproperty-alignment: AlignLeft, AlignVCenter;
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

#**************************************************** HERE ARE THE BUTTONS
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
        self.return_Btn.focusPolicy = Qt.NoFocus

#**********************************************************************************

        self.BACKGROUND.raise_()
        self.postVentaGlow.raise_()
        self.postVenta.raise_()

        self.return_Btn.raise_()
        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"form", None))
        
    # retranslateUi

