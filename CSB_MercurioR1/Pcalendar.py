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

#**************************************************** ON OFF
        ONOFF_btnStyle = f"""
                QPushButton {{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        background-image: url({main.path}/icons/calendar_circle.png);
                        font-size: 28px;
                        color: #34E0D6;
                }}
                QPushButton:checked {{
                        background-image: url({main.path}/icons/calendar_circlePressed.png);
                        color: #001C42;
                }}
                """
        
        self.onBtn = QPushButton(self.BACKGROUND)
        self.onBtn.setGeometry(329, 213, 100, 100)
        self.onBtn.setStyleSheet(ONOFF_btnStyle)
        self.onBtn.setFocusPolicy(Qt.NoFocus)
        self.onBtn.setFlat(True)
        self.onBtn.setCheckable(True)
        self.onBtn.setText("On")

        self.offBtn = QPushButton(self.BACKGROUND)
        self.offBtn.setGeometry(50, 213, 100, 100)
        self.offBtn.setStyleSheet(ONOFF_btnStyle)
        self.offBtn.setFocusPolicy(Qt.NoFocus)
        self.offBtn.setFlat(True)
        self.offBtn.setCheckable(True)
        self.offBtn.setText("Off")

        self.uvBtn = QPushButton(self.BACKGROUND)
        self.uvBtn.setGeometry(190, 213, 100, 100)
        self.uvBtn.setStyleSheet(ONOFF_btnStyle)
        self.uvBtn.setFocusPolicy(Qt.NoFocus)
        self.uvBtn.setFlat(True)
        self.uvBtn.setText("UV")

#**************************************************** INICIO
        self.inicioLbl = QLabel(self.BACKGROUND)
        self.inicioLbl.setGeometry(92, 379, 388, 17)
        inicioLbl_style=f"""
                QLabel{{
                        font-size: 14px;
                        color: #1BC6D5;
                        qproperty-alignment: AlignLeft;
                }}"""
        self.inicioLbl.setStyleSheet(inicioLbl_style)

        self.initDateEdit = QDateEdit(self.BACKGROUND)
        self.initDateEdit.setGeometry(118, 407, 139, 24)
        self.initDateEdit.setCalendarPopup(True)
        self.initDateEdit.setDisplayFormat("dd/MM/yyyy")
        self.initDateEdit.setFocusPolicy(Qt.NoFocus)

        self.initTimeEdit = QTimeEdit(self.BACKGROUND)
        self.initTimeEdit.setGeometry(118, 460, 139, 24)
        #self.initTimeEdit.setCalendarPopup(True)
        self.initTimeEdit.setDisplayFormat("hh:mm")
        self.initTimeEdit.setFocusPolicy(Qt.NoFocus)
        self.initTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

#plus and minus buttons

        self.initDatePlusBtn = QPushButton(self.BACKGROUND)
        self.initDatePlusBtn.setGeometry(263, 404, 30, 30)    
        self.initDatePlusBtn.setCheckable(True)
        self.initDatePlusBtn.setFlat(True)    
        initDatePlus_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_plus.png);
                }}"""
        self.initDatePlusBtn.setStyleSheet(initDatePlus_style)
        self.initDatePlusBtn.setFocusPolicy(Qt.NoFocus)

        self.initDateMinusBtn = QPushButton(self.BACKGROUND)
        self.initDateMinusBtn.setGeometry(90, 404, 30, 30)    
        self.initDateMinusBtn.setCheckable(True)
        self.initDateMinusBtn.setFlat(True)    
        initDateMinus_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_minus.png);
                }}"""
        self.initDateMinusBtn.setStyleSheet(initDateMinus_style)
        self.initDateMinusBtn.setFocusPolicy(Qt.NoFocus)

#INIT TIME plus and minus buttons 

        self.initTimePlusBtn = QPushButton(self.BACKGROUND)
        self.initTimePlusBtn.setGeometry(263, 457, 30, 30)    
        self.initTimePlusBtn.setCheckable(True)
        self.initTimePlusBtn.setFlat(True)    
        initTimePlusBtn_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_plus.png);
                }}"""
        self.initTimePlusBtn.setStyleSheet(initTimePlusBtn_style)
        self.initTimePlusBtn.setFocusPolicy(Qt.NoFocus)

        self.initTimeMinusBtn = QPushButton(self.BACKGROUND)
        self.initTimeMinusBtn.setGeometry(90, 457, 30, 30)    
        self.initTimeMinusBtn.setCheckable(True)
        self.initTimeMinusBtn.setFlat(True)    
        initTimeMinusBtn_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_minus.png);
                }}"""
        self.initTimeMinusBtn.setStyleSheet(initTimeMinusBtn_style)
        self.initTimeMinusBtn.setFocusPolicy(Qt.NoFocus)

#**************************************************** 

#**************************************************** 
        self.endLbl = QLabel(self.BACKGROUND)
        self.endLbl.setGeometry(92, 540, 388, 17)
        endLbl_style=f"""
                QLabel{{
                        font-size: 14px;
                        color: #1BC6D5;
                        qproperty-alignment: AlignLeft;
                }}"""
        self.endLbl.setStyleSheet(endLbl_style)

        self.endDateEdit = QDateEdit(self.BACKGROUND)
        self.endDateEdit.setGeometry(118, 567, 139, 24)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDisplayFormat("dd/MM/yyyy")
        self.endDateEdit.setFocusPolicy(Qt.NoFocus)

        self.endTimeEdit = QTimeEdit(self.BACKGROUND)
        self.endTimeEdit.setGeometry(118, 620, 139, 24)
        #self.endTimeEdit.setCalendarPopup(True)
        self.endTimeEdit.setDisplayFormat("hh:mm")
        self.endTimeEdit.setFocusPolicy(Qt.NoFocus)
        self.endTimeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)

#plus and minus buttons

        self.endDatePlusBtn = QPushButton(self.BACKGROUND)
        self.endDatePlusBtn.setGeometry(263, 564, 30, 30)    
        self.endDatePlusBtn.setCheckable(True)
        self.endDatePlusBtn.setFlat(True)    
        endDatePlusBtn_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_plus.png);
                }}"""
        self.endDatePlusBtn.setStyleSheet(endDatePlusBtn_style)
        self.endDatePlusBtn.setFocusPolicy(Qt.NoFocus)

        self.endDateMinusBtn = QPushButton(self.BACKGROUND)
        self.endDateMinusBtn.setGeometry(90, 564, 30, 30)    
        self.endDateMinusBtn.setCheckable(True)
        self.endDateMinusBtn.setFlat(True)    
        endDateMinusBtn_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_minus.png);
                }}"""
        self.endDateMinusBtn.setStyleSheet(endDateMinusBtn_style)
        self.endDateMinusBtn.setFocusPolicy(Qt.NoFocus)

#END TIME plus and minus buttons 

        self.endTimePlusBtn = QPushButton(self.BACKGROUND)
        self.endTimePlusBtn.setGeometry(263, 618, 30, 30)    
        self.endTimePlusBtn.setCheckable(True)
        self.endTimePlusBtn.setFlat(True)    
        endTimePlusBtn_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_plus.png);
                }}"""
        self.endTimePlusBtn.setStyleSheet(endTimePlusBtn_style)
        self.endTimePlusBtn.focusPolicy = Qt.NoFocus

        self.endTimeMinusBtn = QPushButton(self.BACKGROUND)
        self.endTimeMinusBtn.setGeometry(90, 618, 30, 30)    
        self.endTimeMinusBtn.setCheckable(True)
        self.endTimeMinusBtn.setFlat(True)    
        endTimeMinusBtn_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendar_minus.png);
                }}"""
        self.endTimeMinusBtn.setStyleSheet(endTimeMinusBtn_style)
        self.endTimeMinusBtn.focusPolicy = Qt.NoFocus

#**************************************************** 

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

        #self.BACKGROUND.raise_()


        #self.return_Btn.raise_()

        QMetaObject.connectSlotsByName(form)
    # setupUi