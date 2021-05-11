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
                	background-position: center center;
                }}
                QPushButton {{
                        border-style: none;
                        background-repeat: no-repeat; 
                        background-position: center center
                }}
                QLabel {{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        color: white;
                        background: transparent;
                        qproperty-alignment: AlignCenter;
                }} 
                """
        self.BACKGROUND.setStyleSheet(Background_Style)
        """El estilo de QPushButton se aplica al BACKGROUND, y se 
        hereda por todos los QPushButton que contiene, tanto en estado común, como 
        en estado "checked". No es necesario volver a especificar el estilo 
        de borde, la repetibilidad de imagen, o su posicion.
        """
#**************************************************** HERE ARE THE BUTTONS
#Rutina button
        self.rutina_Btn = QPushButton(self.BACKGROUND)
        self.rutina_Btn.setObjectName(u"rutina_Btn")
        self.rutina_Btn.setGeometry(QRect(68, 133, 100, 100))
        self.rutina_Btn.setCheckable(True)
        self.rutina_Btn.setFlat(True)
        RUTINA_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/routine_off.png); 
                        }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/routine_on.png); 
                }}"""
        self.rutina_Btn.setStyleSheet(RUTINA_Button)
        self.rutina_Btn.focusPolicy = Qt.NoFocus
        
#ECO mode button
        self.eco_Btn = QPushButton(self.BACKGROUND)
        self.eco_Btn.setObjectName(u"eco_Btn")
        self.eco_Btn.setGeometry(QRect(312, 133, 100, 100))
        self.eco_Btn.setCheckable(True)
        self.eco_Btn.setFlat(True)
        ECO_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/eco_off.png); 
                }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/eco_on.png); 
                }}"""
        self.eco_Btn.setStyleSheet(ECO_Button)
        self.eco_Btn.focusPolicy = Qt.NoFocus

#LED light button
        self.luz_Btn = QPushButton(self.BACKGROUND)
        self.luz_Btn.setObjectName(u"luz_Btn")
        self.luz_Btn.setGeometry(QRect(68, 583, 100, 100))
        self.luz_Btn.setCheckable(True)
        self.luz_Btn.setFlat(True)
        LUZ_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/led_off.png); 
                }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/led_on.png); 
                }}"""
        self.luz_Btn.setStyleSheet(LUZ_Button)
        self.luz_Btn.focusPolicy = Qt.NoFocus
        
#UV light button
        self.uv_Btn = QPushButton(self.BACKGROUND)
        self.uv_Btn.setObjectName(u"uv_Btn")
        self.uv_Btn.setGeometry(QRect(312, 583, 100, 100))
        self.uv_Btn.setCheckable(True)
        self.uv_Btn.setFlat(True)
        UV_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/uv_off.png); 
                }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/uv_on.png); 
                }}"""
        self.uv_Btn.setStyleSheet(UV_Button)
        self.uv_Btn.focusPolicy = Qt.NoFocus

#Puerta button
        self.door_Btn = QPushButton(self.BACKGROUND)
        self.door_Btn.setObjectName(u"door_Btn")
        self.door_Btn.setGeometry(QRect(190, 640, 100, 100))
        self.door_Btn.setCheckable(True)
        self.door_Btn.setFlat(True)
        door_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/puerta_abierta.png); 
                }}"""
        self.door_Btn.setStyleSheet(door_Button)
        self.door_Btn.focusPolicy = Qt.NoFocus        

#Config Button
        self.config_Btn = QPushButton(self.BACKGROUND)
        self.config_Btn.setObjectName(u"config_Btn")
        self.config_Btn.setFlat(True)
        self.config_Btn.setGeometry(QRect(362, 23, 38, 38))
        Config_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/configuracion.png);
                }}"""
        self.config_Btn.setStyleSheet(Config_style)
        self.config_Btn.focusPolicy = Qt.NoFocus

#Alert/advertencia button
        self.advertencia_Btn = QPushButton(self.BACKGROUND)
        self.advertencia_Btn.setObjectName(u"advertencia_Btn")
        self.advertencia_Btn.setGeometry(QRect(362, 74, 38, 38))
        self.advertencia_Btn.setFlat(True)
        Alerta_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/alerta.png);
                }}"""
        self.advertencia_Btn.setStyleSheet(Alerta_style)
        self.advertencia_Btn.focusPolicy = Qt.NoFocus

#Reloj button
        self.reloj_Btn = QPushButton(self.BACKGROUND)
        self.reloj_Btn.setObjectName(u"reloj_Btn")
        self.reloj_Btn.setGeometry(QRect(73, 24, 34, 36))
        self.advertencia_Btn.setFlat(True)
        Reloj_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/reloj.png);
                }}"""
        self.reloj_Btn.setStyleSheet(Reloj_style)
        self.reloj_Btn.focusPolicy = Qt.NoFocus

        
#Calendario button
        self.calendario_Btn = QPushButton(self.BACKGROUND)
        self.calendario_Btn.setObjectName(u"calendario_Btn")
        self.calendario_Btn.setGeometry(QRect(71, 74, 39, 37))
        self.calendario_Btn.setFlat(True)
        Calendario_style=f"""
                QPushButton {{
                        background-image: url({main.path}/icons/calendario.png);
                }}"""
        self.calendario_Btn.setStyleSheet(Calendario_style)
        self.calendario_Btn.focusPolicy = Qt.NoFocus

#**************************************************************************

        self.horizontalSlider = QSlider(self.BACKGROUND)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(200, 50, 100, 20))
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.horizontalSlider_2 = QSlider(self.BACKGROUND)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(200, 720, 100, 20))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

#************************************************Here are the center round progress bar indicators
        Bar_InitialStyle="""
                QFrame{
                	background-image: url();
                	border-radius: 138px;
                	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 145), stop:0.05 rgba(255, 255, 255, 0));
                }"""

        self.TopProgressBar = QFrame(self.BACKGROUND)
        self.TopProgressBar.setObjectName(u"TopProgressBar")
        self.TopProgressBar.setGeometry(QRect(50, 175, 380, 231))  #y0 = 201
        self.TopProgressBar.setAutoFillBackground(True)
        TopHalf_style=f"""
                QFrame{{
                	background-image: url({main.path}/images/semi_circulo_superior.png);
                }}"""
        self.TopProgressBar.setStyleSheet(TopHalf_style)
        self.TopProgressBar.setFrameShape(QFrame.NoFrame)
        self.TopProgressBar.setFrameShadow(QFrame.Plain)

        self.Bar = QFrame(self.TopProgressBar)
        self.Bar.setObjectName(u"Bar")
        self.Bar.setGeometry(QRect(52, 93, 276, 276))
        self.Bar.setStyleSheet(Bar_InitialStyle)
        self.Bar.setFrameShape(QFrame.NoFrame)
        self.Bar.setFrameShadow(QFrame.Raised)        

        self.label_2 = QLabel(self.TopProgressBar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 190, 200, 50))
        font = QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        #self.label_2.setAttribute(Qt.WA_TranslucentBackground)
        #self.label_2.setStyleSheet(u"color: white;")
        #self.label_2.setAlignment(Qt.AlignCenter)

        self.BottomProgressBar = QFrame(self.BACKGROUND)
        self.BottomProgressBar.setObjectName(u"BottomProgressBar")
        self.BottomProgressBar.setGeometry(QRect(50, 420, 380, 231))               #y0 = 445
        BottomHalf_style=f"""
                QFrame{{
                	background-image: url({main.path}/images/semi_circulo_inferior.png);
                	background-repeat: no-repeat;
                	background-position: bottom center;
                }}"""
        self.BottomProgressBar.setStyleSheet(BottomHalf_style)
        self.BottomProgressBar.setFrameShape(QFrame.NoFrame)
        self.BottomProgressBar.setFrameShadow(QFrame.Raised)
        self.Bar_2 = QFrame(self.BottomProgressBar)
        self.Bar_2.setObjectName(u"Bar_2")
        self.Bar_2.setGeometry(QRect(52, -138, 271, 276))
        self.Bar_2.setStyleSheet(Bar_InitialStyle)
        self.Bar_2.setFrameShape(QFrame.NoFrame)
        self.Bar_2.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.BottomProgressBar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, -10, 200, 50))
        self.label_3.setFont(font)
        #self.label_3.setAttribute(Qt.WA_TranslucentBackground)
        #self.label_3.setStyleSheet(u"color: white;")
        #self.label_3.setAlignment(Qt.AlignCenter)
#**************************************************************************

        self.wind_icon = QFrame(self.BACKGROUND)
        self.wind_icon.setObjectName(u"wind_icon")
        self.wind_icon.setGeometry(QRect(218, 180, 44, 25))
        self.wind_icon.setFrameShape(QFrame.NoFrame)
        self.wind_icon.setFrameShadow(QFrame.Raised)
        Wind_style=f"""
                QFrame {{
                	background-image: url({main.path}/images/viento.png);
                }}"""
        self.wind_icon.setStyleSheet(Wind_style)
        self.wind_icon.setVisible(False)

        self.wind_icon2 = QFrame(self.BACKGROUND)
        self.wind_icon2.setObjectName(u"wind_icon2")
        self.wind_icon2.setGeometry(QRect(218, 676, 44, 25))
        self.wind_icon2.setFrameShape(QFrame.NoFrame)
        self.wind_icon2.setFrameShadow(QFrame.Raised)        
        self.wind_icon2.setStyleSheet(Wind_style)
        self.wind_icon2.setVisible(False)

#************************ Here are the labels indicating some text ***************************
        self.hora = QLabel(self.BACKGROUND)
        self.hora.setObjectName(u"hora")
        self.hora.setGeometry(QRect(118, 34, 60, 16))
        Hora_style=f"""
                QLabel{{
                        font-size: 13px;
                }}"""
        self.hora.setStyleSheet(Hora_style)

        self.fecha = QLabel(self.BACKGROUND)
        self.fecha.setObjectName(u"fecha")
        self.fecha.setGeometry(QRect(118, 85, 75, 16))
        Fecha_style=f"""
                QLabel{{
                        font-size: 13px;
                }}"""
        self.fecha.setStyleSheet(Fecha_style)

        self.user = QLabel(self.BACKGROUND)
        self.user.setGeometry(QRect(400, 785, 75, 15))
        user_style=f"""
                QLabel{{
                        font-size: 13px;
                        qproperty-alignment: AlignRight;
                }}"""
        self.user.setStyleSheet(user_style)

#************************ Here are the labels indicating some text ***************************


        self.ModoEco_label = QLabel(self.BACKGROUND)
        self.ModoEco_label.setObjectName(u"ModoEco_label")
        self.ModoEco_label.setGeometry(QRect(312, 229, 100, 12))
        ModoECO_style=f"""
                QLabel{{
                        font-size: 10px;
                }}"""
        self.ModoEco_label.setStyleSheet(ModoECO_style)

        self.Rutina_label = QLabel(self.BACKGROUND)
        self.Rutina_label.setObjectName(u"Rutina_label")
        self.Rutina_label.setGeometry(QRect(68, 229, 100, 12))
        Rutina_style= f"""
                QLabel{{
                        font-size: 10px;
                }}"""
        self.Rutina_label.setStyleSheet(Rutina_style)

        self.LED_label = QLabel(self.BACKGROUND)
        self.LED_label.setObjectName(u"LED_label")
        self.LED_label.setGeometry(QRect(68, 736, 100, 24))
        LED_style= f"""
                QLabel{{
                        font-size: 10px;
                }}"""
        self.LED_label.setStyleSheet(LED_style)

        self.UV_label = QLabel(self.BACKGROUND)
        self.UV_label.setObjectName(u"UV_label")
        self.UV_label.setGeometry(QRect(312, 736, 100, 24))
        UV_style=f"""
                QLabel{{
                        font-size: 10px;
                }}"""                
        self.UV_label.setStyleSheet(UV_style)
#**********************************************************************************

        self.BACKGROUND.raise_()
        
        self.TopProgressBar.raise_()
        self.BottomProgressBar.raise_()
        
        self.hora.raise_()
        self.fecha.raise_()
        self.wind_icon2.raise_()
        self.wind_icon.raise_()
        
        self.ModoEco_label.raise_()
        self.Rutina_label.raise_()
        self.LED_label.raise_()
        self.UV_label.raise_()
        
        self.horizontalSlider.raise_()
        self.horizontalSlider_2.raise_()

        self.rutina_Btn.raise_()
        self.eco_Btn.raise_()
        self.luz_Btn.raise_()
        self.uv_Btn.raise_()
        self.config_Btn.raise_()
        self.advertencia_Btn.raise_()
        self.reloj_Btn.raise_()
        self.calendario_Btn.raise_()


        QMetaObject.connectSlotsByName(form)
    # setupUi
