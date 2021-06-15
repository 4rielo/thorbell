#*********************************************************************
# Status server:
#               Este archivo se ejecuta al inicio, antes de comenzar
# el programa de la pantalla principal. Corre dentro de un puerto 
# interno de localhost, y mediante métodos de GET y POST, recibe y 
# devuelve el estado de las variables globales. 
#               Cuando se realiza una modificación digna de almacenar
# en el disco duro, éste es el único punto donde se realizará dicho
# proceso, reduciendo la escritura y el acceso al disco al mínimo
# posible, ya que el estado global de la mayoría de las variables
# que se necesita acceder van a estar almacenadas en memoria RAM,
# dentro de la ejecución de éste archivo.

import web
import subprocess
import requests
import time
import json
import datetime
import threading

#Módulos de manejo de puertos de I/O e I2C
import ADS1115
import MCP23017
from DS3231 import DS3231
import OPi.GPIO as GPIO                 #Para PWM en RA5 (PWM0)

from pyA20.gpio import gpio             #Para PWM por software en PA6 (pin 7)    
from pyA20.gpio import port
from orangepwm import *

import random

#Variables "globales", que se acceden en las distintas clases que atienden
# las solicitudes
global status
global statusFile
mediciones = dict()
#  Cuando sea necesario actualizar algún estado de manera permanente, como el idioma,
# alguna fecha/hora, o advertencias, se escribirá el archivo status.dat
#  Para saber si el dato modificado debe ser almacenado en el archivo de status, 
# tengo una lista de "essentials", que se revisa cuando se recibe un POST.
#  Si el "key" de la solicitud de modificación se encuentra en la lista de "essentials"
# se almacena la modificación en el archivo "status.dat"
global essentials 
essentials = ( 
                "UV_Timer",
                "UV_Calendar",
                "UV_Calendar_init",
                "UV_Calendar_end",
                "Rutina_Calendar",
                "Rutina_Calendar_init",
                "Rutina_Calendar_end",
                "WARNINGS"
            )

#################################################################################

#PWM por software, con librería orangepwm, y pyA20
gpio.init()
pwm = OrangePwm(100, port.PA6)          #100Hz en PA6
pwm.start(0)

#PWM0 - Configuración con librería OPi.GPIO
PWM_chip = 0
PWM_pin = 0
frequency_Hz=2000
Duty_Cycle_Percent=0
LED = GPIO.PWM(PWM_chip, PWM_pin, frequency_Hz, Duty_Cycle_Percent)
LED.start_pwm(0)

#Crea una instancia de la lectura/escritura del reloj RTC 
RTC = DS3231()
#################################################################################

#Las direcciones sobre las que recibe solicitudes de microservicios "status"
urls = ('/','root', '/status', 'Status','/adc','ADC', '/reboot','reboot')
app = web.application(urls,globals())

#Dirección de la carpeta, donde se encuentra el archivo ejecutado
path = __file__.replace("/statusServer.py","")
if(not path):
    path = "."

#Dirección de la ubicación del archivo "status.dat"
statusFile= f"{path}/CSB_MercurioR1/status.dat"

#intenta abrir el archivo "status.dat"
try:                 
    print("Trying to open status file")
    f=open(statusFile)              #Busca el archivo statusFile, si existe, lo abre
    status = json.load(f)             #y carga el último estado guardado
    f.close()                       #(cierra el archivo, no lo necesita por ahora)
    print("Status File found, reading initial status")
except:                             #Si no econtró el arvchivo
    status = {                        #genera un status inicial
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
    with open(statusFile, "w") as f:                   #Y lo guarda en statusFile (crea el archivo)
        json.dump(data,f)
    print("Status file not found. Creates initial ( default) status file")

#TODO: Aquí se obtiene el tiempo del reloj SPI, y se revisa si hay conexión a 
# internet. 

#################################################################################

class root:
    def __init__(self):
        self.hello="Please go to /scan to search for available networks"

    def GET(self):
        return self.hello

class reboot:
    def GET(self):
        input = web.input()
        for x in input.keys():
            if(x == "reboot"): 
                command = "reboot"
                subprocess.run(command,shell=True)

class Status:
    #Variables globales obtenidas del archivo status.dat
    global status
    global essentials
    #####################################################
    def __init__(self):
        #GPIO.setboard(GPIO.)
        global LED
        
        pass

    def GET(self):              #Aquí defino qué variable quiero leer, ej: GET -> status?Idioma
        input = web.input()
        #print("Input:")
        #print(input)
        for x in input.keys():              #analizo la clave ("key") recibida en la solicitud
            #print("Key: " + str(x))
            if(x == "time"):                 #consulto la hora
                #TODO: currentTimeDate es el valor obtenido del RTC, NO la hora del sistema
                timeRTC = RTC.readTimeString()
                while(timeRTC == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.005)                           #Espera un muy breve instante a que se desocupe
                    timeRTC = RTC.readTimeString()              #Y vuelve a consultar la hora

                dateRTC = RTC.readDateString()
                while(dateRTC == "ERROR"):                      #Dió error, debido a un intento fallido de acceso al puerto I2C
                    time.sleep(0.005)                           #Espera un muy breve instante a que se desocupe
                    dateRTC = RTC.readDateString()              #Y vuelve a consultar la fecha

                currentTime = datetime.time.fromisoformat(timeRTC)       #gets datetime object
                currentDate = datetime.datetime.fromisoformat(dateRTC)
                currentTimeDate = datetime.datetime(year=currentDate.year,
                                                    month=currentDate.month,
                                                    day = currentDate.day,
                                                    hour=currentTime.hour,
                                                    minute=currentTime.minute,
                                                    second=currentTime.second)
                #print (currentTimeDate)
                return currentTimeDate
            if(x=='ADC'):
                return str(readValues())
            if x in status:                 #Y si se encuentra en la variable "status"
                #print(str({x : status.get(x)}))
                return json.dumps({x : status.get(x)})                  #Devuelvo el valor correspondiente
        else:                   #Si no especificó ningun parámetro en particular, devuelve el objeto entero
            #print(status)
            return json.dumps(status)

    def POST(self):         #Aquí defino qué variables quiero modificar, ej: GET -> status?Idioma="es-AR"
        input = web.input()
        # Todo lo recibido con POST, es un string, así que debo analizar el valor
        #de la solicitud, para ver si es un número, o un valor booleano
        for x in input.keys():              #Analizo las claves ("key") de lo solicitado
            try:                            #Primero reviso si el valor recibido es un número
                if(int(input[x])):          
                    input[x] = int(input[x])        #Es un número, lo reescribo como tal
                #print(input[x])
                #print(type(input[x]))
            except:                                 #No es un número
                print("Not a Number")               #devuelve una excepción la instrucción "int(input[x])"

            if(input[x]=="True"):                   #Si el valor de la solicitud es el texto "True"
                input[x]=True                       #sobreescribo con la variable booleana True
            elif(input[x]=="False"):                #Lo mismo si es el texto "False"
                input[x]=False                      #sobreescribo con la variable booleana False
            status.update({x:input[x]})             #y actualizo el valor en la variable "status"

        storeInStatus = False           #pre define que no es una variable digna de almacenar en archivo
        for a in input.keys():          #Según la clave de lo solicitado,
            if a in essentials:         #Busca si se encuentra dentro de las variables esenciales
                #storeInStatusp=True           #Si corresponde, actualiza el archivo status.dat
                with open(statusFile, "w") as st:
                    json.dump(status,st)

            if (a == 'LED_Light'):          #se quiere encender o apagar la luz LED
                if(input[a]):
                    LED.duty_cycle(status.get('LEDPWM'))
                else:
                    LED.duty_cycle(0)
                
            if(a == 'LEDPWM'):
                if(status.get('LED_Light')):
                    LED.duty_cycle(status.get('LEDPWM'))

            if(a == 'UV_Light'):
                if(input[a]):
                    pwm.changeDutyCycle(status.get('LEDPWM'))
                else:
                    pwm.changeDutyCycle(0)

        #Finalmente, devuelve el valor de la variable status que se modificó
        return json.dumps({x: status.get(x) for x in input.keys()})

class ADC:
    def __init__(self):
        global mediciones

    def GET(self):
        time.sleep(0.01)

        input = web.input()             #What ADC reading was requested
        for x in input.keys():          
            pass
        #print(f"GET: {mediciones}")
        return json.dumps(mediciones)
        
    def POST(self):
        input = web.input()
        for x in input.keys():
            mediciones[x] = input[x]

        #print(f"POST: {mediciones}")
        return "Ok"

class TIMER:
    def __init__(self):
        self.flujoEntrada=float()
        self.flujoSalida=float()
        self.presionEntrada=float()
        self.presionSalida=float()

        self.status=dict()

        self.status = json.loads(app.request("/status", method = 'GET').data)

        self.mediciones = { 'flujoEntrada' : self.flujoEntrada , 
                        'flujoSalida' : self.flujoSalida , 
                        'presionEntrada' : self.presionEntrada , 
                        'presionSalida' : self.presionSalida
                        }

    def timer10ms(self):
        sec1=0 
        ads1 = 0x48
        ads2 = 0x49

        ADS1115_FS_4096 = 1
        ADS1115_FS_2048 = 2
        ADS1115_FS_1024 = 3
        ADS1115_FS_512 = 4

        acumTmp_flujoEntrada = 0
        acumRv_flujoEntrada = 0

        acumTmp_flujoSalida = 0
        acumRv_flujoSalida = 0

        acumPresion_Entrada = 0
        acumPresion_Salida = 0

        contadorMediciones = 0

        while(True):

            sec1 += 1

            if(not sec1%10):             #cada 100 ms
                #Mido temperatura y Rv de flujo de entrada, y acumulo para sacar medición promedio
                acumTmp_flujoEntrada += ADS1115.ReadADC(ads1,5,ADS1115_FS_4096)
                acumRv_flujoEntrada += ADS1115.ReadADC(ads1,4,ADS1115_FS_4096)

                #Mido temperatura y Rv de flujo de salida, y acumulo para sacar medición promedio
                acumTmp_flujoSalida += ADS1115.ReadADC(ads1,7,ADS1115_FS_4096)
                acumRv_flujoSalida += ADS1115.ReadADC(ads1,6,ADS1115_FS_4096)

                acumPresion_Entrada += ADS1115.ReadADC(ads2,4,ADS1115_FS_512)
                acumPresion_Salida += ADS1115.ReadADC(ads2,5,ADS1115_FS_512) #"""
                
                """#bloque de números RANDOM para probar el código en la PC
                acumTmp_flujoEntrada += random.randint(1000,2096)
                acumRv_flujoEntrada += random.randint(2000,3096)

                #Mido temperatura y Rv de flujo de salida, y acumulo para sacar medición promedio
                acumTmp_flujoSalida += 100#random.randint(00,500)
                acumRv_flujoSalida += random.randint(2000,2500)

                acumPresion_Entrada += random.randint(1000,2096)
                acumPresion_Salida += random.randint(2000,2596) #"""
                contadorMediciones +=1          #incremento la cantidad de mediciones

                if(contadorMediciones>9):        #10 mediciones para calcular el promedio (contador de 0 a 9)

                    """Cálculo de flujo de Entrada"""
                    rvEntrada = acumRv_flujoEntrada/10.0          #promedio de 10 mediciones
                    tmpEntrada = acumTmp_flujoEntrada/10.0        #promedio de 10 mediciones
                    
                    #Fórmula obtenida de software de PIC, extraida de hoja de datos del sensor de flujo de aire
                    velCeroEntrada = -0.0006 * tmpEntrada * tmpEntrada / 1024.0 + 1.0727 * tmpEntrada/32.0 + 8.172
                    rvEntrada /= 32.0
                    velCeroEntrada = (rvEntrada - velCeroEntrada) * 0.01739
                    if(velCeroEntrada < 0):
                        velCeroEntrada = 0.0
                    
                    self.flujoEntrada = pow(velCeroEntrada,2.7265) * 160.934

                    """Cálculo de flujo de Salida"""
                    rvSalida = acumRv_flujoSalida/10.0          #promedio de 10 mediciones
                    tmpSalida = acumTmp_flujoSalida/10.0        #promedio de 10 mediciones
                    
                    #Fórmula obtenida de software de PIC, extraida de hoja de datos del sensor de flujo de aire
                    velCeroSalida = -0.0006 * tmpSalida * tmpSalida / 1024.0 + 1.0727 * tmpSalida/32.0 + 8.172
                    rvSalida /= 32.0
                    velCeroSalida = (rvSalida - velCeroSalida) * 0.01739
                    if(velCeroSalida < 0):
                        velCeroSalida = 0.0
                    
                    self.flujoSalida = pow(velCeroSalida,2.7265) * 160.934

                    """Cálculo de presion de flujo de entrada """
                    self.presionEntrada = acumPresion_Entrada/10

                    """Cálculo de presion de flujo de salida """
                    self.presionSalida = acumPresion_Salida/10

                    """Recopilo todas las mediciones en un dict"""
                    self.mediciones = { 'flujoEntrada' : self.flujoEntrada , 
                        'flujoSalida' : self.flujoSalida , 
                        'presionEntrada' : self.presionEntrada , 
                        'presionSalida' : self.presionSalida
                        }
                    #y lo envío al servidor, para que la pantalla y app web tengan un nuevo valor
                    print(f"ADC: {self.mediciones}")
                    postData = app.request("/adc" , method ='POST' , data = self.mediciones)
                    
                    """ Reinicio contadores y acumuladores a cero"""
                    acumTmp_flujoEntrada=0
                    acumRv_flujoEntrada=0

                    acumTmp_flujoSalida=0
                    acumRv_flujoSalida=0

                    acumPresion_Entrada = 0
                    acumPresion_Salida = 0

                    contadorMediciones=0

                    self.status = json.loads(app.request("/status", method = 'GET').data)

            if(sec1>100):       #Pasó 1 segundo
                sec1=0
                if(self.status.get('UV_Light')):
                    print("Turn on that damn light!!!")


            time.sleep(0.01)


if __name__ == "__main__":
    loopTimer = TIMER()
    clock = threading.Thread(target=loopTimer.timer10ms,daemon=True)
    clock.start()

    app.run()
