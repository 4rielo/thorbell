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
                QLabel{{
                        font-family: url({main.path}/fonts/Montserrat-Regular.ttf);
                        font-size: 15px;
                        color: white;
                        qproperty-alignment: AlignCenter;
                        background: transparent;
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
                }}"""
        self.tittle.setStyleSheet(tittle_style)

        self.tittleGlow = QLabel(self.BACKGROUND)
        self.tittleGlow.setObjectName(u"tittleGlow")
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


#**************************************************** HERE ARE THE BUTTONS
        """#UPDATE button
        self.update_Btn = QPushButton(self.BACKGROUND)
        self.update_Btn.setObjectName(u"update_Btn")
        self.update_Btn.setGeometry(QRect(290, 700, 100, 100))
        self.update_Btn.setCheckable(True)
        self.update_Btn.setFlat(True)"""
        UPDATE_Button = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/routine_off.png); 
                }} 
                QPushButton:checked{{
                        background-image: url({main.path}/icons/routine_on.png); 
                }}"""
        """self.update_Btn.setStyleSheet(UPDATE_Button)
        self.update_Btn.setFocusPolicy(Qt.NoFocus)"""

#USB button
        usb_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/usb.png);
                }}"""
        
        """self.usb_Btn = QPushButton(self.BACKGROUND)
        self.usb_Btn.setFixedSize(76, 48)
        self.usb_Btn.setStyleSheet(usb_BtnStyle)
        self.usb_Btn.setFocusPolicy(Qt.NoFocus)

        self.usbLabel = QLabel(self.BACKGROUND)
        self.usbLabel.setFixedSize(76, 16)
        #self.usbLabel.setAttribute(Qt.WA_TranslucentBackground)"""

#ComboBox
        languageBoxStyle = f"""
                QComboBox{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 25px;
                        color: white;
                        background-color: darkblue;
                        border: 2px solid darkgray;
		    	}}
		QComboBox QAbstractItemView{{
                        font-family: url({main.path}/fonts/Montserrat-SemiBold.ttf);
                        font-size: 25px;
			background-color: rgb(20,20,75);
			color: white;
			selection-background-color: rgb(30,30,150);
			selection-color: white;	
		}}"""
        self.LanguageBox = QComboBox(self.BACKGROUND)
        self.LanguageBox.setGeometry(140,520,200,35)
        self.LanguageBox.setStyleSheet(languageBoxStyle)

#Language button
        language_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/idioma.png);
                }}"""
        self.language_Btn = QPushButton(self.BACKGROUND)
        self.language_Btn.setGeometry(QRect(138,288,75,75))
        self.language_Btn.setStyleSheet(language_BtnStyle)
        self.language_Btn.setFocusPolicy(Qt.NoFocus)
        self.language_Btn.setCheckable(True)

        self.languageLabel = QLabel(self.BACKGROUND)
        self.languageLabel.setGeometry(QRect(138,363,76, 20))

#Info Button
        info_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/info.png);
                }}"""
        self.info_Btn = QPushButton(self.BACKGROUND)
        self.info_Btn.setObjectName(u"info_Btn")
        self.info_Btn.setGeometry(QRect(266,288,75,75))
        self.info_Btn.setStyleSheet(info_BtnStyle)
        self.info_Btn.setFocusPolicy(Qt.NoFocus)

        self.infoLabel = QLabel(self.BACKGROUND)
        self.infoLabel.setGeometry(QRect(266,363,75, 20))

        glowSize=f"""
                QLabel{{
                        font-size: 14px;
                }}"""
        """self.infoLabel_Glow = QLabel(self.BACKGROUND)
        self.infoLabel_Glow.setFixedSize(76, 16)
        self.infoLabel_Glow.setStyleSheet(glowSize)
        self.infoGlow=QGraphicsBlurEffect()
        self.infoGlow.setBlurRadius(10)
        self.infoLabel_Glow.setGraphicsEffect(self.infoGlow)"""

#TurnOf Button
        turnOff_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/turn_off.png);
                }}"""
        self.turnOff_Btn = QPushButton(self.BACKGROUND)
        self.turnOff_Btn.setGeometry(QRect(266,400,75,75))
        self.turnOff_Btn.setStyleSheet(turnOff_BtnStyle)
        self.turnOff_Btn.setFocusPolicy(Qt.NoFocus)

        self.turnOffLabel = QLabel(self.BACKGROUND)
        self.turnOffLabel.setGeometry(QRect(266,475,75,20))

        glowSize=f"""
                QLabel{{
                        font-size: 14px;
                }}"""
        """self.turnOffLabel_Glow = QLabel(self.BACKGROUND)
        self.turnOffLabel_Glow.setFixedSize(76, 16)
        self.turnOffLabel_Glow.setStyleSheet(glowSize)
        self.turnOffGlow=QGraphicsBlurEffect()
        self.turnOffGlow.setBlurRadius(10)
        self.turnOffLabel_Glow.setGraphicsEffect(self.infoGlow)"""

#Login Button
        login_BtnStyle = f"""
                QPushButton {{
                        background-image: url({main.path}/icons/login.png);
                }}"""
        self.login_Btn = QPushButton(self.BACKGROUND)
        self.login_Btn.setObjectName(u"login_Btn")
        self.login_Btn.setGeometry(QRect(138,400,75,75))
        self.login_Btn.setStyleSheet(login_BtnStyle)
        self.login_Btn.setFocusPolicy(Qt.NoFocus)

        self.loginLabel = QLabel(self.BACKGROUND)
        self.loginLabel.setGeometry(QRect(138,475,75,20))
        #self.loginLabel.setAttribute(Qt.WA_TranslucentBackground)

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

        self.BACKGROUND.raise_()

        self.tittle.raise_()

        QMetaObject.connectSlotsByName(form)