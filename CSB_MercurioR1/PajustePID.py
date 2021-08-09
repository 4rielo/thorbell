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
                        background-position: center center;
                        background-image: url({main.path}/icons/login_button.png);
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 18px;
                        color: #1BDDD2;
                }}
                QPushButton:checked {{
                        background-image: url({main.path}/icons/login_button_pressed.png);
                        color: #001532;
                }}
                QLabel {{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 15px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        background: transparent;
                }}"""
        self.BACKGROUND.setStyleSheet(Background_Style)
        """El estilo de QPushButton se aplica al BACKGROUND, y se 
        hereda por todos los QPushButton que contiene, tanto en estado común, como 
        en estado "checked". No es necesario volver a especificar el estilo 
        de borde, la repetibilidad de imagen, o su posicion.
        """
#**************************************************** Tittle

        self.tittle = QLabel(self.BACKGROUND)
        self.tittle.setGeometry(QRect(0, 88, 480, 22))
        #self.tittle.setAttribute(Qt.WA_TranslucentBackground)
        tittle_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 19px;
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setGeometry(QRect(0, 88, 480, 22))
        #self.tittleGlow.setAttribute(Qt.WA_TranslucentBackground)
        tittleGlow_style=f"""
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 20px;
                }}"""
        self.tittleGlow.setStyleSheet(tittleGlow_style)
        
        self.Effect=QGraphicsBlurEffect()
        self.Effect.setBlurRadius(10)
        self.tittleGlow.setGraphicsEffect(self.Effect)

#**************************************************** HERE ARE THE infoLabels
        LabelsStyle = f"""
                QLabel{{
                        qproperty-alignment: AlignLeft;
                        }}"""

        self.toleranciaCalibrarLbl1 = QLabel(self.BACKGROUND)
        self.toleranciaCalibrarLbl1.setGeometry(QRect(100, 150, 120, 22))
        self.toleranciaCalibrarLbl1.setStyleSheet(LabelsStyle)

        self.tolCalibrarValue = QLabel(self.BACKGROUND)
        self.tolCalibrarValue.setGeometry(QRect(250, 150, 120, 22))
        self.tolCalibrarValue.setStyleSheet(LabelsStyle)

        self.toleranciaTrabajoLbl = QLabel(self.BACKGROUND)
        self.toleranciaTrabajoLbl.setGeometry(QRect(100, 180, 120, 22))
        self.toleranciaTrabajoLbl.setStyleSheet(LabelsStyle)

        self.tolTrabajoValue = QLabel(self.BACKGROUND)
        self.tolTrabajoValue.setGeometry(QRect(250, 180, 120, 22))
        self.tolTrabajoValue.setStyleSheet(LabelsStyle)

        self.limInferiorLbl = QLabel(self.BACKGROUND)
        self.limInferiorLbl.setGeometry(QRect(100, 210, 120, 22))
        self.limInferiorLbl.setStyleSheet(LabelsStyle)
        
        self.limInferiorValue = QLabel(self.BACKGROUND)
        self.limInferiorValue.setGeometry(QRect(250, 210, 120, 22))
        self.limInferiorValue.setStyleSheet(LabelsStyle)

        self.limSuperiorLbl = QLabel(self.BACKGROUND)
        self.limSuperiorLbl.setGeometry(QRect(100, 240, 120, 22))
        self.limSuperiorLbl.setStyleSheet(LabelsStyle)

        self.limSuperiorValue = QLabel(self.BACKGROUND)
        self.limSuperiorValue.setGeometry(QRect(250, 240, 120, 22))
        self.limSuperiorValue.setStyleSheet(LabelsStyle)

        self.constanteKLbl = QLabel(self.BACKGROUND)
        self.constanteKLbl.setGeometry(QRect(100, 300, 120, 22))
        self.constanteKLbl.setStyleSheet(LabelsStyle)
        
        self.constanteKValue = QLabel(self.BACKGROUND)
        self.constanteKValue.setGeometry(QRect(250, 300, 120, 22))
        self.constanteKValue.setStyleSheet(LabelsStyle)

        self.constanteTaoLbl = QLabel(self.BACKGROUND)
        self.constanteTaoLbl.setGeometry(QRect(100, 330, 120, 22))
        self.constanteTaoLbl.setStyleSheet(LabelsStyle)
        
        self.constanteTaoValue = QLabel(self.BACKGROUND)
        self.constanteTaoValue.setGeometry(QRect(250, 330, 120, 22))
        self.constanteTaoValue.setStyleSheet(LabelsStyle)

        self.constanteThetaLbl = QLabel(self.BACKGROUND)
        self.constanteThetaLbl.setGeometry(QRect(100, 360, 120, 22))
        self.constanteThetaLbl.setStyleSheet(LabelsStyle)
        
        self.constanteThetaValue = QLabel(self.BACKGROUND)
        self.constanteThetaValue.setGeometry(QRect(250, 360, 120, 22))
        self.constanteThetaValue.setStyleSheet(LabelsStyle)
        
        self.setPointLbl = QLabel(self.BACKGROUND)
        self.setPointLbl.setGeometry(QRect(100, 390, 120, 22))
        self.setPointLbl.setStyleSheet(LabelsStyle)
        
        self.setPointValue = QLabel(self.BACKGROUND)
        self.setPointValue.setGeometry(QRect(250, 390, 120, 22))
        self.setPointValue.setStyleSheet(LabelsStyle)
#**************************************************** HERE ARE THE BUTTONS
        guardarStyle =f"""
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/login_button_pressed.png);
                        color: #001532;
                }}"""
        self.guardar_Btn = QPushButton(self.BACKGROUND)
        self.guardar_Btn.setGeometry(QRect(280, 700, 180, 55))
        self.guardar_Btn.setFocusPolicy(Qt.NoFocus)
        self.guardar_Btn.setStyleSheet(guardarStyle)

# Motor de Bajada button
        """self.motorBajadaOnOff_Btn = QPushButton(self.BACKGROUND)
        self.motorBajadaOnOff_Btn.setGeometry(QRect(20, 500, 180, 55))
        self.motorBajadaOnOff_Btn.setFocusPolicy(Qt.NoFocus)
        self.motorBajadaOnOff_Btn.setCheckable(True)"""

        plus_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/up_released.png); 
                }}
                QPushButton:pressed {{
                        background-image: url({main.path}/icons/up_pressed.png); 
                }}"""

        minus_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/down_released.png); 
                }}
                QPushButton::pressed {{
                        background-image: url({main.path}/icons/down_pressed.png); 
                }}"""

        self.selectionMas_Btn = QPushButton(self.BACKGROUND)
        self.selectionMas_Btn.setGeometry(QRect(300, 500, 60, 40))
        self.selectionMas_Btn.setStyleSheet(plus_Button)
        self.selectionMas_Btn.setFocusPolicy(Qt.NoFocus)

        self.selectionMenos_Btn = QPushButton(self.BACKGROUND)
        self.selectionMenos_Btn.setGeometry(QRect(120, 500, 60, 40))
        self.selectionMenos_Btn.setStyleSheet(minus_Button)
        self.selectionMenos_Btn.setFocusPolicy(Qt.NoFocus)

        self.tolCalibrarRadioBox = QRadioButton(self.BACKGROUND)
        self.tolCalibrarRadioBox.setGeometry(QRect(30,150,20,20))

        self.tolTrabajoRadioBox = QRadioButton(self.BACKGROUND)
        self.tolTrabajoRadioBox.setGeometry(QRect(30,180,20,20))

        self.limInferiorRadioBox = QRadioButton(self.BACKGROUND)
        self.limInferiorRadioBox.setGeometry(QRect(30,210,20,20))

        self.limSuperiorRadioBox = QRadioButton(self.BACKGROUND)
        self.limSuperiorRadioBox.setGeometry(QRect(30,240,20,20))

        self.constanteKRadioBox = QRadioButton(self.BACKGROUND)
        self.constanteKRadioBox.setGeometry(QRect(30,300,20,20))

        self.constanteTaoRadioBox = QRadioButton(self.BACKGROUND)
        self.constanteTaoRadioBox.setGeometry(QRect(30,330,20,20))

        self.constanteThetaRadioBox = QRadioButton(self.BACKGROUND)
        self.constanteThetaRadioBox.setGeometry(QRect(30,360,20,20))

        self.setPointRadioBox = QRadioButton(self.BACKGROUND)
        self.setPointRadioBox.setGeometry(QRect(30,390,20,20))
#back button
        return_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/back.png); 
                }}"""
        self.return_Btn = QPushButton(self.BACKGROUND)
        self.return_Btn.setGeometry(QRect(41, 700, 38, 37))
        self.return_Btn.setFlat(True)
        self.return_Btn.setStyleSheet(return_Button)
        self.return_Btn.setFocusPolicy(Qt.NoFocus)


#**********************************************************************************

        #self.BACKGROUND.raise_()

        #self.tittle.raise_()

        QMetaObject.connectSlotsByName(form)