#Fprincipal.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

#import fbUpload
import time
import threading
from datetime import datetime, date
#from CSB_MercurioR1.Pprincipal import Ui_form
#from CSB_MercurioR1.Fconfig import ConfigWindow

from Pprincipal import Ui_form
from Fconfig import ConfigWindow            #Config window 
from Fluminaria_led import LEDWindow        #Luminaria LED window (para dimerizar la luz)
from Fadvertencias import AdvertenciaWindow
from Fcalendar import CalendarWindow

import main         #to read the lightOnOff status
import json

counter = 0
lightPercent = 50

class MainWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)

        self.setWindowTitle("THORBELL")

        with open(main.statusFile) as f:
            data=json.load(f)                               #and loads json object

        with open(f"{main.path}/idioma/{data.get('Idioma')}.dat") as f:
            main.texto = json.load(f)

        #print("IDIOMA: ")
        #print(main.texto)
        main.lightOnOff = data.get("LED")
        main.lightPercent = data.get("LEDPWM")
        #Create all sub-windows, to call on them when different buttons are clicked.

        self.horizontalSlider.valueChanged.connect(self.Dial)
        self.horizontalSlider_2.valueChanged.connect(self.Dial2)

        self.config_Btn.clicked.connect(self.Config)
        self.calendario_Btn.clicked.connect(self.Calendar)

        self.luz_Btn.setAutoRepeat(True)
        self.luz_Btn.setAutoRepeatDelay(3000)
        #self.luz_Btn.pressed.connect(self.LuminariaLED_pressed)#handler.LuminariaLED_pressed)
        self.luz_Btn.clicked.connect(self.LuminariaLED_clicked)
        
        self.uv_Btn.setAutoRepeat(True)
        self.uv_Btn.setAutoRepeatDelay(3000)
        self.uv_Btn.clicked.connect(self.UVLED_clicked)

        self.advertencia_Btn.clicked.connect(self.advertenciaClicked)

        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

        if(main.lightOnOff):
            self.luz_Btn.setChecked=True
        else:
            self.luz_Btn.setChecked=False

        currentTime=datetime.now().strftime("%H:%M:%S")
        self.hora.setText(currentTime)
        today=date.today().strftime("%d/%m/%Y")
        self.fecha.setText(today)
        self.firstKey=False

        self.LED_label.setText(main.texto.get("luminariaLED"))
        self.UV_label.setText(main.texto.get("luminariaUV"))
        self.ModoEco_label.setText(main.texto.get("modoEco"))
        self.Rutina_label.setText(main.texto.get("rutina"))

        #Thread de 100 ms, para base de tiempo de ejecución. 
        #Corre en paralelo con la app
        self.ms100=0
        clock = threading.Thread(target=self.timer100ms,daemon=True)
        clock.start()
    #FIN init

#**********************************************************************************************
#Timer de 100 ms. Éste timer corre en paralelo con la app principal. 
#Aquí se lee el "status.dat", y se actualiza el estado de las salidas
#Cada un segundo se actualiza el reloj en pantalla.

    def timer100ms(self):           #recurrent timer - base de tiempo de 100ms para chekear estado de las cosas
        while(True):
            #revisa el estado de la luz led, y setea el botón de luz de acuerdo
            if(self.luz_Btn.isChecked() != main.lightOnOff):
                self.luz_Btn.toggle()
                self.status.update( { 'LED' : main.lightOnOff } )
                with open(main.statusFile, "w") as st:
                    json.dump(self.status, st)
            
            self.ms100 += 1
            if(self.ms100>10):
                self.ms100=0
                currentTime=datetime.now().strftime("%H:%M:%S")
                self.hora.setText(currentTime)
                today=date.today().strftime("%d/%m/%Y")
                self.fecha.setText(today)
                #self.luz_Btn.setChecked(main.lightOnOff)
            
                #La variable status contiene el estado global del equipo.
                #TODO: actualizar el estado de las salidas en base a lo leído
                #del archivo "status.dat"
                with open(main.statusFile) as st:
                    self.status=json.load(st)

                with open(main.usersFile) as us:
                    self.users=json.load(us)

                self.currentUser=self.users.get(self.status.get("screenUser"))
                #print(self.currentUser)
                self.user.setText(self.currentUser['name'])
            time.sleep(0.1)

#**********************************************************************************************
#Aquí está la interacción con el botón de luz.
#Está activado el auto-repeat, con un delay de 3seg. 
#Cuando se activa la señal de "clicked", se controla el estado del botón
#Si NO está "down" (es decir, se dejó de apretar, y fué un simple click),
#Se actualiza el valor de "main.lightOnOff", y se guarda en status.dat
#En cambio, si el botón está "down" (es decir, sigue presionado), la acción "click" saltó por
#autorepeat. En ese caso, se compara el estado "checked" del botón, contra el estado de 
#"main.lightOnOff", y se corrige si es necesario (por defecto con el click el botón cambia de 
# estado), y luego se muestra la ventana de configuración de iluminación LED
#Antes de invocar la ventana de configuración de LED, setea el botón de OnOff, y el porcentaje
#según lo almacenado en "main.lightPercent"
    def LuminariaLED_clicked(self):
        if(not self.luz_Btn.isDown()):
            main.lightOnOff=self.luz_Btn.isChecked()
            #Opens status file
            with open(main.statusFile) as f:
                data=json.load(f)                               #and loads json object
            data.update( { "LED": main.lightOnOff } )           #updates LED status
            with open(main.statusFile, "w") as f:               #And saves it to status File
                json.dump(data,f)                               #as an JSON object
        else:
            if(main.lightOnOff != self.luz_Btn.isChecked()):
                self.luz_Btn.toggle()

            self.ledWindow = LEDWindow()            
            self.ledWindow.show()
        

#**************************************************************************************


#**********************************************************************************************
#Aquí está la interacción con el botón de luz UV.
#Está activado el auto-repeat, con un delay de 3seg. 
#Cuando se activa la señal de "clicked", se controla el estado del botón
#Si NO está "down" (es decir, se dejó de apretar, y fué un simple click),
#Se actualiza el valor de "main.uvOnOff", y se guarda en status.dat
#En cambio, si el botón está "down" (es decir, sigue presionado), la acción "click" saltó por
#autorepeat. En ese caso, se compara el estado "checked" del botón, contra el estado de 
#"main.uvOnOff", y se corrige si es necesario (por defecto con el click el botón cambia de 
# estado), y luego se muestra la ventana de configuración de iluminación LED UV
#Antes de invocar la ventana de configuración de LED UV, setea el botón de OnOff, y el tiempo
#según lo almacenado en "main.uvTimer"
    def UVLED_clicked(self):
        if(not self.luz_Btn.isDown()):
            main.uvOnOff=self.uv_Btn.isChecked()
            #Opens status file
            with open(main.statusFile) as f:
                data=json.load(f)                               #and loads json object
            data.update( { "UVLED": main.uvOnOff } )           #updates UVLED status
            with open(main.statusFile, "w") as f:               #And saves it to status File
                json.dump(data,f)                               #as an JSON object
        else:
            if(main.uvOnOff != self.uv_Btn.isChecked()):
                self.uv_Btn.toggle()

            #TODO Set UV button in config window self.ledWindow.OnOffButton.setChecked(main.lightOnOff)          
            #TODO set UV timer in config window self.ledWindow.dialChange(main.lightPercent)
            #TODO Show UV config window self.ledWindow.show()
#**************************************************************************************************************


#**************************************************************************************************************
#Ventana de advertencia
    def advertenciaClicked(self):
        print("Show Advertencia")
        self.advertenciaWindow = AdvertenciaWindow()
        self.advertenciaWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
#Ventana de configuración
    def Config(self):
        self.configWindow = ConfigWindow()
        self.configWindow.show()

#**************************************************************************************************************
#Calendar window
    def Calendar(self):
        self.calendarWindow = CalendarWindow()
        self.calendarWindow.show()

#**************************************************************************************************************

#OLD test stuff
    def Upload(self):
        #fbUpload.upload()
        self.counter += 1
        self.label.setText(str(counter))

    def Decrease(self):
        self.counter -= 1
        self.label.setText(str(counter))

#**************************************************************************************************************
    def Dial(self):
        slider= self.horizontalSlider.value()
        self.label_2.setText(str(slider) + " %")
        stopValue= (slider)/100
    #       print("Slider value= " + str(stopValue))
        gradient = stopValue-0.05
        if(gradient < 0):
            gradient = 0
            stopValue = 0.05
        if(stopValue>1):
            stopValue=1
        if(gradient>1):
            gradient=1
                
        if(stopValue < 0.15 or stopValue > 0.85 ):
            color= (255, 0, 0, 145)
        elif(stopValue < 0.4 or stopValue > 0.6):
            color=(255,197,0,145)
        else:
            color=(51, 255, 151, 145)
        style=u"QFrame{\n"
        style += "	\n"
        style += "	border-radius: 138px;\n"
        style += "   background-image: url();\n"
        style += "	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:" 
        style += str(stopValue) + " rgba(255, 255, 255, 0), stop:" + str(gradient) + " rgba" + str(color) + ");\n"
        style += "}"
    #        print(style)
        self.Bar.setStyleSheet(style)

    def Dial2(self):
        slider= self.horizontalSlider_2.value()
        self.label_3.setText(str(slider) + " %")
        stopValue= (slider)/100
#        print("Slider value= " + str(stopValue))
        gradient = stopValue-0.05
        if(gradient < 0):
            gradient = 0
            stopValue = 0.05
        if(stopValue>1):
            stopValue=1
        if(gradient>1):
            gradient=1
            
        if(stopValue < 0.15 or stopValue > 0.85 ):
            color=(255, 0, 0, 145)
        elif(stopValue < 0.4 or stopValue > 0.6):
            color=(255,197,0,145)
        else:
            color=(51, 255, 151, 145)

        style=u"QFrame{\n"
        style += "	\n"
        style += "	border-radius: 138px;\n"
        style += "   background-image: url();\n"
        style += "	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:" 
        style += str(stopValue) + " rgba(255, 255, 255, 0), stop:" + str(gradient) + " rgba" + str(color) + ");\n"
        style += "}"
        self.Bar_2.setStyleSheet(style)

