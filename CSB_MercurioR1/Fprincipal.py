#Fprincipal.py
import sys
import PySide2
from PySide2 import QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader

import time
#import threading
import requests
import json
from datetime import datetime, date

#GPIO and I2C handling
import ADS1115 
import OPi.GPIO as OPiGPIO                 #GPIO handling library

from Pprincipal import Ui_form              #El formulario descriptivo de qué contiene ésta ventana
from Fconfig import ConfigWindow            #Config window 
from Fluminaria_led import LEDWindow        #Luminaria LED window (para dimerizar la luz)
from Fluminaria_ledUV import UVWindow       #Luminaria UV window (para configurar un timer de apagado)
from Fadvertencias import AdvertenciaWindow #Advertencia window (Muestra las advertencias)
from Fcalendar import CalendarWindow        #Calendario, setea hora de inicio y fin de rutina y/o luz UV
from Fclock import ClockWindow              #Setea fecha, hora y uso horario
from Fpuerta import PuertaWindow            #Menu para manipular la puerta motorizada
from FroutineAnimation import RoutineAnimationWindow            #Animation for routine start

#import FfirebaseUpload

import main         #to read the lightOnOff status


class MainWindow(QtWidgets.QMainWindow, Ui_form):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)

        self.setWindowTitle("THORBELL")

        try:
        #Obtiene el estado global del servidor de estado
            response = requests.get(f"{main.localhost}/status").text
            self.status = json.loads(str(response))
        except:
            self.status = {                        #genera un status inicial
                "Idioma": "es-AR", 
                
                "LED_Light": False, 
                "LEDPWM": 100, 
                
                "UV_Light": False, 
                "UV_TimerEnable": False,
                "UV_Timer": 0, 
                
                "UVLEDPWM": 100, 
                
                "UV_Calendar": False, 
                "UV_Calendar_init": format(datetime.now(),"%Y/%m/%d %H:%M"), 
                "UV_Calendar_end": format(datetime.now(),"%Y/%m/%d %H:%M"), 

                "Rutina_Calendar": False,
                "Rutina_Calendar_init": format(datetime.now(),"%Y/%m/%d %H:%M"), 
                "Rutina_Calendar_end": format(datetime.now(),"%Y/%m/%d %H:%M"), 

                "PWR": False, 

                "screenUser": "", 

                "webUsers": {
                    "userA": {
                        "ip": "", 
                        "user": ""
                    }
                }, 
                "WARNINGS": [],
                "GMT": 0
            }
        #Idioma almacenado en el estado del equipo
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            with open(f"{main.path}/idioma/{self.status.get('Idioma')}.dat") as f:
                main.texto = json.load(f)
            self.idioma = main.texto

        #Pone los textos de los pulsadores de acuerdo al idioma elegido
        self.LED_label.setText(self.idioma.get("luminariaLED"))
        self.UV_label.setText(self.idioma.get("luminariaUV"))
        self.ControlPuerta_label.setText(self.idioma.get("puerta"))
        self.Rutina_label.setText(self.idioma.get("rutina"))

        #Estado inicial de las variables
        main.lightOnOff = self.status.get("LED_Light")
        main.lightPercent = self.status.get("LEDPWM")
        main.uvOnOff = self.status.get("UV_Light")
        main.UV_Timer=self.status.get("UV_Timer")
        main.UV_TimerEnable= self.status.get("UV_TimerEnable")

        #Botón de configuración, cuando se clickea, conecta con "Config()""
        self.config_Btn.clicked.connect(self.Config)
        #Botón de calendario, cuando se clickea, conecta con "Calendar()"
        self.calendario_Btn.clicked.connect(self.Calendar)
        #Botón de reloj, cuando se clickea, conecta con "Clock()"
        self.reloj_Btn.clicked.connect(self.Clock)
        #Botón de Rutina, conecta con "routineAnimation()"
        self.rutina_Btn.clicked.connect(self.RoutineWindow)
      

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

        #Botón de control de puerta
        self.puerta_Btn.clicked.connect(self.puertaClicked)

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

        #Timer counters de 100ms y 1s, para base de tiempo de ejecución. 
        self.ms100=0
        self.s1=0
        
        self.flujoEntrada=float()
        self.flujoSalida=float()
        self.presionEntrada=float()
        self.presionSalida=float()

        self.medicionesADC=0

        self.ads1 = 0x48
        self.ads2 = 0x49

        self.ADS1115_FS_4096 = 1
        self.ADS1115_FS_2048 = 2
        self.ADS1115_FS_1024 = 3
        self.ADS1115_FS_512 = 4

        self.acumTmp_flujoEntrada = 0
        self.acumRv_flujoEntrada = 0

        self.acumTmp_flujoSalida = 0
        self.acumRv_flujoSalida = 0

        self.acumPresion_Entrada = 0
        self.acumPresion_Salida = 0

        self.lectura=0
        self.contadorMediciones=0          #incremento la cantidad de mediciones

        self.TimingTimer.timeout.connect(self.timer10ms)
        self.TimingTimer.start()

    #FIN init

    def updateLanguage(self):
        try:
            response = requests.get(f"{main.localhost}/language").text
            self.idioma=json.loads(response)
        except:
            with open(f"{main.path}/idioma/{self.status.get('Idioma')}.dat") as f:
                main.texto = json.load(f)
            self.idioma = main.texto

        self.LED_label.setText(self.idioma.get("luminariaLED"))
        self.UV_label.setText(self.idioma.get("luminariaUV"))
        self.ControlPuerta_label.setText(self.idioma.get("puerta"))
        self.Rutina_label.setText(self.idioma.get("rutina"))


    def UpdateData(self, payload):
        self.firebaseLbl.setText(payload)

#**********************************************************************************************
# Timer de 10 ms. 
# Aquí se lee el "status.dat", y se actualiza el estado de las salidas
# Cada un segundo se actualiza el reloj en pantalla.

    def timer10ms(self):           #recurrent timer - base de tiempo de 100ms para chekear estado de las cosas
        #revisa el estado de la luz led, y setea el botón de luz de acuerdo
        #Compara contra "main.ligthOnOff", ya que éste valor se modifica
        #dentro del menú de LuminariaLED
        if(self.luz_Btn.isChecked() != main.lightOnOff):
            self.luz_Btn.toggle()
        if(self.uv_Btn.isChecked() != main.uvOnOff):
            self.uv_Btn.toggle()

        self.s1 +=1
        self.ms100 += 1

        #Mediciones de ADC:

        #Mido temperatura y Rv de flujo de entrada, y acumulo para sacar medición promedio
        if(not self.lectura):
            ADC_reading=ADS1115.ReadADC(self.ads1,5,self.ADS1115_FS_4096)     #intenta leer
            while(ADC_reading == "ERROR"):                      #si devuelve ERROR (puerto I2C ocupado)
                time.sleep(0.001)                               #espera 3 ms
                ADC_reading=ADS1115.ReadADC(self.ads1,5,self.ADS1115_FS_4096) #e intenta nuevamente
            self.acumTmp_flujoEntrada += ADC_reading
            self.lectura += 1
        elif(self.lectura == 1):
            ADC_reading=ADS1115.ReadADC(self.ads1,4,self.ADS1115_FS_4096)
            while(ADC_reading == "ERROR"):
                time.sleep(0.001)
                ADC_reading=ADS1115.ReadADC(self.ads1,4,self.ADS1115_FS_4096)
            self.acumRv_flujoEntrada += ADC_reading
            self.lectura += 1
        elif(self.lectura==2):
            #Mido temperatura y Rv de flujo de salida, y acumulo para sacar medición promedio
            ADC_reading=ADS1115.ReadADC(self.ads1,7,self.ADS1115_FS_4096)
            while(ADC_reading == "ERROR"):
                time.sleep(0.001)
                ADC_reading=ADS1115.ReadADC(self.ads1,7,self.ADS1115_FS_4096)
            self.acumTmp_flujoSalida += ADC_reading
            self.lectura += 1
        elif(self.lectura==3):
            ADC_reading=ADS1115.ReadADC(self.ads1,6,self.ADS1115_FS_4096)
            while(ADC_reading == "ERROR"):
                time.sleep(0.001)
                ADC_reading=ADS1115.ReadADC(self.ads1,6,self.ADS1115_FS_4096)
            self.acumRv_flujoSalida += ADC_reading
            self.lectura += 1
        elif(self.lectura==4):
            ADC_reading=ADS1115.ReadADC(self.ads2,4,self.ADS1115_FS_512)
            while(ADC_reading == "ERROR"):
                time.sleep(0.001)
                ADC_reading=ADS1115.ReadADC(self.ads2,4,self.ADS1115_FS_512)
            self.acumPresion_Entrada += ADC_reading
            self.lectura += 1
        elif(self.lectura==5):
            ADC_reading=ADS1115.ReadADC(self.ads2,5,self.ADS1115_FS_512) 
            while(ADC_reading == "ERROR"):
                time.sleep(0.001)
                ADC_reading=ADS1115.ReadADC(self.ads2,5,self.ADS1115_FS_512) 
            self.acumPresion_Salida += ADC_reading #"""
            self.lectura=0
            self.contadorMediciones +=1          #incremento la cantidad de mediciones (hizo un loop completo de medidas)

        """#bloque de números RANDOM para probar el código en la PC
        self.acumTmp_flujoEntrada += random.randint(1000,2096)
        self.acumRv_flujoEntrada += random.randint(2000,3096)

        #Mido temperatura y Rv de flujo de salida, y acumulo para sacar medición promedio
        self.acumTmp_flujoSalida += 100#random.randint(00,500)
        self.acumRv_flujoSalida += random.randint(2000,2500)

        self.acumPresion_Entrada += random.randint(1000,2096)
        self.acumPresion_Salida += random.randint(2000,2596) #"""

        if(self.contadorMediciones>9):        #10 mediciones para calcular el promedio (contador de 0 a 9)

            """Cálculo de flujo de Entrada"""
            rvEntrada = self.acumRv_flujoEntrada/10.0          #promedio de 10 mediciones
            tmpEntrada = self.acumTmp_flujoEntrada/10.0        #promedio de 10 mediciones
            
            #Fórmula obtenida de software de PIC, extraida de hoja de datos del sensor de flujo de aire
            velCeroEntrada = -0.0006 * tmpEntrada * tmpEntrada / 1024.0 + 1.0727 * tmpEntrada/32.0 + 8.172
            rvEntrada /= 32.0
            velCeroEntrada = (rvEntrada - velCeroEntrada) * 0.01739
            if(velCeroEntrada < 0):
                velCeroEntrada = 0.0
            
            self.flujoEntrada = pow(velCeroEntrada,2.7265) * 160.934

            """Cálculo de flujo de Salida"""
            rvSalida = self.acumRv_flujoSalida/10.0          #promedio de 10 mediciones
            tmpSalida = self.acumTmp_flujoSalida/10.0        #promedio de 10 mediciones
            
            #Fórmula obtenida de software de PIC, extraida de hoja de datos del sensor de flujo de aire
            velCeroSalida = -0.0006 * tmpSalida * tmpSalida / 1024.0 + 1.0727 * tmpSalida/32.0 + 8.172
            rvSalida /= 32.0
            velCeroSalida = (rvSalida - velCeroSalida) * 0.01739
            if(velCeroSalida < 0):
                velCeroSalida = 0.0
            
            self.flujoSalida = pow(velCeroSalida,2.7265) * 160.934

            """Cálculo de presion de flujo de entrada """
            self.presionEntrada = self.acumPresion_Entrada/10

            """Cálculo de presion de flujo de salida """
            self.presionSalida = self.acumPresion_Salida/10

            """Recopilo todas las mediciones en un dict"""
            self.medicionesADC = { 'flujoEntrada' : self.flujoEntrada , 
                'flujoSalida' : self.flujoSalida , 
                'presionEntrada' : self.presionEntrada , 
                'presionSalida' : self.presionSalida
                }
            #y lo envío al servidor, para que la pantalla y app web tengan un nuevo valor
            #print(f"ADC: {self.medicionesADC}")
            try:
                postData = requests.post(f"{main.localhost}/adc" , params = self.medicionesADC)
            except:
                pass

            """ Reinicio contadores y acumuladores a cero"""
            self.acumTmp_flujoEntrada=0
            self.acumRv_flujoEntrada=0

            self.acumTmp_flujoSalida=0
            self.acumRv_flujoSalida=0

            self.acumPresion_Entrada = 0
            self.acumPresion_Salida = 0

            self.contadorMediciones=0


        #Pasó 1 segundo
        if(self.s1>100):
            self.s1=0

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
            """try:
                medicionesADC = json.loads(requests.get(f"{main.localhost}/adc").text)
            except:
                medicionesADC = {
                    'flujoEntrada':1000,
                    'flujoSalida' : 1000,
                    'presionEntrada' : 1000,
                    'presionSalida' : 1000,
                }
            
                print(medicionesADC)"""
            flujoEntrada_aux=float(self.medicionesADC['flujoEntrada'])
            flujoSalida_aux=float(self.medicionesADC['flujoSalida'])
            self.flujoEntradaLbl.setText("{:.2f} m/s".format(flujoEntrada_aux))
            self.flujoSalidaLbl.setText("{:.2f} m/s".format(flujoSalida_aux))
            self.presionEntradaDial(float(self.medicionesADC['presionEntrada']))
            self.presionSalidaDial(float(self.medicionesADC['presionSalida']))
            

            #self.currentUser=self.users.get(self.status.get("screenUser"))
            #print(self.currentUser)
            #self.userLbl.setText(self.currentUser['name'])

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
            try:
                response = requests.post(f"{main.localhost}/status",params= {"LED_Light" : main.lightOnOff})
            except:
                #TODO: handle microservises request failure
                pass
            
        else:
            if(main.lightOnOff != self.luz_Btn.isChecked()):
                self.luz_Btn.toggle()

            self.ledWindow = LEDWindow()
            self.ledWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
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
            main.uvOnOff=self.uv_Btn.isChecked()
            try:
                response = requests.post(f"{main.localhost}/status",params= {"UV_Light" : main.uvOnOff})
            except:
                #TODO: handle microservises request failure
                pass
        else:
            if(main.uvOnOff != self.uv_Btn.isChecked()):
                self.uv_Btn.toggle()

            #print("UV_Config window open")
            self.uvWindow = UVWindow()
            self.uvWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
            self.uvWindow.show()
#**************************************************************************************************************

#**************************************************************************************************************
#Ventana de advertencia         - Muestra las advertencias existentes
    def advertenciaClicked(self):
        #print("Show Advertencia")
        self.advertenciaWindow = AdvertenciaWindow()
        self.advertenciaWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
        self.advertenciaWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
#Ventana de control de puerta
    def puertaClicked(self):
        self.puertaWindow = PuertaWindow()
        self.puertaWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
        self.puertaWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
#Ventana de configuración
    def Config(self):
        self.configWindow = ConfigWindow()
        self.configWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
        self.configWindow.destroyed.connect(self.updateLanguage)
        self.configWindow.show()

#**************************************************************************************************************
#Calendar window                - Configura hora y fecha de inicio/fin de encendido de rutina o luz Uv
    def Calendar(self): 
        self.calendarWindow = CalendarWindow()
        self.calendarWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
        self.calendarWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
#Clock window                   - setea fecha, hora, y uso horario
    def Clock(self):
        self.clockWindow = ClockWindow()
        self.clockWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
        self.clockWindow.show()

#**************************************************************************************************************

#**************************************************************************************************************
#Ventana de advertencia         - Muestra las advertencias existentes
    def RoutineWindow(self):
        #print("Show RoutineAnimation")
        self.routineWindow = RoutineAnimationWindow()
        self.routineWindow.setAttribute(PySide2.QtCore.Qt.WA_DeleteOnClose, True)
        self.routineWindow.show()

#**************************************************************************************************************


#**************************************************************************************************************
    def presionEntradaDial(self, presion):
        stopValue = round (presion / 4096.0 , 2)

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

    def presionSalidaDial(self, presion2):
        #print("Presion: " + str(presion))
        stopValue2= round(presion2 / 4096.0 , 2)

        #print(f"stopValue: {stopValue2}")

        gradient2 = stopValue2-0.05
        if(gradient2 < 0): 
            gradient2 = 0
            stopValue2 = 0.05
        if(stopValue2>1):
            stopValue2=1
        if(gradient2>1):
            gradient2=1
            
        if(stopValue2 < 0.15 or stopValue2 > 0.85 ):
            color2=(255, 0, 0, 145)
        elif(stopValue2 < 0.4 or stopValue2 > 0.6):
            color2=(255,197,0,145)
        else:
            color2=(51, 255, 151, 145)

        style2=f"""
            QFrame{{
                    border-radius: 138px;
                    background-image: url();
                    background-color: qradialgradient(
                        spread:pad, 
                        cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
                        stop:{stopValue2} rgba(255, 255, 255, 0), 
                        stop:{gradient2} rgba{color2}
                        );
            }}"""
        self.presionSalidaBar.setStyleSheet(style2)
