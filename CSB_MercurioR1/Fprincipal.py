#Fprincipal.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
import threading
import requests
import json
from datetime import datetime, date

from Pprincipal import Ui_form              #El formulario descriptivo de qué contiene ésta ventana
from Fconfig import ConfigWindow            #Config window 
from Fluminaria_led import LEDWindow        #Luminaria LED window (para dimerizar la luz)
from Fluminaria_ledUV import UVWindow       #Luminaria UV window (para configurar un timer de apagado)
from Fadvertencias import AdvertenciaWindow #Advertencia window (Muestra las advertencias)
from Fcalendar import CalendarWindow        #Calendario, setea hora de inicio y fin de rutina y/o luz UV
from Fclock import ClockWindow              #Setea fecha, hora y uso horario

#import FfirebaseUpload

import main         #to read the lightOnOff status


class MainWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)

        self.setWindowTitle("THORBELL")

        #Obtiene el estado global del servidor de estado
        response = requests.get(f"{main.localhost}/status").text
        self.status = json.loads(str(response))

        #Idioma almacenado en el estado del equipo
        with open(f"{main.path}/idioma/{self.status.get('Idioma')}.dat") as f:
            main.texto = json.load(f)

        #Estado inicial de las variables
        main.lightOnOff = self.status.get("LED_Light")
        main.lightPercent = self.status.get("LEDPWM")
        main.uvOnOff = self.status.get("UV_Light")
        main.UV_Timer=self.status.get("UV_Timer")
        main.UV_TimerEnable= self.status.get("UV_TimerEnable")

        #Create all sub-windows, to call on them when different buttons are clicked.

        #self.horizontalSlider.valueChanged.connect(self.Dial)
        #self.horizontalSlider_2.valueChanged.connect(self.Dial2)

        #Botón de configuración, cuando se clickea, conecta con "Config()""
        self.config_Btn.clicked.connect(self.Config)
        #Botón de calendario, cuando se clickea, conecta con "Calendar()"
        self.calendario_Btn.clicked.connect(self.Calendar)
        #Botón de reloj, cuando se clickea, conecta con "Clock()"
        self.reloj_Btn.clicked.connect(self.Clock)
      

        #Botón de luz LED, cuando se clickea, conecta con "LuminariaLED_clicked()"
        #el autorepeat es para habilitar el sub-menú manteniendo presionado.
        #El autoRepeatDelay es el tiempo que se debe mantener presionado
        #para ingresar al sub-menú de dicho pulsador
        self.luz_Btn.setAutoRepeat(True)
        self.luz_Btn.setAutoRepeatDelay(3000)
        self.luz_Btn.clicked.connect(self.LuminariaLED_clicked)
        
        #Botón de luz UV, cuando se clickea, conecta con "UVLED_clicked()"
        #el autorepeat es para habilitar el sub-menú manteniendo presionado.
        #El autoRepeatDelay es el tiempo que se debe mantener presionado
        #para ingresar al sub-menú de dicho pulsador
        self.uv_Btn.setAutoRepeat(True)
        self.uv_Btn.setAutoRepeatDelay(3000)
        self.uv_Btn.clicked.connect(self.UVLED_clicked)

        #Botón de advertencias, cuando se clickea, conecta con "advertenciaClicked()""
        self.advertencia_Btn.clicked.connect(self.advertenciaClicked)

        self.setWindowFlags(PySide2.QtCore.Qt.FramelessWindowHint) 

        #Según lo obtenido de "status.dat", setea el estado inicial de la luz LED
        #(y el estado inicial del pulsador correspondiente)
        self.luz_Btn.setChecked(main.lightOnOff)
        
        #Según lo obtenido de "status.dat", setea el estado inicial de la luz LED
        #(y el estado inicial del pulsador correspondiente)
        self.luz_Btn.setChecked(main.uvOnOff)

        #Muestra fecha y hora actual al momento de iniciar. 
        #ésto se actualiza cada 1 segundo en el timer de 100ms
        currentTime=datetime.now().strftime("%H:%M:%S")
        self.hora.setText(currentTime)
        today=date.today().strftime("%d/%m/%Y")
        self.fecha.setText(today)

        #Pone los textos de los pulsadores de acuerdo al idioma elegido
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


    def UpdateData(self, payload):
        self.firebaseLbl.setText(payload)
#**********************************************************************************************
# Timer de 100 ms. Éste timer corre en paralelo con la app principal. 
# Aquí se lee el "status.dat", y se actualiza el estado de las salidas
# Cada un segundo se actualiza el reloj en pantalla.

    def timer100ms(self):           #recurrent timer - base de tiempo de 100ms para chekear estado de las cosas
        while(True):
            #revisa el estado de la luz led, y setea el botón de luz de acuerdo
            #Compara contra "main.ligthOnOff", ya que éste valor se modifica
            #dentro del menú de LuminariaLED
            if(self.luz_Btn.isChecked() != main.lightOnOff):
                self.luz_Btn.toggle()
            if(self.uv_Btn.isChecked() != main.uvOnOff):
                self.uv_Btn.toggle()
            self.ms100 += 1

            #Pasó 1 segundo
            if(self.ms100>10):
                self.ms100=0

                #Pide la hora actual a microservicios (server en localhost:8085)
                currentTimeDate = requests.get(f"{main.localhost}/status", params = "time").text
                #Convierte el string con fecha y hora, en OBJETO de datetime
                currentTimeDate=datetime.fromisoformat(currentTimeDate)
                #Actualiza hora y fecha
                #obtiene la hora en string para mostrar en pantalla
                currentTime=currentTimeDate.strftime("%H:%M:%S")
                self.hora.setText(currentTime)
                #obtiene la fecha en string para mostrar en pantalla
                today=currentTimeDate.strftime("%d/%m/%Y")
                self.fecha.setText(today)
            
                #La variable status contiene el estado global del equipo.
                """with open(main.usersFile) as us:
                    self.users=json.load(us)"""
                
                #Lee el estado global del equipo
                self.status=json.loads(requests.get(f"{main.localhost}/status").text)
                main.lightOnOff=self.status.get("LED_Light")
                main.uvOnOff=self.status.get("UV_Light")

                #Lee los valores de ADC para mostrar vel de flujo y presión en el dial
                #print("Pide ADC")
                medicionesADC = json.loads(requests.get(f"{main.localhost}/adc").text)
                #print(medicionesADC)
                flujoEntrada_aux=float(medicionesADC['flujoEntrada'])
                flujoSalida_aux=float(medicionesADC['flujoSalida'])
                self.flujoEntradaLbl.setText("{:.2f} m/s".format(flujoEntrada_aux))
                self.flujoSalidaLbl.setText("{:.2f} m/s".format(flujoSalida_aux))
                self.presionEntradaDial(float(medicionesADC['presionEntrada']))
                self.presionSalidaDial(float(medicionesADC['presionSalida']))
                

                #self.currentUser=self.users.get(self.status.get("screenUser"))
                #print(self.currentUser)
                #self.userLbl.setText(self.currentUser['name'])
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
            response = requests.post(f"{main.localhost}/status",params= {"LED_Light" : main.lightOnOff})
            #TODO si no obtiene respuesta de "request.post" debería hacer algo, 
            # y/o ejecutar el servidor de estado
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
        if(not self.uv_Btn.isDown()):
            main.UV_OnOff=self.uv_Btn.isChecked()
            response = requests.post(f"{main.localhost}/status",params= {"UV_Light" : main.UV_OnOff})
            #TODO si no obtiene respuesta de "request.post" debería hacer algo, 
            # y/o ejecutar el servidor de estado
        else:
            if(main.UV_OnOff != self.uv_Btn.isChecked()):
                self.uv_Btn.toggle()

            #print("UV_Config window open")
            self.uvWindow = UVWindow()
            self.uvWindow.show()
#**************************************************************************************************************

#**************************************************************************************************************
#Ventana de advertencia         - Muestra las advertencias existentes
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
#Calendar window                - Configura hora y fecha de inicio/fin de encendido de rutina o luz Uv
    def Calendar(self): 
        self.calendarWindow = CalendarWindow()
        self.calendarWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
#Clock window                   - setea fecha, hora, y uso horario
    def Clock(self):
        self.clockWindow = ClockWindow()
        self.clockWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
    def presionEntradaDial(self, presion):
        stopValue = presion / 4096

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
        style=f"""
            QFrame{{
                    border-radius: 138px;
                    background-image: url();
                    background-color: qradialgradient(
                        spread:pad, 
                        cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
                        stop:{stopValue} rgba(255, 255, 255, 0), 
                        stop:{gradient} rgba{color}
                        );
            }}"""
        self.presionEntradaBar.setStyleSheet(style)

    def presionSalidaDial(self, presion):
        stopValue= presion / 4096.0

        #print(f"stopValue: {stopValue}")
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

        style=f"""
            QFrame{{
                    border-radius: 138px;
                    background-image: url();
                    background-color: qradialgradient(
                        spread:pad, 
                        cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
                        stop:{stopValue} rgba(255, 255, 255, 0), 
                        stop:{gradient} rgba{color}
                        );
            }}"""
        self.presionSalidaBar.setStyleSheet(style)

