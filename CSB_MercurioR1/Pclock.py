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
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 14px;
                        color: white;
                        background: transparent;
                        qproperty-alignment: AlignCenter;
                }}
                QPushButton {{
                        border-style: none;
                        background-repeat: no-repeat;
                        background-position: center center
                }}
                QDateEdit {{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 20px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        
                        background: transparent;
                        border: none;
                }}
                QTimeEdit {{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 20px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        
                        background: transparent;
                        border: none;
                }}
                QSpinBox {{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 20px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        
                        background: transparent;
                        border: none;
                }}
                """
        self.BACKGROUND.setStyleSheet(Background_Style)
        """El estilo de QPushButton se aplica al BACKGROUND, y se 
        hereda por todos los QPushButton que contiene, tanto en estado común, como 
        en estado "checked". No es necesario volver a especificar el estilo 
        de borde, la repetibilidad de imagen, o su posicion.
        """

#**************************************************** Tittle
#Tittle
        self.tittle = QLabel(self.BACKGROUND)
        self.tittle.setObjectName(u"tittle")
        self.tittle.setGeometry(QRect(0, 88, 480, 22))
        tittle_style=f"""
                QLabel{{
                        font-size: 19px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setObjectName(u"tittleGlow")
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 22))
        tittleGlow_style=f"""
                QLabel{{
                        font-size: 20px;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)

#**************************************************** 

#**************************************************** Fecha y Hora
        self.horaActualLbl = QLabel(self.BACKGROUND)
        self.horaActualLbl.setGeometry(92, 379, 388, 17)
        horaLbl_style = f"""
                QLabel{{
                        font-size: 14px;
                        color: #1BC6D5;
                        qproperty-alignment: AlignLeft;
                }}"""
        self.horaActualLbl.setStyleSheet(horaLbl_style)

        self.horaEdit = QTimeEdit(self.BACKGROUND)
        self.horaEdit.setGeometry(118, 407, 139, 24)
        self.horaEdit.setDisplayFormat("HH:mm:ss")
        self.horaEdit.setFocusPolicy(Qt.NoFocus)
        self.horaEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

        """self.gmtEdit = QSpinBox(self.BACKGROUND)
        self.gmtEdit.setGeometry(118, 460, 139, 24)
        self.gmtEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.gmtEdit.setRange(-12,12)
        self.gmtEdit.setFocusPolicy(Qt.NoFocus)
        self.gmtEdit.setPrefix("GMT:")"""

#TIME plus and minus buttons
        Plus_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_plus.png);
                }}"""

        self.horaPlusBtn = QPushButton(self.BACKGROUND)
        self.horaPlusBtn.setGeometry(263, 404, 30, 30)
        self.horaPlusBtn.setFlat(True)    
        self.horaPlusBtn.setFocusPolicy(Qt.NoFocus)
        self.horaPlusBtn.setStyleSheet(Plus_style)

        """self.GMTPlusBtn = QPushButton(self.BACKGROUND)
        self.GMTPlusBtn.setGeometry(263, 457, 30, 30)
        self.GMTPlusBtn.setFlat(True)    
        self.GMTPlusBtn.setFocusPolicy(Qt.NoFocus)
        self.GMTPlusBtn.setStyleSheet(Plus_style)"""

#********************* minus Btns
        Minus_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_minus.png);
                }}"""

        self.horaMinusBtn = QPushButton(self.BACKGROUND)
        self.horaMinusBtn.setGeometry(90, 404, 30, 30)    
        self.horaMinusBtn.setFlat(True)    
        self.horaMinusBtn.setFocusPolicy(Qt.NoFocus)
        self.horaMinusBtn.setStyleSheet(Minus_style)

        """self.GMTMinusBtn = QPushButton(self.BACKGROUND)
        self.GMTMinusBtn.setGeometry(90, 457, 30, 30)    
        self.GMTMinusBtn.setFlat(True)    
        self.GMTMinusBtn.setFocusPolicy(Qt.NoFocus)
        self.GMTMinusBtn.setStyleSheet(Minus_style)"""

#**************************************************** 
#FECHA edit

        self.fechaActualLbl = QLabel(self.BACKGROUND)
        self.fechaActualLbl.setGeometry(92, 540, 388, 17)
        fechaLbl_style=f"""
                QLabel{{
                        font-size: 14px;
                        color: #1BC6D5;
                        qproperty-alignment: AlignLeft;
                }}"""
        self.fechaActualLbl.setStyleSheet(fechaLbl_style)

        self.fechaEdit = QDateEdit(self.BACKGROUND)
        self.fechaEdit.setGeometry(118, 567, 139, 24)
        self.fechaEdit.setCalendarPopup(True)
        self.fechaEdit.setDisplayFormat("dd/MM/yyyy")
        self.fechaEdit.setFocusPolicy(Qt.NoFocus)

        #************************************************************ Plus Btns
        self.fechaPlusBtn = QPushButton(self.BACKGROUND)
        self.fechaPlusBtn.setGeometry(263, 564, 30, 30)
        self.fechaPlusBtn.setFlat(True)
        self.fechaPlusBtn.setFocusPolicy(Qt.NoFocus)
        self.fechaPlusBtn.setStyleSheet(Plus_style)

#********************* minus Btns
        self.fechaMinusBtn = QPushButton(self.BACKGROUND)
        self.fechaMinusBtn.setGeometry(90, 564, 30, 30)
        self.fechaMinusBtn.setFlat(True)    
        self.fechaMinusBtn.setFocusPolicy(Qt.NoFocus)
        self.fechaMinusBtn.setStyleSheet(Minus_style)

#************************** Guardar Btn
        guardarStyle =f"""
                QPushButton {{
                        border-style: none;
                        background-repeat: no-repeat;
                        background-position: center center;
                        background-image: url({main.path}/icons/login_button.png);
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 18px;
                        color: #1BDDD2;
                }}
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/login_button_pressed.png);
                        color: #001532;
                }}"""
        self.guardar_Btn = QPushButton(self.BACKGROUND)
        self.guardar_Btn.setGeometry(QRect(280, 700, 180, 55))
        self.guardar_Btn.setFocusPolicy(Qt.NoFocus)
        self.guardar_Btn.setStyleSheet(guardarStyle)
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
        self.return_Btn.setFocusPolicy(Qt.NoFocus)

#**********************************************************************************

        QMetaObject.connectSlotsByName(form)
    # setupUi